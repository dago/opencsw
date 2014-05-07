# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = check
VERSION = 0.9.12
GARTYPE = v2

DESCRIPTION = A unit test framework for C

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWlibcheck0
SPKG_DESC_CSWlibcheck0 = A unit test framework for C, libcheck.so.0
PKGFILES_CSWlibcheck0 += $(call pkgfiles_lib,libcheck.so.0)

PACKAGES += CSWlibcheck-dev
SPKG_DESC_CSWlibcheck-dev = Development files for libckeck.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibcheck-dev += CSWlibcheck0

REINPLACEMENTS += bash
REINPLACE_MATCH_bash = /bin/sh
REINPLACE_WITH_bash = /bin/bash
REINPLACE_FILES_bash += checkmk/test/check_checkmk

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)
# -pedantic is not rejected, but leads to _mcount not being defined, see for details
#   http://wiki.opencsw.org/porting-faq#toc8
CONFIGURE_ARGS += ax_cv_c_check_flag__pedantic=no

BUILD_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk

