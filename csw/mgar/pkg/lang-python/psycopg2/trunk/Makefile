# $Id$
NAME = psycopg2
VERSION = 2.4.5
CATEGORIES = python
GARTYPE = v2

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

BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWpostgresql-dev
RUNTIME_DEP_PKGS_CSWpy-psycopg2 += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-psycopg2 += CSWlibpq5

MASTER_SITES = http://www.psycopg.org/psycopg/tarballs/PSYCOPG-2-4/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
