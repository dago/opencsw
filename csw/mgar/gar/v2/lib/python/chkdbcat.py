#!/opt/csw/bin/python2.6
"""Check catalog data stored in the database for consistency.

Check catalog data stored in the database for consistency using Peter
Bonivart's chkcat.

Notifications for invalid catalogs can be customized by overriding
CheckDBCat.notify().
"""
from email.mime.text import MIMEText
import cjson
import datetime
import dateutil.parser
import logging
import os
import os.path
import shutil
import smtplib
import subprocess
import sys
import tempfile

from lib.python import configuration
from lib.python.shell import ShellCommand
from lib.python.rest import RestClient, GetUsernameAndPassword

class FSLock(object):
      """Simple Lock class

      Provide a simple locking mechanism using a directory as lock.

      """
      def __init__(self, dirname):
            self.__dirname = dirname

      def __enter__(self):
            """Create lock directory."""
            logging.debug("Create lock dir: %s", self.__dirname)
            os.mkdir(self.__dirname)
            return self

      def __exit__(self, t, v, tb):
            """Remove lock directory."""
            logging.debug("Remove lock dir: %s", self.__dirname)
            os.rmdir(self.__dirname)


class GenerateCatalog(object):
      """Dumping a database catalog to disk in a format digestable for chkcat.

      Replacement for lib.python.generate_catalog_file

      """

      def __init__(self, catrel,
                   arch,
                   osrel,
                   catgenbin):
            self._catrel = catrel
            self._arch = arch
            self._osrel = osrel
            self._catgenbin = catgenbin

      def generate_catalog(self, catalogdir):
            """Generate the catalog and place it to :param catalogdir:"""
            logging.debug("Generate catalog %s %s %s using %s/catalog", self._catrel,
                         self._osrel,
                         self._arch,
                         self._catgenbin)

            (retval,
             wdc1,
             wdc2) = ShellCommand([self._catgenbin,
                                   "-arch", self._arch,
                                   "-catalog-release", self._catrel,
                                   "-os-release", self._osrel,
                                   "-output", os.path.join(catalogdir, "catalog")])

class TimestampRecord(object):
      """Record Timestamp for a given Catalog, Architecture, and OS Release into a json encoded file."""
      def __init__(self, fn):
            """Constructor.

            "fn is" the filename to read from and write to. File will be
            created if necessary and is not required to exist prior
            instantiation of class.

            """
            self.__filename = fn
            if os.path.exists(self.__filename):
                  self.__read_data()
            else:
                  self.__ts_by_catalog={}

      def __enter__(self):
            """Dummy."""
            return self

      def __exit__(self, exc_type, wdc1, wdc2):
            """Save data to file."""
            if exc_type is None:
                  logging.debug("Save TimestampRecord to file")
                  self.save()

      def __read_data(self):
            """Read json data into memory.

            Read json data from file and create a dictionary with
            (catrel,arch,osrel) as key and string representation of
            timestamp as value.

            Dictionary is stored in self.__ts_by_catalog

            """
            with open(self.__filename, "r") as fp:
                  keyval_list = cjson.decode(fp.read())
                  ts_by_ctlg = dict((tuple(x), y) for x, y in keyval_list)
                  self.__ts_by_catalog = ts_by_ctlg

      def save(self):
            """Save in memory data to file.

            Save self.__ts_by_catalog json encoded to file. If self.__ts_by_catalog is
            empty, nothing will be done.

            """
            # We don't create an empty json file in order to prevent
            # reading from an empty json file upon instanciation with
            # the same file name
            if not self.__ts_by_catalog: return

            with open(self.__filename, "w") as fp:
                  fp.write(cjson.encode(self.__ts_by_catalog.items()))

      def get(self, catrel, arch, osrel):
            """Get time stamp for given catrel, arch, and osrel.

            Time stamp will be returned as datetime. None will be
            returned if no time stamp has been recorded for catalog
            triple.

            """
            catkey = (catrel, arch, osrel)
            if self.__ts_by_catalog.has_key(catkey):
                  return dateutil.parser.parse(self.__ts_by_catalog[catkey])
            else:
                  return None

      def set(self, catrel, arch, osrel, date):
            """Set time stamp for a given catrel, arch, and osrel.

            If date is an instance of datetime, the value obtained by
            calling isoformat() will be stored.

            If date is an instance of str, it has to be a date in iso format.

            """
            assert date is not None

            catkey = (catrel, arch, osrel)
            if isinstance(date, datetime.datetime):
                  self.__ts_by_catalog[catkey] = date.replace(microsecond=0).isoformat()
            elif isinstance(date, str):
                  # try to convert string into datetime, so that we
                  # know it has proper format.
                  self.__ts_by_catalog[catkey] = dateutil.parser.parse(date).isoformat()
            else:
                  raise TypeError("Expected instance of str or datetime, got %s" % str(type(date)))


class CatalogTiming(object):
      """Fetch Catalog Timing information.

      Fetch Catalog Timing information, such as when packages have
      been built and uploaded.

      """
      _epoch_start = datetime.datetime(datetime.MINYEAR,1,1,0,0,0,0)

      # Mapping of key name to list index with optional transformation.
      # Used by __list_to_dict_generator()
      __list_to_dict_translation = (
            ('pkg', 0),
            ('version', 1),
            ('spkg', 2),
            ('fullname', 3),
            ('md5', 4),
            ('built', 10,
             lambda x: CatalogTiming._epoch_start if x is None else dateutil.parser.parse(x)),
            ('upload', 11,
             lambda x: CatalogTiming._epoch_start if x is None else dateutil.parser.parse(x)),
            ('uploadby', 12)
      )

      def __init__(self, catrel, arch, osrel):
            self.__catrel = catrel
            self.__arch = arch
            self.__osrel = osrel
            self.__timing_data = self.__json_list_to_dict(self.fetch())

      def __list_to_dict_generator(self, l):
            """Generate tuples suitable to create a dictionary.

            It uses the tuples t in self.__list_to_dict_translation to
            extract the value at position t[1] in l using t[0] as key name.

            If len(t)==3, it assumes t[2] is callable and calls t[2]
            with the value at position t[1] in l as argument.

            """
            for tr in self.__list_to_dict_translation:
                  if len(tr) == 2:
                        yield (tr[0], l[tr[1]])
                  elif len(tr) == 3:
                        yield (tr[0], tr[2](l[tr[1]]))

      def __json_list_to_dict(self, jdat):
            """Translate json encoded timing data to a list of dictionaries.

            Returns a list of dicts decoded from json input.

            Json input "jdat" is expect to have the form:

            [
             [
              "libz1",
              "1.2.8,REV=2013.09.17",
              "CSWlibz1",
              "libz1-1.2.8,REV=2013.09.17-SunOS5.10-sparc-CSW.pkg.gz",
              "7684a5d3a096900f89f78c3c2dda3ff3",
              197630,
              [...],
              [...],
              "libz1 - Zlib data compression library, libz.so.1",
              125,
              "2013-09-17T07:13:30",
              "2013-09-17T10:36:15",
              "raos"
             ],
             . . .
            ]

            Output is a list of dictionaries:

            [
             { "pkg": "libz1",
               "version": "1.2.8,REV=2013.09.17",
               "spkg": "CSWlibz1",
               "fullname": "libz1-1.2.8,REV=2013.09.17-SunOS5.10-sparc-CSW.pkg.gz",
               "md5": "7684a5d3a096900f89f78c3c2dda3ff3",
               "built": "2013-09-17T07:13:30",
               "upload": "2013-09-17T10:36:15",
               "uploadby": "raos"
              },
              . . .
            ]

            """
            return [dict(self.__list_to_dict_generator(v)) for v in jdat]

      def fetch(self):
            """Fetch timing information using REST."""
            return self.rest_client.GetCatalogTimingInformation(
                self.__catrel, self.__arch, self.__osrel)

      def upload_newer_than(self, date):
            """Retrieve timing information on upload newer than "date"."""
            self.__timing_data.sort(key=lambda x: x['upload'])

            # now, find the first item having a `upload date'=>`date'
            # in __timing_data and splice the list starting at that
            # index up to the end. Since the list has been sorted in
            # descending order, this gives all `upload date'=>`date'
            index=0
            for f in self.__timing_data:
                  if f['upload']>=date:
                        break
                  index+=1

            return self.__timing_data[index:]


class CheckDBCatalog(object):
      """Check a catalog retrieved from the database.

      It retrieves a catalog from the database according to the
      tripple (catrel,arch,osrel) and runs `chkcat' on the catalog. If
      `chkcat' reports no errors, a time stamp will be written into a
      file marking the last successful check.

      If `chkcat' finds errors, the last successful time stamp will be
      used to find all newly uploaded packages since this last
      successful check, using "CatalogTiming" class. In that case, the
      time stamp will NOT be updated.

      Each new catalog to be checked is required to pass the check
      initially, since no last successful time stamp is available.

      The class has to be used in a `with' statement, since the
      temporary directory required is created by __enter__() and
      removed by __exit__().

      """
      def __init__(self, catrel, arch, osrel, fn_ts, gen_catalog_bin,
                   chkcat="/opt/csw/bin/chkcat",
                   cattiming_class=CatalogTiming,
                   tsrecord_class=TimestampRecord):
            """Constructor.

            "fn_ts" is the path name to the time stamp file.

            "gen_catalog_bin" is the path to the gen-catalog-index binary

            "chkcat" is the path to `chkcat'. By default
            `/opt/csw/bin/chkcat'.

            "cattiming_class" and "tsrecord_class" are mainly used for
            unit tests in order to provide classes with overridden
            methods.

            """
            config = configuration.GetConfig()
            username, password = GetUsernameAndPassword()
            self.rest_client = RestClient(
                pkgdb_url=config.get('rest', 'pkgdb'),
                releases_url=config.get('rest', 'releases'),
                username=username,
                password=password)

            self.__catalogfgen = GenerateCatalog(catrel, arch, osrel,
                                                 gen_catalog_bin)
            self.__chkcat = chkcat

            # store for later use
            self._catrel = catrel
            self._arch = arch
            self._osrel = osrel

            # will be set by __enter__ and unset by __exit__
            self.tmpdir = None

            self.__tsrecord_class = tsrecord_class
            self.__cattiming_class = cattiming_class
            self.__timestamp_record = tsrecord_class(fn_ts)

      def __enter__(self):
            assert self.tmpdir is None
            self.tmpdir=tempfile.mkdtemp(dir='/var/tmp')
            logging.debug("Created temp dir %s" % self.tmpdir)
            return self

      def __exit__(self, wdc1, wdc2, wdc3):
            """Cleanup temporary directory where catalog has been stored."""
            assert self.tmpdir is not None
            logging.debug("Remove tmp directory %s" % (self.tmpdir,))
            shutil.rmtree(self.tmpdir)
            self.tmpdir = None

      def __get_notification_address(self, pkginfo):
            """Returns the address where the notification will be sent to.

            Find the email address according to package information "pkginfo""

            """
            # In case 'uploadby' is non-conclusive, fall back to
            # retrieve email address of maintainer.
            if pkginfo['uploadby'] is not None and pkginfo['uploadby'] != "web":
                  return pkginfo['uploadby']+'@opencsw.org'
            else:
                  return self.rest_client.GetMaintainerByMd5(
                      pkginfo['md5'])['maintainer_email']

      def notify(self, date, addr, pkginfo):
            """Notification.

            Will be called for each "addr" once. "pkginfo" is a list
            with packages as retrieved by 'CatalogTiming' since last
            successful check.

            """
            logging.info("TO: %s" % addr)
            [logging.info("packge %s uploaded since %s might have caused catalog break" % (p['fullname'],str(date))) for p in pkginfo]

      def fetch_db_cat(self):
            """Fetch catalog stored in database into temporary direcotry."""
            assert self.tmpdir is not None
            self.__catalogfgen.generate_catalog(self.tmpdir)

      def run_chkcat(self):
            """Run `chkcat' on catalog retrieved into temporary directory."""
            assert self.tmpdir is not None

            logging.debug("Run chkcat on %s" % os.path.join(self.tmpdir, "catalog"))
            (self.__chkcat_retval,
             self.stdout,
             self.stderr) = ShellCommand([self.__chkcat,
                                          "-p",
                                          os.path.join(self.tmpdir, "catalog")],
                                         allow_error=True)
            # see `/opt/csw/bin/chkcat -h' for details on the return code
            return self.__chkcat_retval in (0,1)

      def check(self):
            """Download the catalog and use chkcat on it.

            In case the catalog is invalid, a list of packages by
            `uploader' will be composed and notify() called for each
            uploader.

            Returns True upon successful check, False otherwise.
            """
            retval = False
            with FSLock('/tmp/CheckDBCat.lock'):
                  self.fetch_db_cat()
                  retval = self.run_chkcat()

                  # Only record successful checks.
                  if retval:
                        with self.__timestamp_record:
                              self.__timestamp_record.set(self._catrel,
                                                          self._arch,
                                                          self._osrel,
                                                          datetime.datetime.now())

                  # Compose list of packages uploaded since last successful
                  # check by `uploader'.
                  notifications = {}
                  if not retval:
                        lastsuccessful = self.__timestamp_record.get(
                              self._catrel,
                              self._arch,
                              self._osrel)

                        if lastsuccessful is None:
                              logging.warn("No successful catalog check recorded for %s,%s,%s" %
                                           (self._catrel, self._arch, self._osrel))
                              return retval;

                        newpkgs = self.__cattiming_class(self._catrel,
                                                         self._arch,
                                                         self._osrel).upload_newer_than(lastsuccessful)

                        # compose notifications list in a manner so that
                        # each email address is notified exactly once, even
                        # when several packages are affected.
                        notifications = {}
                        for np in newpkgs:
                              addr=self.__get_notification_address(np)
                              notifications.setdefault(addr,{ 'lastsuccessful': lastsuccessful })
                              notifications[addr].setdefault('newpkgs', []).append(np)

                        for n in notifications:
                              self.notify(notifications[n]['lastsuccessful'], n, notifications[n]['newpkgs'], self.stdout, self.stderr)

            return retval


class InformMaintainer(object):
      MAIL_CAT_BROKEN_HEADER = u"""Hi

You uploaded following packages

"""

      MAIL_CAT_BROKEN_FOOTER = u"""
which may (or may not) have broken the catalog for

 %s %s %s

since the last successful check on %s.

Please check the package(s) and re-upload if necessary.

Here is the output from chkcat:

%s

%s

Your Check Database Catalog script

"""

      def __init__(self, cat_tuple, date, addr, pkginfo, chkcat_stdout, chkcat_stderr):
            self._cat_tuple = cat_tuple
            self._date = date
            self._addr = addr
            self._pkginfo = pkginfo
            self._chkcat_stdout = chkcat_stdout
            self._chkcat_stderr = chkcat_stderr

      def _compose_mail(self, from_address):
            """Compose Mail"""

            msg = InformMaintainer.MAIL_CAT_BROKEN_HEADER
            for p in self._pkginfo:
                  msg = msg + p['fullname'] + "\n"
            msg = msg + InformMaintainer.MAIL_CAT_BROKEN_FOOTER

            mail = MIMEText(msg % (self._cat_tuple +
                                   (str(self._date), self._chkcat_stdout, self._chkcat_stderr)))
            mail['From'] = from_address
            mail['To'] = self._addr
            mail['Subject'] = "[chkdbcat] Database Catalog broken by recent upload"

            return mail

      def send_mail(self):
            from_address = "Check Database Catalog <noreply@opencsw.org>"
            s = smtplib.SMTP('mail.opencsw.org')
            try:
                  s.sendmail(from_address, [self._addr],
                             self._compose_mail(from_address).as_string())
                  logging.debug("E-mail sending finished.")
            except smtplib.SMTPRecipientsRefused, e:
                  logging.error(
                        "Sending email to %s failed, recipient refused.",
                        repr(self._addr))
            
