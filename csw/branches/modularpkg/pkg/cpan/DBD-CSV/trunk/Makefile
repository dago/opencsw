GARNAME = DBD-CSV
GARVERSION = 0.22
CATEGORIES = cpan
AUTHOR = JZUCKER

DESCRIPTION = DBI driver for CSV files
define BLURB
  The DBD::CSV module is yet another driver for the DBI (Database independent
  interface for Perl). This one is based on the SQL "engine" SQL::Statement
  and the abstract DBI driver DBD::File and implements access to so-called CSV
  files (Comma separated values). Such files are mostly used for exporting MS
  Access and MS Excel data.
endef

DISTFILES += CSWpmdbdcsv.gspec CSWpmdbdcsv.depend

DEPENDS += cpan/DBI cpan/SQL-Statement cpan/Text-CSV_XS

include gar/category.mk
