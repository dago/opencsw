# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pyOpenSSL
VERSION = 0.13.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = OpenSSL bindings for Python

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

BUILD_DEP_PKGS_CSWpy-openssl += CSWpython_dev
BUILD_DEP_PKGS_CSWpy-openssl += CSWpython27_dev

PACKAGES += CSWpy-openssl
SPKG_DESC_CSWpy-openssl = OpenSSL bindings for Python
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-openssl += CSWlibssl1-0-0

TEST_SCRIPTS =

include gar/category.mk

