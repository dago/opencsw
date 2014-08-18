# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2

NAME = django-haystack
VERSION = 2.2.0
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Search for Django
define BLURB
Haystack provides modular search for Django. It features a unified, familiar API that allows you to plug in different search backends (such as Solr, Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code.
endef

DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpy-django-haystack
ARCHALL_CSWpy-django-haystack = 1

BUILD_DEP_PKGS += CSWpy-setuptools
RUNTIME_DEP_PKGS += CSWpy-django

# checkpkg can't detect python run time dependencies
CHECKPKG_OVERRIDES_CSWpy-django-haystack += surplus-dependency|CSWpy-django


SKIPTEST=1

include gar/category.mk
