GARNAME = Class-DBI-mysql
GARVERSION = 1.00
CATEGORIES = cpan
AUTHOR = TMTM

DESCRIPTION = extensions to Class::DBI for MySQL
define BLURB
  This is an extension to Class::DBI, containing several functions and
  optimisations for the MySQL database. Instead of setting Class::DBI as your
  base class, use this instead.
endef

DISTFILES += CSWpmclassdbimysql.gspec CSWpmclassdbimysql.depend

DEPENDS += cpan/DBD-mysql cpan/Class-DBI

# Tests require MySQL to be running
TEST_SCRIPTS =

include gar/category.mk

