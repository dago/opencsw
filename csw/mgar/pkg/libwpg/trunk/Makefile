# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libwpg
VERSION = 0.2.2
GARTYPE = v2

DESCRIPTION = The free WPG library, converter and viewer

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

BUILD_DEP_PKGS += CSWlibwpd-dev

PACKAGES += CSWlibwpg-utils
SPKG_DESC_CSWlibwpg-utils = WordPerfect graphics and utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibwpg-utils += CSWlibwpg0-2-2
RUNTIME_DEP_PKGS_CSWlibwpg-utils += CSWlibwpd-stream0-9-9
RUNTIME_DEP_PKGS_CSWlibwpg-utils += CSWlibwpd0-9-9
RUNTIME_DEP_PKGS_CSWlibwpg-utils += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibwpg-utils += CSWlibgcc-s1

# This is /usr/bin/perl
CHECKPKG_OVERRIDES_CSWlibwpg-utils += missing-dependency|CSWperl

PACKAGES += CSWlibwpg0-2-2
SPKG_DESC_CSWlibwpg0-2-2 = The free WPG library, converter and viewer
PKGFILES_CSWlibwpg0-2-2 += $(call pkgfiles_lib,libwpg-0.2.so.2)
RUNTIME_DEP_PKGS_CSWlibwpg0-2-2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibwpg0-2-2 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibwpg0-2-2 += CSWlibwpd0-9-9

PACKAGES += CSWlibwpg-dev
SPKG_DESC_CSWlibwpg-dev = Development files for libwpg-0.2.so.2
PKGFILES_CSWlibwpg-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibwpg-dev += $(docdir)/libwpg/.*
RUNTIME_DEP_PKGS_CSWlibwpg-dev += CSWlibwpg0-2-2

GARCOMPILER = GNU

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

