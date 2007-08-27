GARNAME = DBD-SQLite
GARVERSION = 1.13
CATEGORIES = cpan
AUTHOR = MSERGEANT

DESCRIPTION = self contained RDBMS in a DBI driver
define BLURB
  SQLite is a public domain RDBMS database engine that you can find at
  http://www.hwaci.com/sw/sqlite/.
endef

DISTFILES += CSWpmdbdsqlite.gspec

# Use Perl's Config{optimize} instead of -O6
PATCHFILES = optimize.diff

include ../category.mk
