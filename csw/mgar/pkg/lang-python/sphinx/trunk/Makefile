# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = Sphinx
VERSION = 1.1.2
PACKAGES = CSWpy-sphinx
CATEGORIES = python
DESCRIPTION = Helps create documentation consisting of reStructuredText sources
define BLURB
endef
DISTFILES  = $(DISTNAME).tar.gz
ARCHALL_CSWpy-sphinx = 1
DEP_PKGS += CSWpy-docutils
DEP_PKGS += CSWpy-jinja2
DEP_PKGS += CSWpy-pygments
DEP_PKGS += CSWpysetuptools
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpy-docutils
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpy-jinja2
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpy-pygments
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpysetuptools
include gar/category.mk
