GARNAME      = dbh
GARVERSION   = 1.0.24
CATEGORIES   = xfce
XFCE_VERSION = 4.2.3.2

DESCRIPTION = Disk based hash tables, dbh
define BLURB
  Disk based hash tables
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST    = $(GARNAME)-$(GARVERSION).tar.gz	

#DISTFILES += $(call admfiles,CSWdbh, )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Package description
CATALOGNAME = dbh
PACKAGES    = CSWdbh

# Defines dependencies
REQUIRED_PKGS_CSWdbh    = 

TEST_SCRIPTS = 

include gar/category.mk

