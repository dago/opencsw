# $Id$

NAME = mechanize
VERSION = 0.2.5
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Stateful programmatic web browsing in Python
define BLURB
endef
SPKG_SOURCEURL = http://wwwsearch.sourceforge.net/mechanize/
MASTER_SITES = http://wwwsearch.sourceforge.net/$(NAME)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = PKG-INFO
PACKAGES = CSWpy-mechanize
ARCHALL_CSWpy-mechanize = 1

BUILD_DEP_PKGS	+=	CSWpython-dev
BUILD_DEP_PKGS	+=	CSWpython27-dev

RUNTIME_DEP_PKGS	+=	CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS	+=	CSWlibpython2-7-1-0

# mechanize does have tests, but they require files that we don't have in the
# package repository.
SKIPTEST = 1
include gar/category.mk
