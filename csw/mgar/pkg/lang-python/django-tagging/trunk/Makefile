# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2

NAME = django-tagging
VERSION = 0.3.1
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = A generig tagging application for Django projects
define BLURB
	A generic tagging application for Django projects, which allows association 
	of a number of tags with any Model instance and makes retrieval of tags 
	simple.
endef

SPKG_SOURCEURL = http://code.google.com/p/django-tagging/downloads/detail?name=
MASTER_SITES = $(GOOGLE_MIRROR)
DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpy-django-tagging
CATALOGNAME = py_django_tagging
ARCHALL_CSWpy-django-tagging = 1

BUILD_DEP_PKGS += CSWpysetuptools
RUNTIME_DEP_PKGS += CSWpy-django

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-tagging += surplus-dependency|CSWpy-django


SKIPTEST=1
#TEST_TARGET = check

include gar/category.mk
