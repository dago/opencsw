NAME = xerces-c
VERSION = 3.0.1
CATEGORIES = lib

DESCRIPTION = Xerces XML parser for C++
define BLURB
  Xerces-C++ is a validating XML parser written in a portable subset
  of C++. Xerces-C++ makes it easy to give your application the ability
  to read and write XML data. A shared library is provided for parsing,
  generating, manipulating, and validating XML documents using the DOM,
  SAX, and SAX2 APIs. For an introduction to programming with Xerces-C++
 refer to the Programming Guide.
endef

MASTER_SITES = http://apache.abdaal.com/xerces/c/3/sources/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWxerces-c
CATALOGNAME = xerces_c

SPKG_SOURCEURL = http://xerces.apache.org/xerces-c/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
