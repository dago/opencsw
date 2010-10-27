# $Id$
GARNAME = django-filter
GARVERSION = 0.5.3
CATEGORIES = python
PACKAGES = CSWpy-django-filter
CATALOGNAME = py_django_filter
ARCHALL_CSWpy-django-filter = 1
LICENSE = COPYRIGHT

BUILD_DEP_PKGS += CSWpysetuptools
RUNTIME_DEP_PKGS += CSWpy-django 

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-filter += surplus-dependency|CSWpy-django

DESCRIPTION = Django application to filter querysets
define BLURB
  Django-filter is a reusable Django application for allowing users to
  filter qu eryset dynamically.
endef

# 1st char of GARNAME is the directory name
MASTER_SITE_DIR = $(shell echo $(GARNAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
