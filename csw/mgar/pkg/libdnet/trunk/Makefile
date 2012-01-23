# $Id$
NAME = libdnet
VERSION = 1.12
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A simplified, portable interface to several low-level networking routines
define BLURB
endef

VENDOR_URL = http://code.google.com/p/libdnet/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES  = 0001-Using-the-m4-subdirectory-for-macros.patch
PATCHFILES += 0002-Moved-acinclude.m4-to-the-m4-directory.patch

PACKAGES = CSWlibdnet1
CATALOGNAME_CSWlibdnet1 = libdnet1
PKGFILES_CSWlibdnet1 += $(call baseisadirs,$(libdir),libdnet\.so\.1\.0\.1)
PKGFILES_CSWlibdnet1 += $(call baseisadirs,$(libdir),libdnet\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibdnet1 += A simplified, portable interface to several low-level networking routines, libdnet.so.1
RUNTIME_DEP_PKGS_CSWlibdnet += CSWlibdnet1

PACKAGES += CSWlibdnet-dev
SPKG_DESC_CSWlibdnet-dev += $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWlibdnet-dev += CSWlibdnet1

OBSOLETED_BY_CSWlibdnet-dev = CSWlibdnet
OBSOLETED_BY_CSWlibdnet1 = CSWlibdnet

include gar/category.mk

# Not sure whether it's the minimal number of steps, or whether they are in
# a correct order, but it gets the job done.
#
# Workaround based on:
#   http://www.v7w.com/debian/libtool-missing_so.html
#   http://www.v7w.com/debian/libtool-updating.html
#
# Additionally, removing the old aclocal.m4 seems to be necessary.
pre-configure-modulated:
	rm $(WORKSRC)/aclocal.m4
	(cd $(WORKSRC) && libtoolize --copy --force)
	(cd $(WORKSRC) && aclocal)
	(cd $(WORKSRC) && autoreconf -fi)
	@$(MAKECOOKIE)
