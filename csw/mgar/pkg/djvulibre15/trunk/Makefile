NAME = djvulibre
VERSION = 3.5.20.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = DjVu standalone viewer, browser plug-in, command line tools
define BLECTURB
endef

SF_PROJ = djvu
MASTER_SITES = $(SF_MIRRORS)/DjVuLibre/$(VERSION)/
DISTFILES += libdjvulibre.so.15.sparc
DISTFILES += libdjvulibre.so.15.i386

VENDOR_URL = http://djvu.sourceforge.net/

PACKAGES += CSWlibdjvulibre15
SPKG_DESC_CSWlibdjvulibre15 += DjVu library, libdjvulibre.so.15
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibdjvulibre15 += CSWlibjpeg62
RUNTIME_DEP_PKGS_CSWlibdjvulibre15 += CSWlibiconv2

# This is a legacy lib, keep old errors until this expires out
CHECKPKG_OVERRIDES_CSWlibdjvulibre15 += license-missing|/opt/csw/share/doc/libdjvulibre15/license
CHECKPKG_OVERRIDES_CSWlibdjvulibre15 += bad-rpath-entry|/lib|opt/csw/lib/libdjvulibre.so.15.5.0
CHECKPKG_OVERRIDES_CSWlibdjvulibre15 += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/lib/libdjvulibre.so.15.5.0
CHECKPKG_OVERRIDES_CSWlibdjvulibre15 += bad-rpath-entry|/opt/SUNWspro/lib/rw7|opt/csw/lib/libdjvulibre.so.15.5.0
CHECKPKG_OVERRIDES_CSWlibdjvulibre15 += bad-rpath-entry|/opt/SUNWspro/lib/v8|opt/csw/lib/libdjvulibre.so.15.5.0

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall $(WORKDIR)/libdjvulibre.so.15.$(GARCH) $(DESTDIR)$(libdir)/libdjvulibre.so.15.5.0
	gln -s libdjvulibre.so.15.5.0 $(DESTDIR)$(libdir)/libdjvulibre.so.1