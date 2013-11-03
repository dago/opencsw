# $Id$
NAME = astroid
VERSION = 1.0.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Rebuild a new abstract syntax tree from Python ast

DISTFILES  = $(DISTNAME).tar.gz
VENDOR_URL = https://pypi.python.org/pypi/astroid
UPSTREAM_MASTER_SITES = https://pypi.python.org/pypi/astroid/1.0.0
BUILD_DEP_PKGS = CSWpy-setuptools

PACKAGES = CSWpy-astroid

DEP_PKGS = CSWpy-logilab-common
CHECKPKG_OVERRIDES_CSWpy-astroid += surplus-dependency|CSWpy-logilab-common

ARCHALL = 1

include gar/category.mk
