GARNAME = ImageMagick
GARVERSION = 5.5.7
GARSUBREV = 10
CATEGORIES = lib

SPKG_PKGNAME = CSWimagick
SPKG_BITNAME = imagemagick

DESCRIPTION = A comprehensive package supporting automated and interative manipulation of images
define BLURB
  ImageMagickTM 5.5.7 is a robust collection of tools and libraries offered
  under a usage license to read, write, and manipulate an image in many image
  formats (over 89 major formats) including popular formats like TIFF, JPEG,
  PNG, PDF, PhotoCD, and GIF.
endef

MASTER_SITES = ftp://ftp.imagemagick.org/pub/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION)-$(GARSUBREV).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --enable-shared --disable-static

# Test has to be run *after* install
ENABLE_TEST = 0

include ../category.mk

post-install:
	@echo " ==> Running tests for $(GARNAME)"
	@$(MAKE) -C $(WORKSRC) check
