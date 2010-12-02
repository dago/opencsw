import socket
import os
import sqlobject
import models as m

DB_SCHEMA_VERSION = 5L


class DatabaseClient(object):

  CHECKPKG_DIR = ".checkpkg"
  SQLITE3_DBNAME_TMPL = "checkpkg-db-%(fqdn)s"
  TABLES_THAT_NEED_UPDATES = (m.CswFile,)
  TABLES = TABLES_THAT_NEED_UPDATES + (
            m.Pkginst,
            m.CswConfig,
            m.Srv4FileStats,
            m.CheckpkgOverride,
            m.CheckpkgErrorTag,
            m.Architecture,
            m.OsRelease,
            m.Maintainer)
  sqo_conn = None
  db_path = None

  def __init__(self, debug=False):
    self.debug = debug

  @classmethod
  def GetDatabasePath(cls):
    if not cls.db_path:
      dbname_dict = {'fqdn': socket.getfqdn()}
      db_filename = cls.SQLITE3_DBNAME_TMPL % dbname_dict
      home_dir = os.environ["HOME"]
      cls.db_path = os.path.join(home_dir, cls.CHECKPKG_DIR, db_filename)
    return cls.db_path

  @classmethod
  def InitializeSqlobject(cls):
    """Establishes a database connection and stores it as a class member.

    The idea is to share the database connection between instances.  It would
    be solved even better if the connection was passed to the class
    constructor.
    """
    if not cls.sqo_conn:
      db_path = cls.GetDatabasePath()
      cls.sqo_conn = sqlobject.connectionForURI('sqlite:%s' % db_path)
      sqlobject.sqlhub.processConnection = cls.sqo_conn

  def CreateTables(self):
    for table in self.TABLES:
      table.createTable(ifNotExists=True)

  def IsDatabaseGoodSchema(self):
    good_version = self.GetDatabaseSchemaVersion() >= DB_SCHEMA_VERSION
    return good_version
