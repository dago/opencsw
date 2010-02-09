#!/opt/csw/bin/python2.6
# $Id$

import os
import os.path
import shutil
import unittest
import tempfile
import subprocess
import copy
import sys

SHELL = "/bin/sh"

CONFIG_1 = """MIGRATE_FILES="%(migrate_files)s"
SOURCE_DIR___default__="%(srcdir)s"
DEST_DIR___default__="%(dstdir)s"
ARCH_DIR___default__="%(arcdir)s"
"""

class CswmigrateconfSetupMixin(object):
  """Sets up stuff for cswmigrateconf testing."""

  SRC_ETC = "src_etc"
  DST_ETC = "dst_etc"
  MIGRATION_ARCHIVE = "migration-archive"
  I_SCRIPT_PATH = "../files/CSWcswclassutils.i.cswmigrateconf"
  TMP_PREFIX = "csw-classutils-test-"
  SCRIPT_DEBUG = True

  def setUp(self):
    self.tmpdir = tempfile.mkdtemp(prefix=self.TMP_PREFIX)
    self.script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                    self.I_SCRIPT_PATH)
    self.mig_src_dir = os.path.join(self.tmpdir, self.SRC_ETC)
    self.mig_dst_dir = os.path.join(self.tmpdir, self.DST_ETC)
    self.mig_arc_dir = os.path.join(self.tmpdir, self.MIGRATION_ARCHIVE)
    os.mkdir(self.mig_src_dir)
    os.mkdir(self.mig_dst_dir)
    # os.mkdir(self.mig_arc_dir)
    config_content = CONFIG_1 % {
        "srcdir": self.mig_src_dir,
        "dstdir": self.mig_dst_dir,
        "arcdir": self.mig_arc_dir,
        "migrate_files": self.MIGRATE_FILES,
    }
    self.migraconf_conf_src_path = os.path.join(self.tmpdir, "cswmigrateconf_src")
    self.migraconf_conf_dst_path = os.path.join(self.tmpdir, "cswmigrateconf_dest")
    self.stdin_data = """%s %s\n""" % (self.migraconf_conf_src_path,
                                       self.migraconf_conf_dst_path)
    f = open(self.migraconf_conf_src_path, "w")
    f.write(config_content)
    f.close()

  def tearDown(self):
    shutil.rmtree(self.tmpdir)
  
  def RunActionScript(self):
    """Running the migration script."""
    classutils_env = copy.copy(os.environ)
    if self.SCRIPT_DEBUG:
      classutils_env["CLASSUTILS_DEBUG"] = "1"
    classutils_env["CLASSUTILS_SKIP_WARNING"] = "1"
    args = [SHELL, self.script_path]
    migconf_proc = subprocess.Popen(args,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    cwd="/",
                                    env=classutils_env)
    stdout, stderr = migconf_proc.communicate(self.stdin_data)
    retcode = migconf_proc.wait()
    print stdout
    if stderr:
      print "stderr", stderr
    self.assertFalse(retcode, "Running %s has failed" % args)

  def CreateMigrationFiles(self):
    for d in self.DIRS:
      os.mkdir(os.path.join(self.mig_src_dir, d))
    for file_name, file_content in self.FILES:
      f = open(os.path.join(self.mig_src_dir, file_name), "w")
      f.write(file_content)
      f.close()


class CswmigrateconfUnitTest(CswmigrateconfSetupMixin, unittest.TestCase):

  MIGRATE_FILES = "file0 dir0"
  SCRIPT_DEBUG = False
  DIRS = ["dir0", "dir0/dir1"]
  FILES = [
      # ("file name", "content\n")
      ("file0",           "# Test config file.\n"),
      ("dir0/file1",      "# Second test config file.\n"),
      ("dir0/dir1/file2", "# Third test config file.\n"),
  ]

  def test_1(self):
    self.CreateMigrationFiles()
    subprocess.call(["tree", self.tmpdir])
    self.RunActionScript()
    subprocess.call(["tree", self.tmpdir])
    self.RunActionScript()
    subprocess.call(["tree", self.tmpdir])
    # Tests go here

if __name__ == '__main__':
	unittest.main()
