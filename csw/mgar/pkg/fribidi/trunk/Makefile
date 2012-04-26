NAME = fribidi
VERSION = 0.19.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = An implementation of the Unicode Bidirectional Algorithm (bidi)

MASTER_SITES = http://fribidi.org/download/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.fribidi.org/

PACKAGES += CSWlibfribidi0
SPKG_DESC_CSWlibfribidi0 = An implementation of the Unicode Bidirectional Algorithm (bidi), libfribidi.so.0
PKGFILES_CSWlibfribidi0 += $(call pkgfiles_lib,libfribidi.so.0)
OBSOLETED_BY_CSWlibfribidi0 += CSWfribidi

PACKAGES += CSWlibfribidi-dev
SPKG_DESC_CSWlibfribidi-dev = Development files for libfribidi.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibfribidi-dev += CSWlibfribidi0

BUILD64_LIBS_ONLY = 1

TEST_OVERRIDE_VARS += TESTS_ENVIRONMENT
TEST_OVERRIDE_VAR_TESTS_ENVIRONMENT = /opt/csw/bin/bash

include gar/category.mk
