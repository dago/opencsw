GARNAME = libid3tag
GARVERSION = 0.15.1
REV = b
CATEGORIES = lib

DESCRIPTION = A library for reading and (eventually) writing ID3 tags
define BLURB
endef

SF_PROJ = mad
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION)$(REV).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)$(REV)

REQUIRED_PKGS = CSWzlib

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)_rev=$(REV)
