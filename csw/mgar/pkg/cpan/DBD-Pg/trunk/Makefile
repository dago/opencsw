GARNAME = DBD-Pg
GARVERSION = 2.16.1
CATEGORIES = cpan
AUTHOR = TURNSTEP

DESCRIPTION = PostgreSQL database driver for the DBI module
define BLURB
  DBD::Pg is a Perl module which works with the DBI module to provide access
  to PostgreSQL databases.
endef

PACKAGES = CSWpmdbdpg
CATALOGNAME = pm_dbdpg

PG_HOME = /opt/csw/postgresql
RUNTIME_DEP_PKGS = CSWlibpq
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

LICENSE = README

# we need to override pg_config, because the RPATH is missing
PERL_CONFIGURE_ARGS += LIBS="-L$(PG_HOME)/lib -R$(PG_HOME)/lib -lpq"

include gar/category.mk

# set postgres home
CONFIGURE_ENV += POSTGRES_HOME=$(PG_HOME)
