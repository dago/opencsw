# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = aalib
VERSION = 1.4rc5
GARTYPE = v2

DESCRIPTION = Ascii art graphics library

SF_PROJ = aa-project
MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(NAME)-1.4.0
DISTFILES += $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWlibaa1
SPKG_DESC_CSWlibaa1 = Ascii art graphics library, libaa.so.1
PKGFILES_CSWlibaa1 += $(call pkgfiles_lib,libaa.so.1)
OBSOLETED_BY_CSWlibaa1 += CSWaalib

PACKAGES += CSWlibaa-dev
SPKG_DESC_CSWlibaa-dev = Development files for libaa.so.1
PKGFILES_CSWlibaa-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibaa-dev += CSWlibaa1

PACKAGES += CSWaalib-utils
SPKG_DESC_CSWaalib-utils = Utility programs for the libaa.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWaalib-utils += CSWlibaa1

BUILD64_LIBS_ONLY = 1

include gar/category.mk

