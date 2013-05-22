# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jbig2dec
VERSION = 0.11
GARTYPE = v2

DESCRIPTION = Decoder implementing JBIG2 bi-level image compression

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

PATCHFILES += 0001-Fix-test-in-testsuite.patch

VENDOR_URL = http://jbig2dec.sourceforge.net

PACKAGES += CSWjbig2dec
SPKG_DESC_CSWjbig2dec = Decoder implementing JBIG2 bi-level image compression
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWjbig2dec += CSWlibjbig2dec0

PACKAGES += CSWlibjbig2dec0
SPKG_DESC_CSWlibjbig2dec0 = Library for decoding JBIG2 bi-level images, libjbig2dec.so.0
PKGFILES_CSWlibjbig2dec0 += $(call pkgfiles_lib,libjbig2dec.so.0)

PACKAGES += CSWlibjbig2dec-dev
SPKG_DESC_CSWlibjbig2dec-dev = Development files for libjbig2dec.so.0
PKGFILES_CSWlibjbig2dec-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibjbig2dec-dev += CSWlibjbig2dec0

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

# We need /opt/csw/bin/python for the testsuite
TEST_ENV_PATH = $(bindir):$(PATH)

include gar/category.mk

