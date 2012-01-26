NAME = exiftool
VERSION = 8.54
CATEGORIES = cpan
GARTYPE = v2

DESCRIPTION = Read, Write and Edit Image File Meta Information
define BLURB
  ExifTool is a platform-independent Perl library plus a command-line application for
  reading, writing and editing meta information in image, audio and video files.
endef

DISTNAME = Image-ExifTool-$(VERSION)

MASTER_SITES = http://owl.phy.queensu.ca/~phil/exiftool/
MODDIST =
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES  += COPYING

RUNTIME_DEP_PKGS += CSWpmiocompress 

UFILES_REGEX = Image-ExifTool-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://owl.phy.queensu.ca/~phil/exiftool/

CONFIGURE_ARGS = $(DIRPATHS)

ARCHALL = 1 
include gar/category.mk
