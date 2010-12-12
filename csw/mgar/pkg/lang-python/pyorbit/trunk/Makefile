NAME = pyorbit
VERSION = 2.24.0
CATEGORIES = lang
RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9].*\)\.[0-9]*/\1/')

DESCRIPTION = ORBit2 CORBA support for Python
define BLURB
  This is a Python language binding for the ORBit2 CORBA implementation.
endef

MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/pyorbit/$(RELVER)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
STRIP_LIBTOOL = 1

PACKAGES = CSWpyorbit
RUNTIME_DEP_PKGS_CSWpyorbit  = CSWpython CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWpyorbit += CSWlibidl CSWorbit2

CATALOGNAME_CSWpyorbit = pyorbit
SPKG_SOURCEURL_CSWpyorbit = http://freshmeat.net/projects/pyorbit/
SPKG_DESC_CSWpyorbit = ORBit2 CORBA support for Python

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.bz2

## No tests
TEST_SCRIPTS = 

include gar/category.mk

