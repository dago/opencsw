#!/opt/csw/bin/python2.6
# coding=utf-8
# vim:set sw=2 ts=2 sts=2 expandtab:
#
# $Id$
#
# Copyright (c) 2009 Maciej Blizinski
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation.
# 
# Formats e-mail to the OpenCSW maintainer.
#
# To avoid leaking the e-mail addresses, they're base64-encoded:
#
# python -c "print repr('somebody@example.com'.encode('base64'))"
#
#
# The plan:
#
# 1. If necessary, move the relevant packages from /home/testing to
#    ~/to-release
# 2. Construct a list of all the files that are in ~/to-release
# 3. Clean newpkgs/ from the older versions of the files
# 4. Copy all the relevant files from ~/to-release to newpkgs/
# 5. Format the e-mail
# 6. Tell how to send it (no automatic sending for now)

import ConfigParser
import logging
import optparse
import os
import subprocess
import sys
import opencsw
import tag
import common_constants
import file_set_checker


CONFIG_INFO = """Create a file in ~/.releases.ini with the following content:

; A configuration file for the release automation script

[releases]
sender name = Your Name
sender email = your.email@opencsw.org
release manager name = Release Manager
release manager email = pkgsubmissions@lists.opencsw.org
; release cc = maintainers@example.com
; Usually it's /home/testing
package dir = /home/testing
target host = bender
target dir = /home/newpkgs
"""

CONFIGURATION_FILE_LOCATIONS = [
    "/etc/opt/csw/releases.ini",
    "%(HOME)s/.releases.ini",
]
CONFIG_REQUIRED_OPTS = [
    "sender name", "sender email",
    "release manager email",
    "package dir",
]
DEFAULT_FILE_NAME = "newpkgs.mail"
CONFIG_RELEASE_SECTION = "releases"

class Error(Exception):
  pass


class ConfigurationError(Error):
  pass


class PackageSubmissionError(Error):
  pass


def RemoveOldFiles(basename_list, host, directory):
  basename_str = " ".join(["%s/%s*" % (directory, x) for x in basename_list])
  args = ["ssh", host, "rm -f %s" % basename_str]
  logging.debug("Running: %s" % args)
  ret = subprocess.call(args)
  if ret:
    msg = ("Removing %s failed." % basename_str)
    raise PackageSubmissionError(msg)


def RsyncFiles(files_to_rsync, dst_arg):
  args = ["rsync", "-v"] + files_to_rsync + [dst_arg]
  logging.debug(args)
  try:
    ret = subprocess.call(args)
  except OSError, e:
    raise PackageSubmissionError(
        "Couldn't run %s, is the binary "
        "in the $PATH? The error was: %s" % (repr(args[0]), e))
  if ret:
    msg = ("Copying %s to %s has failed. "
           "Are you on the login host?" % (p, dst_arg))
    logging.error(msg)
    raise PackageSubmissionError(msg)

def DisplayCswUploadPkgTeaser(files_to_rsync):
  if not files_to_rsync:
    print "No files have been processed."
    return
  print
  print "Please try the new package upload tool."
  print "It will upload your packages to the opencsw-future catalog."
  print "http://mirror.opencsw.org/opencsw-future/"
  print "Once uploaded, your packages will be available in a couple hours."
  print "To upload, run the following command:"
  print
  script_path = os.path.join(
      os.path.dirname(sys.argv[0]),
      "csw-upload-pkg")
  print "%s \\" % script_path
  for f in files_to_rsync[:-1]:
    print "  %s \\" % f
  print "  %s" % files_to_rsync[-1]


def main():
  try:
    config = ConfigParser.SafeConfigParser()
    for file_name_tmpl in CONFIGURATION_FILE_LOCATIONS:
      config.read(file_name_tmpl % os.environ)
    for opt_name in CONFIG_REQUIRED_OPTS:
      if not config.has_option(CONFIG_RELEASE_SECTION, opt_name):
        logging.error("Option %s is missing from the configuration.",
                repr(opt_name))
        raise ConfigurationError("Option %s is missing from the configuration."
                           % repr(opt_name))
    usage = """%s [options] [file1 file2 ...]""" % sys.argv[0]
    parser = optparse.OptionParser(usage)
    parser.add_option("--debug",
                      dest="debug", default=False,
                      action="store_true",
                      help="Print debugging messages")
    parser.add_option("-d", "--package-dir",
                      dest="package_dir",
                      help="Specify the directory with packages")
    parser.add_option("--no-clean",
                      dest="clean", default=True,
                      action="store_false",
                      help="Prevent submitpkg from deleting old files from newpkgs")
    parser.add_option("-n", "--dry-run",
                      dest="dry_run",
                      default=False, action="store_true",
                      help="Do not perform write operations")
    parser.add_option("-f", "--force",
                       dest="force",
                       default=False, action="store_true",
                       help="Proceed even if errors are reported")
    (options, args) = parser.parse_args()
    file_names = args
    level = logging.INFO
    if options.debug:
      level = logging.DEBUG
    logging.basicConfig(level=level)
    if config.has_option(CONFIG_RELEASE_SECTION, "release manager name"):
      release_mgr_name = config.get(CONFIG_RELEASE_SECTION,
                                    "release manager name")
    else:
      release_mgr_name = None
    if config.has_option(CONFIG_RELEASE_SECTION, "release cc"):
      release_cc = config.get(CONFIG_RELEASE_SECTION, "release cc")
    else:
      release_cc = None
  except ConfigurationError, e:
    print "There was a problem with your configuration."
    print CONFIG_INFO
    print e
    sys.exit(1)

  package_dir = config.get(CONFIG_RELEASE_SECTION, "package dir")
  if options.package_dir:
    package_dir = options.package_dir
  staging_dir = opencsw.StagingDir(package_dir)
  catalognames = []
  for file_name in file_names:
    base_name = os.path.basename(file_name)
    parsed_file_name = opencsw.ParsePackageFileName(base_name)
    catalognames.append(parsed_file_name["catalogname"])
  catalognames = sorted(set(catalognames))
  if not file_names:
    parser.print_help()
    raise ConfigurationError("You need to specify package file names.")

  package_files = file_names
  logging.debug("Copying files to the target host:dir")
  remote_package_files = []
  remote_package_references = []
  files_to_rsync = []
  target_host = config.get(CONFIG_RELEASE_SECTION, "target host")
  target_dir = config.get(CONFIG_RELEASE_SECTION, "target dir")
  dst_arg = ("%s:%s" % (target_host, target_dir))
  for p in package_files:
    files_to_rsync.append(p)
    remote_package_files.append(dst_arg)
    package_base_file_name = os.path.split(p)[1]
    remote_package_references.append(dst_arg + "/" + package_base_file_name)
  fc = file_set_checker.FileSetChecker()
  error_tags = fc.CheckFiles(files_to_rsync)
  if error_tags:
    for error_tag in error_tags:
      print error_tag
    print "There seems to be a problem with the specified package set."
    if not options.force:
      sys.exit(1)
  if options.clean:
    RemoveOldFiles(catalognames, target_host, target_dir)
  if options.dry_run:
    print "files_to_rsync", files_to_rsync
    print "dst_arg", dst_arg
  else:
    RsyncFiles(files_to_rsync, dst_arg)
  nm = opencsw.NewpkgMailer(
      catalognames, remote_package_references,
      release_mgr_name=release_mgr_name,
      release_mgr_email=config.get(CONFIG_RELEASE_SECTION, "release manager email"),
      sender_name=config.get(CONFIG_RELEASE_SECTION, "sender name"),
      sender_email=config.get(CONFIG_RELEASE_SECTION, "sender email"),
      release_cc=release_cc)
  mail_text = nm.FormatMail()
  if options.dry_run:
    print "Not writing the e-mail to disk."
    print mail_text
  else:
    fd = open(DEFAULT_FILE_NAME, "w")
    fd.write(mail_text)
    fd.close()
    text_editor = nm.GetEditorName(os.environ)
    args = [text_editor, DEFAULT_FILE_NAME]
    editor_ret = subprocess.call(args)
    if editor_ret:
      raise Error("File editing has failed.")
    print
    print "Your e-mail hasn't been sent yet!"
    print "Issue the following command to have it sent:"
    print "sendmail -t < %s" % DEFAULT_FILE_NAME
  DisplayCswUploadPkgTeaser(files_to_rsync)


if __name__ == '__main__':
  main()
