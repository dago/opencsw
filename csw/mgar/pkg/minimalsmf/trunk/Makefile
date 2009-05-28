GARNAME = minimalsmf
GARVERSION = 0.2
CATEGORIES = server

DESCRIPTION = A test of an SMF-enabled package and mGAR SMF support
define BLURB
  This package is a minimal build of a package with SMF support, for the
  purposes of testing and documenting mGAR.

  It should contain the least amount of code necessary to build a package,
  which, upon installation, imports a manifest and starts the service in the
  global zone as well as in the non-global zones (full and sparse).

  References:
    - https://apps.sourceforge.net/trac/gar/wiki/cswclassutils
- http://wiki.opencsw.org/cswclassutils-package
endef

ARCHALL = 1
MASTER_SITES =
DISTFILES  = sleeping-beauty
DISTFILES += csw$(GARNAME)

REQUIRED_PKGS = CSWcswclassutils
SPKG_CLASSES = none cswinitsmf

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswminimalsmf$$$$/ { $$$$2 = "cswinitsmf" } { print }'

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(GARNAME)

install-$(GARNAME):
	ginstall -d $(DESTDIR)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 files/sleeping-beauty $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/csw$(GARNAME) \
		$(DESTDIR)/etc/opt/csw/init.d/csw$(GARNAME)

include gar/category.mk
