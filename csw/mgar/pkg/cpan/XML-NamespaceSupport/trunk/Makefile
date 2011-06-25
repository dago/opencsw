NAME = XML-NamespaceSupport
VERSION = 1.11
CATEGORIES = cpan
AUTHOR = PERIGRIN

DESCRIPTION = Simple generic namespace support class
define BLURB
  This module offers a simple to process namespaced XML names (unames) from
  within any application that may need them. It also helps maintain a prefix
  to namespace URI map, and provides a number of basic checks.
endef

DISTFILES = COPYING

PACKAGES = CSWpmxmlnssupp
CATALOGNAME = pm_xmlnssupp

PERL_CONFIGURE_ARGS = --skip

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpmxmlnssupp += catalogname-does-not-match-pkgname|pkgname=CSWpmxmlnssupp|catalogname=pm_xmlnssupp|expected-catalogname=pmxmlnssupp

include gar/category.mk
