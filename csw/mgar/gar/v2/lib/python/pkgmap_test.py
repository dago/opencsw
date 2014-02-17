#!/usr/bin/env python2.6

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest


from lib.python import pkgmap
from lib.python import representations

PKGMAP_1 = """1 f cswcpsampleconf /etc/opt/csw/cups/cupsd.conf.CSW 0644 root bin 4053 20987 1264420689
"""

PKGMAP_2 = """: 1 18128
1 d none /etc/opt/csw/cups 0755 root bin
1 f cswcpsampleconf /etc/opt/csw/cups/cupsd.conf.CSW 0644 root bin 4053 20987 1264420689
1 f none /etc/opt/csw/cups/cupsd.conf.default 0640 root bin 4053 20987 1264420689
1 d none /etc/opt/csw/cups/interfaces 0755 root bin
1 d none /etc/opt/csw/cups/ppd 0755 root bin
1 f cswinitsmf /etc/opt/csw/init.d/cswcups 0555 root bin 4547 14118 1264420798
1 i depend 122 11155 1264524848
1 i pkginfo 489 41685 1264524852
1 i postremove 151 12419 1256302505
1 i preinstall 1488 45678 125630250
"""

PKGMAP_3 = """1 d none /opt/csw/apache2/ap2mod 0755 root bin
1 e build /opt/csw/apache2/ap2mod/suexec ? ? ? 1472 50478 1289099700
1 d none /opt/csw/apache2/libexec 0755 root bin
1 f none /opt/csw/apache2/libexec/mod_suexec.so 0755 root bin 6852 52597 1289092061
1 p none /etc/scn/scn_aa_read 0600 root sys
"""

class PkgmapUnitTest(unittest.TestCase):

  def test_1(self):
    pm = pkgmap.Pkgmap(PKGMAP_1.splitlines())
    entry = representations.PkgmapEntry(
            cksum=None,
            class_='cswcpsampleconf',
            group='bin',
            line=('1 f cswcpsampleconf /etc/opt/csw/cups/cupsd.conf.CSW '
                  '0644 root bin 4053 20987 1264420689'),
            major=None,
            minor=None,
            mode='0644',
            modtime=None,
            owner='root',
            path='/etc/opt/csw/cups/cupsd.conf.CSW',
            pkgnames=[],
            size=None,
            target=None,
            type_='f',
    )
    self.assertEqual(1, len(pm.entries))
    self.assertEqual(entry, pm.entries[0])

  def test_2(self):
    pm = pkgmap.Pkgmap(PKGMAP_2.splitlines())
    line = ': 1 18128'
    self.assertTrue(line in pm.entries_by_line)

  def test_3(self):
    pm = pkgmap.Pkgmap(PKGMAP_2.splitlines())
    self.assertTrue('cswcpsampleconf' in pm.entries_by_class)

  def test_4(self):
    pm = pkgmap.Pkgmap(PKGMAP_3.splitlines())
    self.assertTrue('build' in pm.entries_by_class)

  def testPkgmapSortedByPaths(self):
    pm = pkgmap.Pkgmap(PKGMAP_2.splitlines())
    paths = [x.path for x in pm.entries]
    self.assertEquals(paths, sorted(paths))

  def test_ParseLineSymlink(self):
    pm = pkgmap.Pkgmap(PKGMAP_2.splitlines())
    line = ('1 s none '
            '/opt/csw/lib/postgresql/9.0/lib/sparcv9/libpq.so.5=libpq.so.5.3')
    # s none /opt/csw/lib/sparcv9/libpq.so.5=..//sparcv9/libpq.so.5
    # s none /opt/csw/lib/sparcv9/libpq.so.5.3=..//sparcv9/libpq.so.5.3
    line_to_add = ('/opt/csw/lib/postgresql/9.0/lib/sparcv9/libpq.so.5 --> '
                   'libpq.so.5.3')
    entry = representations.PkgmapEntry(
        cksum=None,
        class_='none',
        group=None,
        line=('1 s none /opt/csw/lib/postgresql/9.0/lib/sparcv9/'
              'libpq.so.5=libpq.so.5.3'),
        major=None,
        minor=None,
        mode=None,
        modtime=None,
        owner=None,
        path='/opt/csw/lib/postgresql/9.0/lib/sparcv9/libpq.so.5',
        pkgnames=[],
        size=None,
        target='/opt/csw/lib/postgresql/9.0/lib/sparcv9/libpq.so.5.3',
        type_='s',
    )
    self.assertEqual((entry, line_to_add), pm._ParseLine(line))


if __name__ == '__main__':
  unittest.main()
