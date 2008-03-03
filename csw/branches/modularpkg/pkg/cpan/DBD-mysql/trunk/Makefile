GARNAME = DBD-mysql
GARVERSION = 4.003
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

DISTFILES += CSWpmdbdmysql.gspec CSWpmdbdmysql.depend

DEPENDS += server/mysql4

# Module version numbers defeat Sort::Versions
MANUAL_UPDATE = 1

CONFIGURE_ARGS = --ssl

# Tests require MySQL to be running
TEST_SCRIPTS =

include gar/category.mk
