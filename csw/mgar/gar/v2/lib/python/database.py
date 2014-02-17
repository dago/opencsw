import socket
import os
import sqlobject
import logging
import ConfigParser
import time

from lib.python import common_constants
from lib.python import configuration
from lib.python import models as m

CONFIG_DB_SCHEMA = "db_schema_version"
DB_SCHEMA_VERSION = 13L

# This list of tables is sensitive to the order in which tables are created.
# After you change the order here, you need to make sure that the tables can
# still be created.
TABLES = (m.Architecture,
          m.CatalogRelease,
          m.CswConfig,
          m.Host,
          m.Maintainer,
          m.OsRelease,
          m.Pkginst,
          m.ElfdumpInfoBlob,
          m.Srv4FileStatsBlob,
          m.CatalogGenData,
          m.Srv4FileStats,
          m.CheckpkgErrorTag,
          m.CswFile,
          m.CheckpkgOverride, # needs Srv4FileStats
          m.Srv4DependsOn,
          m.Srv4IncompatibleWith,
          m.Srv4FileInCatalog,
)
# Shouldn't this be in common_constants?
SYSTEM_PKGMAP = "/var/sadm/install/contents"
CONFIG_MTIME = "mtime"


class Error(Exception):
  """A generic error."""


class DatabaseError(Error):
  """A problem with the database."""


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
      try:
        logging.debug("Creating table %r", table)
        table.createTable(ifNotExists=True)
      except sqlobject.dberrors.OperationalError, e:
        logging.error("Could not create table %r: %s", table, e)
        raise


  def InitialDataImport(self):
    """Imports initial data into the db.

    Assumes that tables are already created.

    Populates initial:
      - architectures
      - OS releases
      - catalog releases
    """
    # We need the 'all' architecture as well.
    for arch in common_constants.ARCHITECTURES:
      try:
        m.Architecture(name=arch)
      except sqlobject.dberrors.DuplicateEntryError:
        pass
    for osrel in common_constants.OS_RELS:
      try:
        m.OsRelease(short_name=osrel, full_name=osrel)
      except sqlobject.dberrors.DuplicateEntryError:
        pass
    for relname in common_constants.DEFAULT_CATALOG_RELEASES:
      try:
        m.CatalogRelease(name=relname)
      except sqlobject.dberrors.DuplicateEntryError:
        pass
    self.SetDatabaseSchemaVersion()

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


def InitDB(config):
  db_uri = configuration.ComposeDatabaseUri(config)
  dbc = CatalogDatabase(uri=db_uri)
  dbc.CreateTables()
  dbc.InitialDataImport()
