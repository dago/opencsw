# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = SOAPpy
VERSION = 0.12.0
CATEGORIES = python
DESCRIPTION = SOAP library for Python
define BLURB
endef
SPKG_SOURCEURL = http://pywebsvcs.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
# To get the patch from Ubuntu
MASTER_SITES += http://archive.ubuntu.com/ubuntu/pool/universe/p/python-soappy/
PACKAGES = CSWpy-soappy
CATALOGNAME_CSWpy-soappy = py_soappy
PATCHFILES += python-soappy_0.12.0-4.diff.gz
SF_PROJ = pywebsvcs
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
ARCHALL_CSWpy-soappy = 1
LICENSE = LICENSE
TEST_SCRIPTS =
DEP_PKGS = CSWpyfpconst
CHECKPKG_OVERRIDES_CSWpy-soappy += surplus-dependency|CSWpyfpconst

include gar/category.mk
