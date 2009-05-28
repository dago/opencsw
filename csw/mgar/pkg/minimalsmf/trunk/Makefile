GARNAME = minimalsmf
GARVERSION = 0.1
CATEGORIES = server

DESCRIPTION = A test of an SMF-enabled package and mGAR SMF support
define BLURB
  This package is a minimal build of a package with SMF support, for the
  purposes of testing and documenting mGAR.

  It should contain the least amount of code necessary to build a package,
  which, upon installation, imports a manifest and starts the service in the
  global zone as well as in the non-global zones (full and sparse).
endef

ARCHALL = 1
MASTER_SITES =
DISTFILES  = sleeping-beauty
DISTFILES += $(call admfiles,CSW$(GARNAME),)
DISTFILES += csw$(GARNAME) csw$(GARNAME).xml svc-csw$(GARNAME)

INITSMF = /opt/csw/etc/init.d/csw$(GARNAME)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(GARNAME)

install-$(GARNAME):
	ginstall -d $(DESTDIR)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 files/sleeping-beauty $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(libdir)/svc/method
	ginstall -m 755 files/svc-csw$(GARNAME) $(DESTDIR)$(libdir)/svc/method/csw$(GARNAME)

include gar/category.mk
