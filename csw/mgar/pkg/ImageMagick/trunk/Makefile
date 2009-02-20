GARNAME = imagemagick
GARVERSION = 6.4.9
GARSUBREV = 4
CATEGORIES = lib

DESCRIPTION = A comprehensive package supporting automated and interative manipulation of images
define BLURB
  ImageMagick is a robust collection of tools and libraries offered under a
  usage license to read, write, and manipulate an image in many image formats
  (over 89 major formats) including popular formats like TIFF, JPEG, PNG, PDF,
  PhotoCD, and GIF.
endef

MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/
DISTFILES  = ImageMagick-$(GARVERSION)-$(GARSUBREV).tar.bz2
DISTFILES += libMagick++.so.10.0.4.i
DISTFILES += libMagick++.so.10.0.4.s
DISTFILES += libMagick.so.10.0.4.i
DISTFILES += libMagick.so.10.0.4.s
DISTFILES += libWand.so.10.0.4.i
DISTFILES += libWand.so.10.0.4.s

DISTNAME = ImageMagick-$(GARVERSION)-$(GARSUBREV)

LICENSE = LICENSE

REQUIRED_PKGS += CSWbzip2 CSWfconfig CSWftype2 CSWgcc2g++rt CSWggettextrt
REQUIRED_PKGS += CSWggettext CSWsunmath
REQUIRED_PKGS += CSWglib2 CSWgs CSWgtk2 CSWilmbase CSWjasper CSWjbigkit
REQUIRED_PKGS += CSWjpeg CSWlcms CSWlibcairo CSWlibfpx CSWlibrsvg 
REQUIRED_PKGS += CSWlibxml2 CSWopenexr CSWperl CSWpng CSWtiff CSWwmf CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-(\d+).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --enable-shared --disable-static

PATCHFILES += Makefile.patch

# Test has to be run *after* install
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

include gar/category.mk

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libMagick.so.10.0.4.s $(INSTALLISADIR)/opt/csw/lib/libMagick.so.10
	@cp $(FILEDIR)/libWand.so.10.0.4.s $(INSTALLISADIR)/opt/csw/lib/libWand.so.10
	@cp $(FILEDIR)/libMagick++.so.10.0.4.s $(INSTALLISADIR)/opt/csw/lib/libMagick++.so.10
	#@ln -s libMagick.so.10.0.4 $(INSTALLISADIR)/opt/csw/lib/libMagick.so.10
	#@ln -s libWand.so.10.0.4 $(INSTALLISADIR)/opt/csw/lib/libWand.so.10
	#@ln -s libMagick++.so.10.0.4 $(INSTALLISADIR)/opt/csw/lib/libMagick++.so.10

post-install-isa-i386:
	@cp $(FILEDIR)/libMagick.so.10.0.4.i $(INSTALLISADIR)/opt/csw/lib/libMagick.so.10
	@cp $(FILEDIR)/libWand.so.10.0.4.i $(INSTALLISADIR)/opt/csw/lib/libWand.so.10
	@cp $(FILEDIR)/libMagick++.so.10.0.4.i $(INSTALLISADIR)/opt/csw/lib/libMagick++.so.10
	#@ln -s libMagick.so.10.0.4 $(INSTALLISADIR)/opt/csw/lib/libMagick.so.10
	#@ln -s libWand.so.10.0.4 $(INSTALLISADIR)/opt/csw/lib/libWand.so.10
	#@ln -s libMagick++.so.10.0.4 $(INSTALLISADIR)/opt/csw/lib/libMagick++.so.10
