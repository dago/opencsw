# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2

NAME = django-mptt
VERSION = 0.6.1
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Modified Preorder Tree Traversal utilities
define BLURB
Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.
endef

DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpy-django-mptt
ARCHALL_CSWpy-django-mptt = 1

BUILD_DEP_PKGS += CSWpy-setuptools
RUNTIME_DEP_PKGS += CSWpy-django

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-mptt += surplus-dependency|CSWpy-django


# SKIPTEST=1

include gar/category.mk
