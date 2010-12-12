NAME = libexif
VERSION = 0.6.19
CATEGORIES = lib

DESCRIPTION = EXIF Tag Parsing Library
define BLURB
  libexif is a library for parsing, editing, and saving EXIF data. It is
	intended to replace lots of redundant implementations in command-line
	utilities and programs with GUIs.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

SPKG_SOURCEURL = http://libexif.sourceforge.net

PACKAGES = CSWlibexif CSWlibexifdevel CSWlibexifdoc
CATALOGNAME_CSWlibexif = libexif
CATALOGNAME_CSWlibexifdevel = libexif_devel
CATALOGNAME_CSWlibexifdoc = libexif_doc
SPKG_DESC_CSWlibexif = $(DESCRIPTION)
SPKG_DESC_CSWlibexifdevel = $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibexifdoc = $(DESCRIPTION) - API documentation package

PKGFILES_CSWlibexifdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibexifdoc = $(sharedstatedir)/doc/libexif/libexif-api.html/.*

RUNTIME_DEP_PKGS_CSWlibexif += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibexifdevel += CSWlibexif
RUNTIME_DEP_PKGS_CSWlibexifdoc += CSWlibexif

ARCHALL_CSWlibexifdoc = 1

LICENSE = COPYING

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=12272
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# Compatibility for Solaris find/tar
PATCHFILES = Makefile.patch
# 
PATCHFILES += exif-tag.patch

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-docs

include gar/category.mk
