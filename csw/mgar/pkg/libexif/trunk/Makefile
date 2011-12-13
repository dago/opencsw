NAME = libexif
VERSION = 0.6.20
CATEGORIES = lib

DESCRIPTION = EXIF Tag Parsing Library
define BLURB
  libexif is a library for parsing, editing, and saving EXIF data. It is
	intended to replace lots of redundant implementations in command-line
	utilities and programs with GUIs.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# Compatibility for Solaris find/tar
PATCHFILES = Makefile.patch
PATCHFILES += exif-tag.patch

VENDOR_URL = http://libexif.sourceforge.net

PACKAGES += CSWlibexif12
SPKG_DESC_CSWlibexif12 = EXIF tag parsing library, libexif.so.12
PKGFILES_CSWlibexif12 += $(call pkgfiles_lib,libexif.so.12)
PKGFILES_CSWlibexif12 += $(sharedstatedir)/locale/.*/libexif-12\.mo
RUNTIME_DEP_PKGS_CSWlibexif12 += CSWlibintl8
OBSOLETED_BY_CSWlibexif12 += CSWlibexif

PACKAGES += CSWlibexif-dev
SPKG_DESC_CSWlibexif-dev = Development files for libexif.so.12
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibexif-dev += CSWlibexif12

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-docs

include gar/category.mk
