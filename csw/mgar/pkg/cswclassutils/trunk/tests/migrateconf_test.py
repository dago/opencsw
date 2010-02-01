#!/opt/csw/bin/python2.6

import os
import os.path
import shutil
import unittest
import tempfile
import subprocess
import copy
import sys

I_SCRIPT_PATH = "../files/CSWcswclassutils.i.cswmigrateconf"
SHELL = "/bin/sh"

CONFIG_1 = """MIGRATE_FILES="file0 dir0"
SOURCE_DIR___default__="%(srcdir)s"
DEST_DIR___default__="%(dstdir)s"
ARCH_DIR___default__="%(arcdir)s"
"""

class CswmigrateconfUnitTest(unittest.TestCase):
  """Tests cswmigrateconf."""

  def setUp(self):
    self.tmpdir = tempfile.mkdtemp(prefix="csw-classutils-test-")
    self.script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), I_SCRIPT_PATH)
    print self.tmpdir
    print self.script_path
    self.mig_src_dir = os.path.join(self.tmpdir, "src_etc")
    self.mig_dst_dir = os.path.join(self.tmpdir, "dst_etc")
    self.mig_arc_dir = os.path.join(self.tmpdir, "migration-archive")
    os.mkdir(self.mig_src_dir)
    os.mkdir(self.mig_dst_dir)
    # os.mkdir(self.mig_arc_dir)
    config_content = CONFIG_1 % {
        "srcdir": self.mig_src_dir,
        "dstdir": self.mig_dst_dir,
        "arcdir": self.mig_arc_dir,
    }
    self.migraconf_conf_src_path = os.path.join(self.tmpdir, "cswmigrateconf_src")
    self.migraconf_conf_dst_path = os.path.join(self.tmpdir, "cswmigrateconf_dest")
    self.stdin_data = """%s %s\n""" % (self.migraconf_conf_src_path,
                                       self.migraconf_conf_dst_path)
    f = open(self.migraconf_conf_src_path, "w")
    f.write(config_content)
    f.close()
    f = open(os.path.join(self.mig_src_dir, "file0"), "w")
    f.write("# Test config file.\n")
    f.close()
    os.mkdir(os.path.join(self.mig_src_dir, "dir0"))
    f = open(os.path.join(self.mig_src_dir, "dir0", "file1"), "w")
    f.write("# Second test config file.\n")
    f.close()

  def tearDown(self):
    shutil.rmtree(self.tmpdir)
  
  def test_2(self):
    """Running the thing.

After the migration:

/tmp/csw-classutils-test-8ghrVo
|-- cswmigrateconf_dest
|-- cswmigrateconf_src
|-- dst_etc
|   |-- dir0
|   |   `-- file1
|   `-- file0
|-- migration-archive
|   |-- dir0
|   |   `-- file1
|   `-- file0
`-- src_etc
    |-- dir0.README.migration
    `-- file0.README.migration

5 directories, 8 files
    """
    # srcpath
    # dstpath
    # config content
    subprocess.call(["tree", self.tmpdir])
    print "trying to run it."
    classutils_env = copy.copy(os.environ)
    classutils_env["CLASSUTILS_DEBUG"] = "1"
    args = [SHELL, self.script_path]
    migconf_proc = subprocess.Popen(args,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    cwd="/",
                                    env=classutils_env)
    print "feeding:", repr(self.stdin_data)
    stdout, stderr = migconf_proc.communicate(self.stdin_data)
    retcode = migconf_proc.wait()
    print "stdout", repr(stdout)
    print "stderr", repr(stderr)
    print stdout
    print os.listdir(self.tmpdir)
    subprocess.call(["tree", self.tmpdir])
    self.assertFalse(retcode, "Running %s has failed" % args)

if __name__ == '__main__':
	unittest.main()
