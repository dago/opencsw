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

BUILD_DEP_PKGS += CSWpy-setuptools
BUILD_DEP_PKGS += CSWpy-django
BUILD_DEP_PKGS += CSWpy-argparse

PACKAGES = CSWpy-django-ckeditor
ARCHALL_CSWpy-django-ckeditor = 1

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-ckeditor += surplus-dependency|CSWpy-django

# ImportError: Unable to import test settings: No module named test_settings
SKIPTEST=1

include gar/category.mk
