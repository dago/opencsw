GARNAME = ghostscript
GARVERSION = 8.70
CATEGORIES = apps

DESCRIPTION = EXIF Tag Parsing Library
define BLURB
  libexif is a library for parsing, editing, and saving EXIF data. It is
	intended to replace lots of redundant implementations in command-line
	utilities and programs with GUIs.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

SPKG_SOURCEURL = http://www.ghostscript.com

LICENSE = COPYING

REQUIRED_PKGS += 

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
