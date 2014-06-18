# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2

NAME = django-schedule
VERSION = git
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = A calendaring app for Django
define BLURB
	simple.
endef

GIT_REPOS = git://github.com/atiberghien/django-schedule.git
# DISTNAME = $(NAME)-$(VERSION)
# DISTFILES  = $(DISTNAME).tar.gz

LICENSE = LICENCSE.txt

# PATCHFILES += 0001-add-schedule.conf.patch

BUILD_DEP_PKGS += CSWpy-setuptools
RUNTIME_DEP_PKGS += CSWpy-django
CHECKPKG_OVERRIDES_CSWpy-django-schedule += surplus-dependency|CSWpy-django
ARCHALL_CSWpy-django-schedule = 1

# checkpkg can't detect python run time dependencies

SKIPTEST=1

include gar/category.mk
