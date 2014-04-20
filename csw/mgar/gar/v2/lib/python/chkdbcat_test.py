#!/opt/csw/bin/python2.6

"""Tests for chkdbcat.py."""

import os
import cjson
import datetime
import logging
import unittest
from lib.python.chkdbcat import TimestampRecord, CatalogTiming, CheckDBCatalog, InformMaintainer

##
## Unit tests
##
class TCatalogTiming(CatalogTiming):
      """Override fetch() for CatalogTiming.

      Class overrides fetch() for use in tests.

      """
      def fetch(self):
            """Provide static data for unit test."""
            return cjson.decode("""[
    [
        "libz1",
        "1.2.8,REV=2013.09.17",
        "CSWlibz1",
        "libz1-1.2.8,REV=2013.09.17-SunOS5.10-sparc-CSW.pkg.gz",
        "7684a5d3a096900f89f78c3c2dda3ff3",
        197630,
        [],
        [],
        "libz1 - Zlib data compression library, libz.so.1",
        125,
        "2013-09-17T07:13:30",
        "2013-09-17T10:36:15",
        "raos"
    ],
   [
        "zlib_stub",
        "1.2.8,REV=2013.09.17",
        "CSWzlib",
        "zlib_stub-1.2.8,REV=2013.09.17-SunOS5.10-all-CSW.pkg.gz",
        "93f73a862bf07339badd723cf11eb0ca",
        1857,
        [],
        [],
        "zlib_stub - Transitional package. Content moved to CSWlibz1",
        125,
        "2013-09-17T07:16:39",
        "2013-09-17T10:36:28",
        "raos"
    ],
        [
        "389_admin",
        "1.1.30,REV=2013.01.07",
        "CSW389-admin",
        "389_admin-1.1.30,REV=2013.01.07-SunOS5.10-sparc-CSW.pkg.gz",
        "f7d9c15d13118a3d837849d581339a65",
        396732,
        [],
        [],
        "389_admin - The 389 LDAP server Admin Tools",
        126,
        "2013-01-07T11:53:26",
        null,
        null
    ],
    [
        "zsh",
        "5.0.1,REV=2012.12.21",
        "CSWzsh",
        "zsh-5.0.1,REV=2012.12.21-SunOS5.10-sparc-CSW.pkg.gz",
        "78420c21d8772b3ce72518ad91c82813",
        2176170,
        [],
        [],
        "zsh - Powerful UNIX shell",
        98,
        "2012-12-21T00:25:14",
        null,
        null
    ],
    [
        "zutils",
        "1.0,REV=2013.07.05",
        "CSWzutils",
        "zutils-1.0,REV=2013.07.05-SunOS5.10-sparc-CSW.pkg.gz",
        "82c42dd606530aebc230d813f324c3e5",
        161930,
        [],
        [],
        "zutils - Utilities to deal with compressed and non-compressed files",
        3,
        "2013-07-05T11:28:42",
        "2013-07-05T13:31:57",
        "dam"
    ]
]
""")


class TestTimestampRecord(unittest.TestCase):
      def setUp(self):
            self.__tmpfile = "/tmp/TestTimestampRecord"
            self.__now = datetime.datetime.now().replace(microsecond=0)
            self.__fixture = [
                  [ [(a,b,c) for a in ('unstable', 'kiel', 'testing')]
                  for b in ('i386', 'sparc') ]
                  for c in ('SunOS5.10', 'SunOS5.11')]

      def test_LastSuccessfulCheck_str(self):
            """Single pass test writing and retrieving data from a file using string date."""
            try:
                  os.unlink(self.__tmpfile)
            except:
                  pass

            # With statement used to make sure data is saved to disk
            with TimestampRecord(self.__tmpfile) as obj:
                  obj.set('unstable', 'sparc', 'SunOS5.10', self.__now.isoformat())

            obj = TimestampRecord(self.__tmpfile)
            self.assertEqual(self.__now.isoformat(), obj.get('unstable', 'sparc', 'SunOS5.10').isoformat())

      def test_Many_str(self):
            """Multiple pass test writing and retrieving data from a file using string date."""
            try:
                  os.unlink(self.__tmpfile)
            except:
                  pass

            with TimestampRecord(self.__tmpfile) as obj:
                  [[[obj.set(c[0], c[1], c[2], self.__now.isoformat()) for c in b] for b in a] for a in self.__fixture]

            obj = TimestampRecord(self.__tmpfile)
            [[[self.assertEqual(self.__now.isoformat(),obj.get(c[0], c[1], c[2]).isoformat()) for c in b] for b in a] for a in self.__fixture]

      def test_LastSuccessfulCheck_obj(self):
            """Single pass test writing and retrieving data from a file using datetime object."""
            try:
                  os.unlink(self.__tmpfile)
            except:
                  pass

            with TimestampRecord(self.__tmpfile) as obj:
                  obj.set('unstable', 'sparc', 'SunOS5.10', self.__now)

            obj = TimestampRecord(self.__tmpfile)
            self.assertEqual(self.__now.isoformat(), obj.get('unstable', 'sparc', 'SunOS5.10').isoformat())

      def test_Many_obj(self):
            """Multiple pass test writing and retrieving data from a file using datetime obj."""
            try:
                  os.unlink(self.__tmpfile)
            except:
                  pass

            with TimestampRecord(self.__tmpfile) as obj:
                  [[[obj.set(c[0], c[1], c[2], self.__now) for c in b] for b in a] for a in self.__fixture]

            obj = TimestampRecord(self.__tmpfile)
            [[[self.assertEqual(self.__now.isoformat(),obj.get(c[0], c[1], c[2]).isoformat()) for c in b] for b in a] for a in self.__fixture]

      def test_SetInvalidType(self):
            """Test set() with invalid type."""

            with TimestampRecord(self.__tmpfile) as obj:
                  self.assertRaises(ValueError,obj.set,'unstable','i386','SunOS5.11',"abcd")

            with TimestampRecord(self.__tmpfile) as obj:
                  self.assertRaises(TypeError,obj.set,'unstable', 'i386', 'SunOS5.11', 1)

      def test_Notified(self):
            with TimestampRecord(self.__tmpfile) as obj:
                  obj.set('unstable', 'i386', 'SunOS5.10',
                          datetime.datetime.now().replace(microsecond=0))
                  obj.notified('unstable', 'i386', 'SunOS5.10',
                               'raos@opencsw.org')
                  obj.notified('unstable', 'i386', 'SunOS5.10',
                               'somebodyelse@opencsw.org')

                  obj.set('unstable', 'sparc', 'SunOS5.10',
                          datetime.datetime.now().replace(microsecond=0))
                  obj.notified('unstable', 'sparc', 'SunOS5.10',
                               '1@opencsw.org')
                  obj.notified('unstable', 'sparc', 'SunOS5.10',
                               '2@opencsw.org')

                  self.assertTrue(obj.is_notified('unstable', 'i386',
                                                  'SunOS5.10',
                                                  'raos@opencsw.org'))
                  self.assertTrue(obj.is_notified('unstable', 'i386',
                                                  'SunOS5.10',
                                                  'somebodyelse@opencsw.org'))
                  self.assertTrue(obj.is_notified('unstable', 'sparc',
                                                  'SunOS5.10',
                                                  '1@opencsw.org'))
                  self.assertTrue(obj.is_notified('unstable', 'sparc',
                                                  'SunOS5.10',
                                                  '2@opencsw.org'))

            with TimestampRecord(self.__tmpfile) as obj:
                  self.assertTrue(obj.is_notified('unstable', 'i386',
                                                  'SunOS5.10',
                                                  'raos@opencsw.org'))
                  self.assertTrue(obj.is_notified('unstable', 'i386',
                                                  'SunOS5.10',
                                                  'somebodyelse@opencsw.org'))
                  self.assertTrue(obj.is_notified('unstable', 'sparc',
                                                  'SunOS5.10',
                                                  '1@opencsw.org'))
                  self.assertTrue(obj.is_notified('unstable', 'sparc',
                                                  'SunOS5.10',
                                                  '2@opencsw.org'))

      def tearDown(self):
            try:
                  #os.unlink(self.__tmpfile)
                  pass
            except:
                  pass


class TestCatalogTiming(unittest.TestCase):
      def test_Newer1(self):
            obj = TCatalogTiming('unstable', 'sparc', 'SunOS5.10')
            self.assertEqual(
                  len(obj.upload_newer_than(datetime.datetime(datetime.MINYEAR,1,1,0,0,0,0))),
                  5
            )

      def test_Newer2(self):
            obj = TCatalogTiming('unstable', 'sparc', 'SunOS5.10')
            self.assertEqual(
                  len(obj.upload_newer_than(datetime.datetime(2013,9,1,0,0,0,0))),
                  2
            )

      def test_Newer3(self):
            obj = TCatalogTiming('unstable', 'sparc', 'SunOS5.10')
            self.assertEqual(
                  len(obj.upload_newer_than(datetime.datetime(2040,1,1,0,0,0,0))),
                  0
            )


class TestCheckDBCatalog(unittest.TestCase):
      class TCheckDBCatalogInvalid(CheckDBCatalog):
            """Generate an invalid catalog."""
            def fetch_db_cat(self):
                  logging.debug('Create catalog %s' %
                                os.path.join(self.tmpdir,'catalog'))
                  with open(os.path.join(self.tmpdir,'catalog'), 'w') as fp:
                        # The catalog is invalid because several dependencies are missing
                        fp.write("""zsh 5.0.1,REV=2012.12.21 CSWzsh zsh-5.0.1,REV=2012.12.21-SunOS5.10-sparc-CSW.pkg.gz 78420c21d8772b3ce72518ad91c82813 2176170 CSWcommon|CSWlibiconv2|CSWlibncursesw5|CSWlibpcre1|CSWlibgdbm4 none none
zutils 1.0,REV=2013.07.05 CSWzutils zutils-1.0,REV=2013.07.05-SunOS5.10-sparc-CSW.pkg.gz 82c42dd606530aebc230d813f324c3e5 161930 CSWcas-texinfo|CSWcommon|CSWisaexec|CSWlzip none none""")


      class TCheckDBCatalogValid(CheckDBCatalog):
            def fetch_db_cat(self):
                  """Generate a valid catalog"""
                  logging.debug('Create catalog %s' %
                                os.path.join(self.tmpdir,'catalog'))
                  with open(os.path.join(self.tmpdir,'catalog'), 'w') as fp:
                        fp.write("""common 1.5,REV=2010.12.11 CSWcommon common-1.5,REV=2010.12.11-SunOS5.8-sparc-CSW.pkg f83ab71194e67e04d1eee5d8db094011 23040 none none none
                  zsh 5.0.1,REV=2012.12.21 CSWzsh zsh-5.0.1,REV=2012.12.21-SunOS5.10-sparc-CSW.pkg.gz 78420c21d8772b3ce72518ad91c82813 2176170 CSWcommon none none
                  zutils 1.0,REV=2013.07.05 CSWzutils zutils-1.0,REV=2013.07.05-SunOS5.10-sparc-CSW.pkg.gz 82c42dd606530aebc230d813f324c3e5 161930 CSWcommon none none""")


      class TCheckDBCatalogNotification(TCheckDBCatalogInvalid):
            expected_notification_on = {
                  'dam@opencsw.org': {
                        'lastsuccessful': datetime.datetime(2013,5,17,0,0,0),
                        'newpkgs': [
                              'zutils-1.0,REV=2013.07.05-SunOS5.10-sparc-CSW.pkg.gz'
                        ]
                  },
                  'raos@opencsw.org': {
                        'lastsuccessful': datetime.datetime(2013,5,17,0,0,0),
                        'newpkgs': [
                              'libz1-1.2.8,REV=2013.09.17-SunOS5.10-sparc-CSW.pkg.gz',
                              'zlib_stub-1.2.8,REV=2013.09.17-SunOS5.10-all-CSW.pkg.gz'
                        ]
                  }
            }

            def notify_broken(self, date, addr, pkginfo, chkcat_stdout, chkcat_stderr):
                  assert date == self.expected_notification_on[addr]['lastsuccessful']

                  if addr == "raos@opencsw.org":
                        assert len(pkginfo) == 2
                  elif addr == "dam@opencsw.org":
                        assert len(pkginfo) == 1
                  else:
                        raise Exception("Unexpected address")

                  for p in pkginfo:
                        assert p['fullname'] in self.expected_notification_on[addr]['newpkgs']

                  mail = InformMaintainer((self._catrel, self._osrel, self._arch),
                                          date, addr, pkginfo, chkcat_stdout, chkcat_stderr)
                  print mail._compose_mail_broken('TestScript')


      def setUp(self):
            self.__timestamp_file = '/tmp/TestCheckDBCatalog.ts'

      def test_InvalidCatalog(self):
            """Test a locally generated invalid catalog"""

            with self.TCheckDBCatalogInvalid('unstable', 'sparc',
                                             'SunOS5.10',
                                             self.__timestamp_file,
                                             'go/bin/gen-catalog-index',
                                             cattiming_class=TCatalogTiming) as test:
                  self.assertFalse(test.check())

      def test_ValidCatalog(self):
            """Test a locally generated valid catalog"""
            with self.TCheckDBCatalogValid('unstable', 'sparc',
                                           'SunOS5.10',
                                           self.__timestamp_file,
                                           'go/bin/gen-catalog-index',
                                           cattiming_class=TCatalogTiming) as test:
                  self.assertFalse(test.check())

      def test_Notification(self):
            """Test notification for invalid catalog."""
            # Create last successful test time stamp for catalog to be tested
            with TimestampRecord(self.__timestamp_file) as tsobj:
                  tsobj.set('unstable','sparc','SunOS5.10',datetime.datetime(2013,5,17,0,0,0))

            with self.TCheckDBCatalogNotification('unstable', 'sparc',
                                                  'SunOS5.10',
                                                  self.__timestamp_file,
                                                  'go/bin/gen-catalog-index',
                                                  cattiming_class=TCatalogTiming) as test:
                  self.assertFalse(test.check())

      def tearDown(self):
            try:
                  os.unlink(self.__timestamp_file)
            except:
                  pass


if __name__ == '__main__':
      logging.basicConfig(level=logging.INFO)
      unittest.main()
