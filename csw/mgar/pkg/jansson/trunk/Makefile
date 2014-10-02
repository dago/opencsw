# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jansson
VERSION = 2.7
GARTYPE = v2

DESCRIPTION = C library for encoding, decoding and manipulating JSON data

MASTER_SITES = http://www.digip.org/jansson/releases/
DISTFILES  = $(DISTNAME).tar.bz2

VENDOR_URL = http://www.digip.org/jansson/

PACKAGES += CSWlibjansson4
SPKG_DESC_CSWlibjansson4 = C library for encoding, decoding and manipulating JSON data, libjansson.so.4
PKGFILES_CSWlibjansson4 += $(call pkgfiles_lib,libjansson.so.4)

PACKAGES += CSWlibjansson-dev
SPKG_DESC_CSWlibjansson-dev = Development files for libjansson.so.4
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibjansson-dev += CSWlibjansson4

BUILD64 = 1

EXTRA_CPPFLAGS = -features=extensions -D__FUNCTION__=__func__

REINPLACEMENTS += bash
REINPLACE_MATCH_bash = /bin/sh
REINPLACE_WITH_bash = /bin/bash
REINPLACE_FILES_bash += test/run-suites
REINPLACE_FILES_bash += test/suites/api/run
REINPLACE_FILES_bash += test/suites/invalid-unicode/run
REINPLACE_FILES_bash += test/suites/invalid/run
REINPLACE_FILES_bash += test/suites/valid/run

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

