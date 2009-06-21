GARNAME = DBD-mysql
GARVERSION = 4.012
CATEGORIES = cpan
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
PACKAGES	= CSWpmdbdmysql

ARCHALL_CSWpmdbdmysql = 1

LICENSE = README

PKGS_REQUIRED_CSWpmdbdmysql = CSWmysql4

CONFIGURE_ARGS += --ssl

include gar/category.mk
