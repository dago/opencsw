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

CONFIGURE_ARGS  = --mysql_config=$(prefix)/mysql5/bin/mysql_config
CONFIGURE_ARGS += --ssl

# Tests require MySQL to be running
ENABLE_TEST = 0

include ../category.mk
