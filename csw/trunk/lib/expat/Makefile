GARNAME = expat
GARVERSION = 1.95.6
CATEGORIES = lib

SPKG_PKGNAME = CSWexpat
SPKG_BITNAME = expat

DESCRIPTION = XML Parser Toolkit
define BLURB
  Expat is a fast, non-validating, stream-oriented XML parsing library.
endef

MASTER_SITES = http://unc.dl.sourceforge.net/sourceforge/expat/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# The expat 'check' target tries to compile tests that use GCC
# constructs -- won't compile under Forte without hackery.
TEST_TARGET = check
ENABLE_TEST = 0

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir libdir includedir mandir 

include ../category.mk
