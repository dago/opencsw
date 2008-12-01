GARNAME = ImageMagick
GARVERSION = 6.2.7
GARSUBREV = 8
CATEGORIES = lib

DESCRIPTION = A comprehensive package supporting automated and interative manipulation of images
define BLURB
  ImageMagick is a robust collection of tools and libraries offered under a
  usage license to read, write, and manipulate an image in many image formats
  (over 89 major formats) including popular formats like TIFF, JPEG, PNG, PDF,
  PhotoCD, and GIF.
endef

MASTER_SITES = ftp://ftp.fifi.org/pub/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION)-$(GARSUBREV).tar.bz2
DISTFILES += $(call admfiles,CSWimagick,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-(\d+).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --enable-shared --disable-static

# Test has to be run *after* install
TEST_SCRIPTS =

include gar/category.mk

post-install:
	@echo " ==> Running tests for $(GARNAME)"
	@$(MAKE) -C $(WORKSRC) check
