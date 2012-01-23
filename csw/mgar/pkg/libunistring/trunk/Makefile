# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libunistring
VERSION = 0.9.3
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Provides functions for manipulating Unicode strings
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWlibunistring0
SPKG_DESC_CSWlibunistring0 = Provides functions for manipulating Unicode strings, libunistring.so.0
PKGFILES_CSWlibunistring0 += $(call pkgfiles_lib,libunistring.so.0)
RUNTIME_DEP_PKGS_CSWlibunistring0 += CSWlibiconv2

PACKAGES += CSWlibunistring-dev
SPKG_DESC_CSWlibunistring-dev = Development files for libunistring.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibunistring-dev += CSWlibunistring0

# These are just docs, override for now
CHECKPKG_OVERRIDES_CSWlibunistring-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libunistring/libunistring_15.html
CHECKPKG_OVERRIDES_CSWlibunistring-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/libunistring.info

BUILD64_LIBS_ONLY = 1

EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset\.alias

include gar/category.mk

