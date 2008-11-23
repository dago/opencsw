GARNAME = DBD-mysql
GARVERSION = 3.0006
CATEGORIES = cpan
AUTHOR = CAPTTOFU

DESCRIPTION = MySQL 5 DBI Driver.
define BLURB
  DBD::mysql is the Perl5 Database Interface driver for the MySQL database. In
  other words: DBD::mysql is an interface between the Perl programming
  language and the MySQL programming API that comes with the MySQL relational
  database management system. Most functions provided by this programming API
  are supported. Some rarely used functions are missing, mainly because noone
  ever requested them.
endef

DISTFILES += $(call admfiles,CSWpmdbdmysql5,depend prototype)

DEPENDS += server/mysql5

# Module version numbers defeat Sort::Versions
MANUAL_UPDATE = 1

myroot = $(prefix)/mysql5
mylib = $(myroot)/lib/mysql
mybin = $(myroot)/bin
mycfg = $(mybin)/mysql_config

CONFIGURE_ARGS  = --mysql_config=$(mycfg)
CONFIGURE_ARGS += --libs="-R$(mylib) $(shell $(mycfg) --libs)"
CONFIGURE_ARGS += --ssl

# Tests require MySQL to be running
TEST_SCRIPTS =

include gar/category.mk

