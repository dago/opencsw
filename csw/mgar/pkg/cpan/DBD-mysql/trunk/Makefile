NAME = DBD-mysql
VERSION = 4.024
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CAPTTOFU

DESCRIPTION = MySQL driver for the Perl5 Database Interface (DBI)
define BLURB
  DBD::mysql is the Perl5 Database Interface driver for the MySQL database. In
  other words: DBD::mysql is an interface between the Perl programming
  language and the MySQL programming API that comes with the MySQL relational
  database management system. Most functions provided by this programming API
  are supported. Some rarely used functions are missing, mainly because noone
  ever requested them.
endef

CATALOGNAME = pm_dbdmysql
PACKAGES    = CSWpmdbdmysql

# ARCHALL_CSWpmdbdmysql = 1

LICENSE = README

BUILD_DEP_PKGS += CSWmysql-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWpm-dbi

RUNTIME_DEP_PKGS += CSWlibmysqlclient18
RUNTIME_DEP_PKGS += CSWlibz1
RUNTIME_DEP_PKGS += CSWlibssl1-0-0
RUNTIME_DEP_PKGS += CSWpm-dbi

CONFIGURE_ARGS += --ssl
CONFIGURE_ARGS += --testuser=root
CONFIGURE_ARGS += --mysql_config=$(prefix)/bin/mysql_config
#EXTRA_LIB = $(prefix)/mysql5/lib/mysql

include gar/category.mk
