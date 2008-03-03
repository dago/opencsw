GARNAME = Ima-DBI
GARVERSION = 0.34
CATEGORIES = cpan
AUTHOR = TMTM

DESCRIPTION = database connection caching and organization
define BLURB
  Ima::DBI attempts to organize and facilitate caching and more efficient use
  of database connections and statement handles by storing DBI and SQL
  information with your class (instead of as separate objects). This allows
  you to pass around just one object without worrying about a trail of DBI
  handles behind it.
endef

DISTFILES += CSWpmimadbi.gspec CSWpmimadbi.depend

DEPENDS += cpan/Class-WhiteHole cpan/Class-Data-Inheritable
DEPENDS += cpan/DBIx-ContextualFetch

include gar/category.mk
