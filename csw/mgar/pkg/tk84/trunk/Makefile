NAME = tk
VERSION = 8.4.15
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = GUI toolkit for tcl
define BLECTURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTFILES += 8.4.i386.tar.xz
DISTFILES += 8.4.sparc.tar.xz
DISTFILES += license.terms

NOEXTRACT += 8.4.i386.tar.xz
NOEXTRACT += 8.4.sparc.tar.xz

# Tk in general is only rebuilt on Solaris 10, to avoid collisions we must also only do Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

PACKAGES += CSWlibtk8-4
SPKG_DESC_CSWlibtk8-4 = GUI toolkit library for tcl, libtk8.4.so
# PKGFILES is catchall

# This is correct, the soname with *.so is really the one to use
CHECKPKG_OVERRIDES_CSWlibtk8-4 += soname-equals-filename

# These are legacy files, just leave them for now
CHECKPKG_OVERRIDES_CSWlibtk8-4 += file-with-bad-content|/usr/local|root/opt/csw/lib/tk8.4/demos/tcolor
CHECKPKG_OVERRIDES_CSWlibtk8-4 += file-with-bad-content|/usr/local|root/opt/csw/lib/tk8.4/demos/README
CHECKPKG_OVERRIDES_CSWlibtk8-4 += file-with-bad-content|/export/medusa|root/opt/csw/lib/libtk8.4.so

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)
	xz -c -d $(FILEDIR)/8.4.$(GARCH).tar.xz | (cd $(DESTD