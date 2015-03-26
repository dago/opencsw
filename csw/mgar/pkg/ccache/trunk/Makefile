# $Id$
NAME = ccache
VERSION = 3.2.1
GARTYPE = v2

DESCRIPTION = Fast C/C++ compiler cache

MASTER_SITES = http://samba.org/ftp/ccache/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = https://ccache.samba.org

PACKAGES += CSWccache
SPKG_DESC_CSWccache = Fast C/C++ compiler cache
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWccache += CSWlibz1

EXTRA_TEST_EXPORTS += SHELL
TEST_ENV_SHELL = $(SHELL)

include gar/category.mk
