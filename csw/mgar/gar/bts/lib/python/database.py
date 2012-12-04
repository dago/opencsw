import socket
import os
import sqlobject
import models as m
import logging
import common_constants
import configuration
import ConfigParser
import time
import system_pkgmap

CONFIG_DB_SCHEMA = "db_schema_version"
DB_SCHEMA_VERSION = 7L
TABLES_THAT_NEED_UPDATES = (m.CswFile,)
TABLES = TABLES_THAT_NEED_UPDATES + (
            m.Architecture,
            m.CatalogRelease,
            m.CatalogReleaseType,
            m.CheckpkgErrorTag,
            m.CheckpkgOverride,
            m.CswConfig,
            m.Host,
            m.Maintainer,
            m.OsRelease,
            m.Pkginst,
            m.Srv4DependsOn,
            m.Srv4FileInCatalog,
            m.Srv4FileStats,
            m.Srv4FileStatsBlob)
# Shouldn't this be in common_constants?
SYSTEM_PKGMAP = "/var/sadm/install/contents"
CONFIG_MTIME = "mtime"


class Error(Exception):
  pass


class DeprecatedError(Error):
  pass


class DatabaseError(Error):
  "A problem with the database."


class DatabaseManager(object):
  """Responsible for verifying that the database is set up correctly."""

  def __init__(self):
    self.config = None

  def AutoManage(self):
    self.config = configuration.GetConfig()
    try:
      auto_manage_option = self.config.get("database", "auto_manage")
      logging.debug("auto_manage_option = %s", auto_manage_option)
      auto_manage = (auto_manage_option in ("yes", "true"))
      # We only automanage sqlite.
      if self.config.get("database", "type") != "sqlite":
        auto_manage = False
      logging.debug("auto_manage: %s", auto_manage)
      self._CheckAndMaybeFixSchema(auto_fix=auto_manage)
      self._CheckAndMaybeFixFreshness(auto_fix=auto_manage)
    except ConfigParser.NoOptionError, e:
      logging.critical("No 'auto_manage' option in the configuration. "
                       "Please review the configuration file.")
      raise DatabaseError(e)

  def _CheckAndMaybeFixSchema(self, auto_fix):
    ldm = LocalDatabaseManager()
    logging.debug("Database schema version: %s, application expects: %s",
                  ldm.GetDatabaseSchemaVersion(),
                  DB_SCHEMA_VERSION)
    if not ldm.IsDatabaseGoodSchema():
      if auto_fix:
        logging.warning("Old database schema detected.")
        logging.warning("Dropping and creating all tables.")
        ldm.PurgeDatabase(drop_tables=True)
        ldm.CreateTables()
        ldm.InitialDataImport()
        ldm.SetDatabaseSchemaVersion()
      else:
        msg = (
            "Database schema does not match the application. "
            "Database contains: %s, "
            "the application expects: %s. "
            % (ldm.GetDatabaseSchemaVersion(), DB_SCHEMA_VERSION))
        if DB_SCHEMA_VERSION < ldm.GetDatabaseSchemaVersion():
          msg += "Make sure your application sources are up to date."
        elif DB_SCHEMA_VERSION > ldm.GetDatabaseSchemaVersion():
          msg += ("Make sure your database is up to date.  "
                  "Re-create it if necessary.")
        raise DatabaseError(msg)

  def _CheckAndMaybeFixFreshness(self, auto_fix):
    ldm = LocalDatabaseManager()
    if not ldm.IsDatabaseUpToDate():
      if auto_fix:
        logging.warning(
            "Cache database is not up to date.  "
            "Refreshing it.")
        ldm.ClearTablesForUpdates()
        ldm.RefreshDatabase()
        ldm.SetDatabaseMtime()
      else:
        # Not doing anything. The user could want it that way.
        # We don't even print a warning, because in a non-managed setup
        # checkpkg should not care about this.
        pass

  def VerifyContents(self, sqo_osrel, sqo_arch):
    "Verify that we know the system files on the OS release and architecture."
    res = m.Srv4FileStats.select(
        sqlobject.AND(
          m.Srv4FileStats.q.use_to_generate_catalogs==False,
          m.Srv4FileStats.q.registered==True,
          m.Srv4FileStats.q.os_rel==sqo_osrel,
          m.Srv4FileStats.q.arch==sqo_arch))
    # logging.warning("VerifyContents(): Packages Count: %s", res.count())
    system_pkgs = res.count()
    logging.debug("VerifyContents(%s, %s): %s", sqo_osrel, sqo_arch, system_pkgs)
    if system_pkgs < 10:
      raise DatabaseError(
          "Checkpkg can't find system files for %s %s in the cache database.  "
          "These are files such as /usr/lib/libc.so.1.  "
          "Private DB setup: "
          "you can only check packages built for the same Solaris version "
          "you're running on this machine.  "
          "For instance, you can't check a SunOS5.9 package on SunOS5.10. "
          "Shared DB setup (e.g. OpenCSW maintainers): "
          "If you have one home directory on multiple hosts, make sure you "
          "run checkpkg on the host you intended to.  "
          "To fix, go to a %s %s host and execute: pkgdb system-files-to-file; "
          "pkgdb import-system-file install-contents-%s-%s.pickle; "
          "See http://wiki.opencsw.org/checkpkg for more information."
          % (sqo_osrel.short_name, sqo_arch.name,
             sqo_arch.name, sqo_osrel.short_name,
             sqo_osrel.short_name, sqo_arch.name))


class CheckpkgDatabaseMixin(object):

  def PurgeDatabase(self, drop_tables=False):
    if drop_tables:
      for table in TABLES:
        if table.tableExists():
          table.dropTable()
    else:
      logging.debug("Truncating all tables")
      for table in TABLES:
        table.clearTable()

  def CreateTables(self):
    for table in TABLES:
      table.createTable(ifNotExists=True)

  def InitialDataImport(self):
    """Imports initial data into the db.

    Assumes that tables are already created.

    Populates initial:
      - architectures
      - OS releases
      - catalog releases
    """
    for arch in common_constants.PHYSICAL_ARCHITECTURES:
      try:
        obj = m.Architecture(name=arch)
      except sqlobject.dberrors.DuplicateEntryError:
        pass
    for osrel in common_constants.OS_RELS:
      try:
        obj = m.OsRelease(short_name=osrel, full_name=osrel)
      except sqlobject.dberrors.DuplicateEntryError:
        pass
    for reltype in common_constants.DEFAULT_CATALOG_RELEASES:
      try:
        sqo_reltype = m.CatalogReleaseType(name=reltype)
        obj = m.CatalogRelease(name=reltype, type=sqo_reltype)
      except sqlobject.dberrors.DuplicateEntryError:
        pass
    self.SetDatabaseSchemaVersion()

  def CreateTables(self):
    for table in TABLES:
      table.createTable(ifNotExists=True)

  def ClearTablesForUpdates(self):
    for table in TABLES_THAT_NEED_UPDATES:
      table.clearTable()

  def IsDatabaseGoodSchema(self):
    good_version = self.GetDatabaseSchemaVersion() == DB_SCHEMA_VERSION
    if not good_version:
      logging.fatal("Database schema version: %s, "
                    "Application expects version: %s",
                    self.GetDatabaseSchemaVersion(),
                    DB_SCHEMA_VERSION)
    return good_version

  def GetDatabaseSchemaVersion(self):
    schema_on_disk = 1L
    if not m.CswConfig.tableExists():
      return schema_on_disk;
    res = m.CswConfig.select(m.CswConfig.q.option_key == CONFIG_DB_SCHEMA)
    if res.count() < 1:
      logging.debug("No db schema value found, assuming %s.",
                   schema_on_disk)
    elif res.count() == 1:
      schema_on_disk = res.getOne().int_value
    return schema_on_disk

  def SetDatabaseSchemaVersion(self):
    try:
      config_option = m.CswConfig.select(
          m.CswConfig.q.option_key==CONFIG_DB_SCHEMA).getOne()
      config_option.int_value = DB_SCHEMA_VERSION
    except sqlobject.main.SQLObjectNotFound, e:
      version = m.CswConfig(option_key=CONFIG_DB_SCHEMA,
                            int_value=DB_SCHEMA_VERSION)


class CatalogDatabase(CheckpkgDatabaseMixin):
  """Drives checkpkg-related db operations.

  This separates those operations from the DatabaseClient class, which
  implicitly opens database connections.
  """
  def __init__(self, uri):
    super(CheckpkgDatabaseMixin, self).__init__()
    self.uri = uri
    self.sqo_conn = sqlobject.connectionForURI(self.uri)
    sqlobject.sqlhub.processConnection = self.sqo_conn


class LocalDatabaseManager(CheckpkgDatabaseMixin):
  """Detects if local database is up to date, and re-populates it."""

  def __init__(self):
    self.file_mtime = None
    self.cache_mtime = None

  def SetDatabaseMtime(self):
    mtime = self.GetFileMtime()
    res = m.CswConfig.select(m.CswConfig.q.option_key==CONFIG_MTIME)
    if res.count() == 0:
      logging.debug("Inserting the mtime (%s) into the database.", mtime)
      config_record = m.CswConfig(option_key=CONFIG_MTIME, float_value=mtime)
    else:
      logging.debug("Updating the mtime (%s) in the database.", mtime)
      res.getOne().float_value = mtime

  def GetDatabaseMtime(self):
    if not self.cache_mtime:
      res = m.CswConfig.select(m.CswConfig.q.option_key==CONFIG_MTIME)
      if res.count() == 1:
        self.cache_mtime = res.getOne().float_value
      elif res.count() < 1:
        self.cache_mtime = 1
    logging.debug("GetDatabaseMtime() --> %s", self.cache_mtime)
    return self.cache_mtime

  def GetFileMtime(self):
    if not self.file_mtime:
      try:
        stat_data = os.stat(SYSTEM_PKGMAP)
        self.file_mtime = stat_data.st_mtime
      except OSError, e:
        logging.warning("Could not open %s: %s", SYSTEM_PKGMAP, e)
    return self.file_mtime

  def IsDatabaseUpToDate(self):
    f_mtime_epoch = self.GetFileMtime()
    d_mtime_epoch = self.GetDatabaseMtime()

    # On some systems where pkgdb runs, f_mtime_epoch can be None.  To
    # allow to run pkgdb, the absence of the SYSTEM_PKGMAP file must be
    # tolerated.  The GetDatabaseMtime function returns None if the file
    # is absent.  If f_mtime_epoch cannot be translated into a number,
    # it's set to zero.
    f_mtime = 0
    try:
      f_mtime = time.gmtime(int(f_mtime_epoch))
    except TypeError, e:
      logging.warning("Could not get file mtime: %s", e)
    d_mtime = time.gmtime(int(d_mtime_epoch))
    logging.debug("IsDatabaseUpToDate: f_mtime %s, d_time: %s", f_mtime, d_mtime)
    # Rounding up to integer seconds.  There is a race condition: 
    # pkgadd finishes at 100.1
    # checkpkg reads /var/sadm/install/contents at 100.2
    # new pkgadd runs and finishes at 100.3
    # subsequent checkpkg runs won't pick up the last change.
    # I don't expect pkgadd to run under 1s.
    fresh = f_mtime <= d_mtime
    good_version = self.GetDatabaseSchemaVersion() >= DB_SCHEMA_VERSION
    logging.debug("IsDatabaseUpToDate: good_version=%s, fresh=%s",
                  repr(good_version), repr(fresh))
    return fresh and good_version

  def RefreshDatabase(self):
    # Using the same stuff pkgdb is using.
    logging.warning(
        "Refreshing the database.  It may take a long time, please be patient.")
    logging.warning("If you need a way to make it faster, please see:")
    logging.warning("http://wiki.opencsw.org/checkpkg#toc5")
    infile_contents = common_constants.DEFAULT_INSTALL_CONTENTS_FILE
    infile_pkginfo = None
    logging.debug("Indexing.")
    spi = system_pkgmap.Indexer(None,
                                infile_contents,
                                infile_pkginfo,
                                None,
                                None)
    data = spi.Index(show_progress=True)
    logging.debug("Importing to the database.")
    importer = system_pkgmap.InstallContentsImporter()
    importer.ImportData(
        data, show_progress=True,
        include_prefixes=frozenset(["CSW"]))
