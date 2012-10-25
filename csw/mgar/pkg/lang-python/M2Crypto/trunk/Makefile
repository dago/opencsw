# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = M2Crypto
VERSION = 0.21.1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = The most complete Python wrapper for OpenSSL
define BLURB
endef

MASTER_SITES = http://pypi.python.org/packages/source/M/M2Crypto/
DISTFILES = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://chandlerproject.org/Projects/MeTooCrypto

PACKAGES = CSWpy-m2crypto
SPKG_DESC_CSWpy-m2crypto = The most complete Python wrapper for OpenSSL
RUNTIME_DEP_PKGS_CSWpy-m2crypto += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWpy-m2crypto += CSWlibpython2-6-1-0

PYBUILD_CMD = build build_ext
BUILD_ARGS += --openssl=$(prefix)


# Skip testsuite until this is fixed:
#   https://bugzilla.osafoundation.org/show_bug.cgi?id=13039
SKIPTEST ?= 1

include gar/category.mk
