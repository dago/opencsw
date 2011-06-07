# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libwebp
VERSION = 0.1.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = An image format that does lossy compression of digital photographic images
define BLURB
endef

GOOGLE_PROJECT = webp
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWlibwebp-dev
SPKG_DESC_CSWlibwebp-dev = Development files for libwebp.so.0
PKGFILES_CSWlibwebp-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibwebp-dev += CSWlibwebp0

PACKAGES += CSWlibwebp0
SPKG_DESC_CSWlibwebp0 = Library for the WebP lossy photographic image format, libwebp.so.0
PKGFILES_CSWlibwebp0 = $(call pkgfiles_lib,libwebp.so.0)

PACKAGES += CSWwebp
SPKG_DESC_CSWwebp = An image format that does lossy compression of digital photographic images
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWwebp += CSWlibwebp0
RUNTIME_DEP_PKGS_CSWwebp += CSWpng
RUNTIME_DEP_PKGS_CSWwebp += CSWjpeg

BUILD64 = 1

# On amd64 -xO3 results in an assembler error
OPT_FLAGS_SOS-amd64 = -xO2
OPT_FLAGS_SOS = $(or $(OPT_FLAGS_SOS-$(ISA)),-xO3)

include gar/category.mk

post-extract-modulated:
	@# This tarball has not been boostrapped
	-cd $(WORKSRC) && ./autogen.sh
	@$(MAKECOOKIE)
