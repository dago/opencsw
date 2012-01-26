NAME = libspectre
VERSION = 0.2.6
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A small library for rendering Postscript documents
define BLURB
endef

MASTER_SITES = http://libspectre.freedesktop.org/releases/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://libspectre.freedesktop.org

DEP_PKGS = CSWgs

PACKAGES += CSWlibspectre1
PKGFILES_CSWlibspectre1 += $(call pkgfiles_lib,libspectre.so.1)
SPKG_DESC_CSWlibspectre1 += A small library for rendering Postscript documents, libspectre.so.1
RUNTIME_DEP_PKGS_CSWlibspectre += CSWlibspectre1
OBSOLETED_BY_CSWlibspectre1 = CSWlibspectre
CATALOGNAME_CSWlibspectre = libspectre_stub

PACKAGES += CSWlibspectre-dev
SPKG_DESC_CSWlibspectre-dev = Development files for libspectre.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibspectre-dev = CSWlibspectre1

# Disable for now as libgs is missing 64 bit
#BUILD64_LIBS_ONLY = 1

include gar/category.mk
