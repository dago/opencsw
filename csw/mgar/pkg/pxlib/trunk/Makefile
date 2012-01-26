NAME = pxlib
VERSION = 0.6.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library to read and write Paradox databases
define BLURB
	pxlib is a simply and still small C library to read and write Paradox DB 
	files. It supports all versions starting from 3.0. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

SPKG_SOURCEURL = http://pxlib.sourceforge.net

LICENSE = COPYING

#RUNTIME_DEP_PKGS += CSWggettextrt

UPSTREAM_MASTER_SITES = http://sourceforge.net/projects/pxlib/files
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
