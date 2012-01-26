# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = liferea
VERSION = 1.6.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = An aggregator for online news feeds
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# We need GNU msgfont
PATH := /opt/csw/gnu:$(PATH)
