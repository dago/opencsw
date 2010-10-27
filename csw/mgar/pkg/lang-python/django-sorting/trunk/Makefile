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

MASTER_SITES = http://github.com/mirumee/$(GARNAME)/tarball/master/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# There's a problem that the download URL of the source tarball does not
# contain the file name. The browser is being redirected instead. Hard-coding
# the URL and using a custom target to fit the rest of mGAR.
http//github.com/mirumee/$(GARNAME)/tarball/master/$(GARNAME)-$(GARVERSION).tar.gz:
	@wget $(WGET_OPTS) -T 30 -c -P $(PARTIALDIR) -O $(DISTFILES) http://github.com/mirumee/$(GARNAME)/tarball/master/


CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
