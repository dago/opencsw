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
import datetime
import logging
import optparse
import os
import subprocess
import sys
import opencsw


CONFIG_INFO = """Create a file in ~/.releases.ini with the following content:

; A configuration file for the release automation script

[releases]
sender name = Your Name
sender email = your.email@example.com
release manager name = Release Manager
release manager email = their.email@example.com
release cc = maintainers@example.com
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
    "release manager name", "release manager email",
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
    parser = optparse.OptionParser()
    parser.add_option("-p", "--pkgnames",
                      dest="pkgnames",
                      help="A comma-separated list of pkgnames: "
                           "cups,cupsdevel,libcups")
    parser.add_option("-d", "--debug",
                      dest="debug", default=False,
                      action="store_true",
                      help="Print debugging messages")
    (options, args) = parser.parse_args()
    level = logging.WARN
    if options.debug:
      level = logging.DEBUG
    logging.basicConfig(level=level)
    if not options.pkgnames:
      parser.print_help()
      raise ConfigurationError("You need to specify a package name or names.")
    if config.has_option(CONFIG_RELEASE_SECTION, "release cc"):
      release_cc = config.get(CONFIG_RELEASE_SECTION, "release cc")
    else:
      release_cc = None
  except ConfigurationError, e:
    print "There was a problem with your configuration."
    print CONFIG_INFO
    print e
    sys.exit(1)
  pkgnames = options.pkgnames.split(",")
  package_files = []
  staging_dir = opencsw.StagingDir(config.get(CONFIG_RELEASE_SECTION,
                                                  "package dir"))
  for p in pkgnames:
    package_files.extend(staging_dir.GetLatest(p))
  logging.debug("Copying files to the target host:dir")
  remote_package_files = []
  remote_package_references = []
  files_to_rsync = []
  for p in package_files:
    dst_arg = ("%s:%s" % (config.get(CONFIG_RELEASE_SECTION, "target host"),
                          config.get(CONFIG_RELEASE_SECTION, "target dir")))
    files_to_rsync.append(p)
    remote_package_files.append(dst_arg)
    package_base_file_name = os.path.split(p)[1]
    remote_package_references.append(dst_arg + "/" + package_base_file_name)
  # TODO(maciej): rsync only once
  args = ["rsync", "-v"] + files_to_rsync + [dst_arg]
  logging.debug(args)
  try:
    ret = subprocess.call(args)
  except OSError, e:
    raise PackageSubmissionError(
        "Couldn't run %s, is the binary "
        "in the $PATH? The error was: %s" % (repr(args[0]), e))
  if ret:
    msg = "Copying %s to %s has failed." % (p, dst_arg)
    logging.error(msg)
    raise PackageSubmissionError(msg)
  nm = opencsw.NewpkgMailer(
      pkgnames, remote_package_references,
      release_mgr_name=config.get(CONFIG_RELEASE_SECTION, "release manager name"),
      release_mgr_email=config.get(CONFIG_RELEASE_SECTION, "release manager email"),
      sender_name=config.get(CONFIG_RELEASE_SECTION, "sender name"),
      sender_email=config.get(CONFIG_RELEASE_SECTION, "sender email"),
      release_cc=release_cc)
  mail_text = nm.FormatMail()
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


if __name__ == '__main__':
  main()
