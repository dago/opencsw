GARNAME = pyorbit
GARVERSION = 2.24.0
CATEGORIES = lang

DESCRIPTION = ORBit2 CORBA support for Python
define BLURB
  This is a Python language binding for the ORBit2 CORBA implementation.
endef

MASTER_SITES = http://freshmeat.net/projects/pyorbit/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += fixme.sh

PACKAGES = CSWpyorbit
REQUIRED_PKGS_CSWpyorbit  = CSWpython CSWggettextrt CSWglib2
REQUIRED_PKGS_CSWpyorbit += CSWlibidl CSWorbit2

CATALOGNAME_CSWpyorbit = py_orbit
SPKG_DESC_CSWpyorbit = ORBit2 CORBA support for Python

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

## No tests
TEST_SCRIPTS = 

include gar/category.mk

post-configure-$(MODULATION):
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)
