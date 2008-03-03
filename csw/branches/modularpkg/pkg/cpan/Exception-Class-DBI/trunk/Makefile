GARNAME = Exception-Class-DBI
GARVERSION = 0.95
CATEGORIES = cpan
AUTHOR = DWHEELER

DESCRIPTION = DBI exception objects
define BLURB
  This module offers a set of DBI-specific exception classes. They inherit
  from Exception::Class, the base class for all exception objects created by
  the Exception::Class module from the CPAN. Exception::Class::DBI itself
  offers a single class method, handler(), that returns a code reference
  appropriate for passing to the DBI HandleError attribute.
endef

DISTFILES += CSWpmexceptclsdbi.gspec CSWpmexceptclsdbi.depend

DEPENDS += cpan/Exception-Class cpan/Module-Build

include gar/category.mk
