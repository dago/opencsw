GARNAME = exiftool
GARVERSION = 7.69
CATEGORIES = cpan

DESCRIPTION = Read, Write and Edit Image File Meta Information
define BLURB
  ExifTool is a platform-independent Perl library plus a command-line application for
  reading, writing and editing meta information in image, audio and video files.
endef

DISTNAME = Image-ExifTool-$(GARVERSION)

MASTER_SITES = http://owl.phy.queensu.ca/~phil/exiftool/
MODDIST =
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += $(call admfiles,CSWexiftool,)

REQUIRED_PKGS += CSWperl CSWpmcompresszlib
# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
