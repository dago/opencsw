# $Id$

NAME		=	cssutils
VERSION		=	0.9.10b1
CATEGORIES	=	python
GARTYPE		=	v2

DESCRIPTION	=	CSS Cascading Style Sheets parser and builder
define BLURB
  A Python package to parse and build CSS Cascading Style Sheets.
  DOM only, not any rendering facilities!
endef

MASTER_SITES	=	https://bitbucket.org/cthedot/cssutils/downloads/
DISTFILES 		=	$(DISTNAME).zip

BUILD_DEP_PKGS	+=	CSWpython-dev
BUILD_DEP_PKGS	+=	CSWpython27-dev
BUILD_DEP_PKGS	+=	CSWpy-setuptools

CONFIGURE_ARGS	=	$(DIRPATHS)

TEST_SCRIPTS	=	non-stop

ARCHALL	=	1

RUNTIME_DEP_PKGS	+=	CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS	+=	CSWlibpython2-7-1-0

EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/lib/python/site-packages/tests.*

include gar/category.mk

test-non-stop:
	-( cd $(WORKSRC) && $(TEST_ENV) python ./setup.py test $(TEST_ARGS) )
	$(MAKECOOKIE)
