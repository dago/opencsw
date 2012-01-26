NAME = iso-codes
VERSION = 3.17
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Translations for names of various ISO standards
define BLURB
	This package provides lists of various ISO standards (e.g. country,
	language, language scripts, and currency names) in one place, rather
	than repeated in many programs throughout the system
endef

MASTER_SITES = ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PACKAGES = CSWiso-codes
CATALOGNAME = iso_codes
SPKG_SOURCEURL = http://alioth.debian.org/projects/pkg-isocodes/
 
LICENSE = LICENSE

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check 

ARCHALL = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
