# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
GARNAME = maildrop
GARVERSION = 2.4.3
CATEGORIES = utils

DESCRIPTION = Mail delivery agent with filtering abilities
define BLURB
endef

SF_PROJ = courier
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

DEP_PKGS = CSWlibidn CSWgdbm CSWpcrert

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# We need whoami
PATH := /opt/csw/gnu:$(PATH)
