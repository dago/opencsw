GARNAME = DBD-AnyData
GARVERSION = 0.08
CATEGORIES = cpan
AUTHOR = JZUCKER

DESCRIPTION = DBI access to XML, CSV and other formats
define BLURB
  The DBD::AnyData module provides a DBI/SQL interface to data in many formats
  and from many sources.

  Currently supported formats include general format flatfiles (CSV, Fixed
  Length, Tab or Pipe "delimited", etc.), specific formats (passwd files, web
  logs, etc.), a variety of other kinds of formats (XML, Mp3, HTML tables),
  and, for some operations, any DBI accessible database. The number of
  supported formats will continue to grow rapidly since there is an open API
  making it easy for any author to create additional format parsers which can
  be plugged in to AnyData.
endef

DISTFILES += CSWpmdbdanydata.gspec CSWpmdbdanydata.depend

DEPENDS += cpan/SQL-Statement cpan/DBD-File cpan/AnyData cpan/DBI

include gar/category.mk
