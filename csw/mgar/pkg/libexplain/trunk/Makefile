# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# * inspect failed tests from the testsuite

NAME = libexplain
VERSION = 0.52.D002
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Explains unix system call errors
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Solaris-fixes.patch

LICENSE = LICENSE

PACKAGES += CSWexplain
SPKG_DESC_CSWexplain = Explains unix system call errors
PKGFILES_CSWexplain += $(bindir)/.*
PKGFILES_CSWexplain += $(mandir)/man1/.*
RUNTIME_DEP_PKGS_CSWexplain += CSWlibexplain30
RUNTIME_DEP_PKGS_CSWexplain += CSWlibintl8
RUNTIME_DEP_PKGS_CSWexplain += CSWlibiconv2

PACKAGES += CSWlibexplain30
SPKG_DESC_CSWlibexplain30 = Explains unix system call errors, libexplain.so.30
PKGFILES_CSWlibexplain30 += $(call pkgfiles_lib,libexplain.so.30)
RUNTIME_DEP_PKGS_CSWlibexplain30 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibexplain30 += CSWlibiconv2

PACKAGES += CSWlibexplain-dev
SPKG_DESC_CSWlibexplain-dev = Development files for libexplain.so.30
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibexplain-dev += CSWlibexplain30

BUILD64_LIBS_ONLY = 1

include gar/category.mk
