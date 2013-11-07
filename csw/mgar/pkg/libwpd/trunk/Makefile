# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libwpd
VERSION = 0.9.9
GARTYPE = v2

DESCRIPTION = A library for importing WordPerfect documents

MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.xz

VENDOR_URL = http://libwpd.sourceforge.net

PACKAGES += CSWlibwpd-utils
SPKG_DESC_CSWlibwpd-utils = WorkPerfect import utilities
RUNTIME_DEP_PKGS_CSWlibwpd-utils += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibwpd-utils += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibwpd-utils += CSWlibwpd-stream0-9-9
RUNTIME_DEP_PKGS_CSWlibwpd-utils += CSWlibwpd0-9-9
OBSOLETED_BY_CSWlibwpd-utils += CSWlibwpd

PACKAGES += CSWlibwpd0-9-9
SPKG_DESC_CSWlibwpd0-9-9 = A library for importing WorkPerfect documents, libwpd-0.9.so.9
PKGFILES_CSWlibwpd0-9-9 += $(call pkgfiles_lib,libwpd-0.9.so.9)
RUNTIME_DEP_PKGS_CSWlibwpd0-9-9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibwpd0-9-9 += CSWlibstdc++6

PACKAGES += CSWlibwpd-stream0-9-9
SPKG_DESC_CSWlibwpd-stream0-9-9 = A library for importing WorkPerfect documents, libwpd-stream-0.9.so.9
PKGFILES_CSWlibwpd-stream0-9-9 += $(call pkgfiles_lib,libwpd-stream-0.9.so.9)
RUNTIME_DEP_PKGS_CSWlibwpd-stream0-9-9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibwpd-stream0-9-9 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibwpd-stream0-9-9 += CSWlibz1

PACKAGES += CSWlibwpd-dev
SPKG_DESC_CSWlibwpd-dev = Development files for libwpd-0.9.so.9 and libwpd-stream-0.9.so.9
PKGFILES_CSWlibwpd-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibwpd-dev += $(docdir)/libwpd/.*
RUNTIME_DEP_PKGS_CSWlibwpd-dev += CSWlibwpd-stream0-9-9
RUNTIME_DEP_PKGS_CSWlibwpd-dev += CSWlibwpd0-9-9

GARCOMPILER = GNU

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

# No cppunit ATM
SKIPTEST ?= 1

include gar/category.mk

