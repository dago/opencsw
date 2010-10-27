# $Id$
GARNAME = django-sorting
GARVERSION = 0.1
CATEGORIES = python
PACKAGES = CSWpy-django-sorting
CATALOGNAME = py_django_sorting
ARCHALL_CSWpy-django-sorting = 1
LICENSE = LICENSE.txt

BUILD_DEP_PKGS += CSWpysetuptools
RUNTIME_DEP_PKGS += CSWpy-django 

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-sorting += surplus-dependency|CSWpy-django

DESCRIPTION = Django application to sort querysets
define BLURB
  django-sorting allows for easy sorting, and tables headers
  generation without modifying the views.
endef

# 1st char of GARNAME is the directory name
MASTER_SITE_DIR = $(shell echo $(GARNAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
