# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2

NAME = django-tagging
VERSION = 0.4
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = A generic tagging application for Django projects
define BLURB
	A generic tagging application for Django projects, which allows association 
	of a number of tags with any Model instance and makes retrieval of tags 
	simple.
endef

SPKG_SOURCEURL = http://code.google.com/p/django-tagging/downloads/detail?name=
DISTFILES += $(DISTNAME).tar.gz

# Django-Tagging 0.4 only supports Python 2.7
MODULATIONS_PYTHON_VERSION = 2_7
CHECKPKG_OVERRIDES_CSWpy-django-tagging += python-package-missing-py26-files

BUILD_DEP_PKGS += CSWpy-setuptools

PACKAGES = CSWpy-django-tagging
SPKG_DESC_CSWpy-django-tagging = A generic tagging application for Django projects
# PKGFILES is catchall
RUNTIME_DEP_PKGS += CSWpy-django
ARCHALL_CSWpy-django-tagging = 1

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-tagging += surplus-dependency|CSWpy-django

# SKIPTEST=1
#TEST_TARGET = check

include gar/category.mk
