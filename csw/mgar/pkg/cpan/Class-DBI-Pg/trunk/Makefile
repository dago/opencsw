NAME = Class-DBI-Pg
VERSION = 0.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = IKEBE

DESCRIPTION = Class::DBI extension for Postgres
define BLURB
  Class::DBI::Pg automate the setup of Class::DBI columns and primary key for
  Postgres.
endef

DISTFILES += CSWpmclassdbipg.gspec CSWpmclassdbipg.depend

DEPENDS += cpan/Class-DBI cpan/DBD-Pg

include gar/category.mk

# This test requires Pg to be installed
pre-test:
	@rm -f $(WORKSRC)/t/01_table.t
