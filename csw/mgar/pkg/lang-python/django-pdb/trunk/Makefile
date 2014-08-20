# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2

NAME = django-pdb
VERSION = 0.4.0
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = PDB access in django
define BLURB
	simple.
endef

# https://pypi.python.org/packages/source/d/django-pdb/django-pdb-0.4.0.tar.gz
DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
MASTER_SITE_DIR = $(shell echo $(NAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(NAME)/

BUILD_DEP_PKGS += CSWpysetuptools
RUNTIME_DEP_PKGS += CSWpy-django
CHECKPKG_OVERRIDES_CSWpy-django-pdb += surplus-dependency|CSWpy-django

ARCHALL_CSWpy-django-pdb = 1

# checkpkg can't detect python run time dependencies

# SKIPTEST=1
#TEST_TARGET = check

include gar/category.mk
