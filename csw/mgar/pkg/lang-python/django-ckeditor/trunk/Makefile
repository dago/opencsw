# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2

NAME = django-ckeditor
VERSION = 4.0.2
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Django admin CKEditor integration
define BLURB
endef

DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpy-django-ckeditor

BUILD_DEP_PKGS += CSWpysetuptools
RUNTIME_DEP_PKGS += CSWpy-django

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-ckeditor += surplus-dependency|CSWpy-django

# SKIPTEST=1

include gar/category.mk
