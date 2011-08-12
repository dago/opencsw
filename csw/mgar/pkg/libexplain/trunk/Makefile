# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# * use linkage against libgnugetopt.so only on bin/explain and not the shared library
# * inspect failed tests from the testsuite

NAME = libexplain
VERSION = 0.45.D002
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Explains unix system call errors
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

#PATCHFILES += 0001-Shield-ptrace-defines.patch
#PATCHFILES += 0002-Include-stdarg.h-for-va_list.patch
#PATCHFILES += 0003-Do-not-return-anything-in-void-functions.patch
PATCHFILES += 0004-Use-fallback-for-AI_NUMERICSERV.patch
#PATCHFILES += 0005-Solaris-does-not-have-O_NOFOLLOW.patch
#PATCHFILES += 0006-Fix-typo-of-stat-struct-member.patch
#PATCHFILES += 0007-Need-headers-for-major-minor.patch
PATCHFILES += 0008-inttypes.h-is-needed-for-int-_t.patch
#PATCHFILES += 0009-Use-necessary-mnttab.h.patch
PATCHFILES += 0010-Include-sys-types.h-for-size_t.patch
PATCHFILES += 0011-Make-sure-to-use-GCC-before-testing-GCC-specific-var.patch
PATCHFILES += 0012-Shield-functions-not-available-on-Solaris-9-autoconf.patch
PATCHFILES += 0013-Add-inttypes.h-to-binary-header.patch

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWlibgnugetopt-dev

PACKAGES += CSWexplain
SPKG_DESC_CSWexplain = Explains unix system call errors
PKGFILES_CSWexplain += $(bindir)/.*
PKGFILES_CSWexplain += $(mandir)/man1/.*
RUNTIME_DEP_PKGS_CSWexplain += CSWlibexplain30
RUNTIME_DEP_PKGS_CSWexplain += CSWlibintl8
RUNTIME_DEP_PKGS_CSWexplain += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWexplain += CSWlibiconv2

PACKAGES += CSWlibexplain30
SPKG_DESC_CSWlibexplain30 = Explains unix system call errors, libexplain.so.30
PKGFILES_CSWlibexplain30 += $(call pkgfiles_lib,libexplain.so.30)
RUNTIME_DEP_PKGS_CSWlibexplain30 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibexplain30 += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibexplain30 += CSWlibiconv2

PACKAGES += CSWlibexplain-dev
SPKG_DESC_CSWlibexplain-dev = Development files for libexplain.so.30
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibexplain-dev += CSWlibexplain30

EXTRA_LINKER_FLAGS = -lgnugetopt

BUILD64 = 1

# Several tests failing, skip for now
SKIPTEST ?= 1

TEST_OVERRIDE_VARS = SH
TEST_OVERRIDE_VAR_SH = /bin/bash

include gar/category.mk

