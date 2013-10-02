# Copyright 2009-2013 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = Sphinx
VERSION = 1.1.3
PACKAGES = CSWpy-sphinx
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Helps create documentation consisting of reStructuredText sources
define BLURB
endef
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-fix-infodir.patch

BUILD_DEP_PKGS	+=	CSWpython-dev
BUILD_DEP_PKGS	+=	CSWpython27-dev
BUILD_DEP_PKGS	+=	CSWpy-docutils
BUILD_DEP_PKGS	+=	CSWpy-jinja2
BUILD_DEP_PKGS	+=	CSWpy-pygments
BUILD_DEP_PKGS	+=	CSWpysetuptools
BUILD_DEP_PKGS	+=	CSWtexinfo

PACKAGES					+=	CSWpy-sphinx
CATALOGNAME_CSWpy-sphinx	=	py_sphinx
SPKG_DESC_CSWpy-sphinx		+=	$(DESCRIPTION)
ARCHALL_CSWpy-sphinx		=	1
RUNTIME_DEP_PKGS += CSWpy-docutils
RUNTIME_DEP_PKGS += CSWpy-jinja2
RUNTIME_DEP_PKGS += CSWpy-pygments
RUNTIME_DEP_PKGS += CSWpysetuptools
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpy-docutils
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpy-jinja2
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpy-pygments
CHECKPKG_OVERRIDES_CSWpy-sphinx += surplus-dependency|CSWpysetuptools

PACKAGES						+=	CSWpy-sphinx-doc
CATALOGNAME_CSWpy-sphinx-doc	=	py_sphinx_doc
SPKG_DESC_CSWpy-sphinx-doc		+=	$(DESCRIPTION), documentation
PKGFILES_CSWpy-sphinx-doc		+=	/opt/csw/share/info/.*
ARCHALL_CSWpy-sphinx-doc		=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-build:
	cd $(WORKSRC)/doc && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) info
	$(MAKECOOKIE)

post-install:
	ginstall -d "$(DESTDIR)$(infodir)"
	cd $(WORKSRC)/doc/_build/texinfo && ginstall --preserve-timestamps --mode=u=rw,go=r *.info *.png $(DESTDIR)$(infodir)
	$(MAKECOOKIE)
