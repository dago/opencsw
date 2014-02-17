import database
import logging
import sqlobject

from lib.python import representations

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


class PackageStatsMixin(object):

  def PrepareElfinfo(self, pkg_data):
    for binary_md5 in pkg_data['elfdump_info']:
      d = pkg_data['elfdump_info'][binary_md5]
      syminfo_list = []
      for syminfo_as_list in d['symbol table']:
        if isinstance(syminfo_as_list, dict):
          del syminfo_as_list['type']
          symbol = representations.ElfSymInfo(**syminfo_as_list)
        else:
          symbol = representations.ElfSymInfo._make(syminfo_as_list)
        syminfo_list.append(symbol)
      d['symbol table'] = syminfo_list
    def PkgMapify(as_list):
      return representations.PkgmapEntry._make(as_list)
    new_pkgmap = [PkgMapify(x) for x in pkg_data['pkgmap']]
    pkg_data['pkgmap'] = new_pkgmap
