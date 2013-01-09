import sqlobject
import database

class SqlObjectTestMixin(object):

  def setUp(self):
    super(SqlObjectTestMixin, self).setUp()
    self.dbc = database.CatalogDatabase(uri="sqlite:/:memory:")
    self.dbc.CreateTables()

  def tearDown(self):
    super(SqlObjectTestMixin, self).tearDown()
    del self.dbc
    sqlobject.sqlhub.processConnection.close()
    sqlobject.sqlhub.processConnection = None
    # SQLObject caches URIs
    # We need to clean the URI cache.
    # Otherwise the in-memory database will persist.
    # http://www.mail-archive.com/sqlobject-discuss@lists.sourceforge.net/msg00416.html
    sqlobject.dbconnection.TheURIOpener.cachedURIs={}


