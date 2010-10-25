# $Id$
GARNAME = psycopg2
GARVERSION = 2.2.2
CATEGORIES = python

DESCRIPTION = Psycopg2 is a PostgreSQL adapter for Python
define BLURB
  Psycopg is the most used PostgreSQL adapter for the Python
  programming language. At the core it fully implements the Python DB
  API 2.0 specifications. Several extensions allow access to many of
  the features offered by PostgreSQL.
endef

PACKAGES = CSWpy-psycopg2
CATALOGNAME = py_psycopg2
LICENSE = LICENSE

BUILD_DEP_PKGS = CSWpython-devel
RUNTIME_DEP_PKGS_CSWpy-psycopg2 = SUNWpostgr-libs
RUNTIME_DEP_PKGS_CSWpy-psycopg2 += CSWlibpython2-6-1-0

MASTER_SITES = http://initd.org/psycopg/tarballs/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
