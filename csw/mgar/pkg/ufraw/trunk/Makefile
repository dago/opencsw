# $Id$

NAME = ufraw
VERSION = 0.17
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A tool for reading and manipulating raw images from digital cameras
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWlibgnugetopt CSWliblensfun

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
