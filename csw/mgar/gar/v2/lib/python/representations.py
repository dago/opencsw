import collections

# Full catalog entry, enough to write a line of a catalog file.
CatalogEntry = collections.namedtuple(
    'CatalogEntry', 'catalogname version pkgname basename '
                    'md5_sum size deps category i_deps desc')
