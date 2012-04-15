# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = setproctitle
VERSION = 1.1.5
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A library to allow customization of the process title

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES = $(DISTNAME).tar.gz

VENDOR_URL = http://code.google.com/p/py-setproctitle/

PACKAGES = CSWpy-setproctitle
RUNTIME_DEP_PKGS_CSWpy-setproctitle += CSWlibpython2-6-1-0
CHECKPKG_OVERRIDES_CSWpy-setproctitle += surplus-dependency|CSWpython

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk
