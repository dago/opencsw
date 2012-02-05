# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = python-openid
VERSION = 2.2.5
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A library for working with graphs in Python
define BLURB
endef

# Github is not trusted by default
WGET_OPTS = --no-check-certificate -O $(NAME)-$(VERSION).tar.gz
MASTER_SITES = https://github.com/openid/python-openid/tarball/
DISTFILES += $(NAME)-$(VERSION).tar.gz

DISTNAME = openid-python-openid-b666238

VENDOR_URL = https://github.com/openid/python-openid

LICENSE = LICENSE

PACKAGES = CSWpy-openid
ARCHALL_CSWpy-openid = 1

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk
