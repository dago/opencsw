# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = libarchive
VERSION = 2.8.4
CATEGORIES = lib

DESCRIPTION = C library for reading and writing various archive formats
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://code.google.com/p/libarchive/

PACKAGES += CSWlibarchive2
SPKG_DESC_CSWlibarchive2 = C library for reading and writing various archive formats, libarchive.so.2
PKGFILES_CSWlibarchive2 = $(call pkgfiles_lib,libarchive.so.2)
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWliblzma5
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibarchive2 += CSWosslrt

PACKAGES += CSWlibarchive-dev
SPKG_DESC_CSWlibarchive-dev = Development files for libarchive.so.2
RUNTIME_DEP_PKGS_CSWlibarchive-dev = CSWlibarchive2
PKGFILES_CSWlibarchive-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibarchive-dev += $(mandir)/man5/.*
OBSOLETED_BY_CSWlibarchive-dev += CSWlibarchive-devel

PACKAGES += CSWlibarchive-utils
SPKG_DESC_CSWlibarchive-utils = Tools for reading and writing various archive formats
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWliblzma5
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibarchive-utils += CSWosslrt

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWlibarchive2)
BUILD_DEP_PKGS += CSWliblzma-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibbz2-dev
BUILD_DEP_PKGS += CSWlibxml2devel
BUILD_DEP_PKGS += CSWossldevel 

EXTRA_INC = $(includedir)/cryptopp

BUILD64 = 1

# There is currently one test failing. Skip until this is fixed:
#   http://code.google.com/p/libarchive/issues/detail?id=171
SKIPTEST ?= 1

include gar/category.mk
