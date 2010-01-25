GARNAME = imagemagick
GARVERSION = 6.5.8
GARSUBREV = 10
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

DISTNAME = ImageMagick-$(GARVERSION)-$(GARSUBREV)

SPKG_SOURCEURL = http://www.imagemagick.org

LICENSE = LICENSE

REQUIRED_PKGS += CSWbzip2 CSWdjvulibrert CSWfconfig CSWftype2 CSWggettextrt
REQUIRED_PKGS += CSWglib2 CSWgs CSWgtk2 CSWilmbase CSWjasper CSWjbigkit
REQUIRED_PKGS += CSWjpeg CSWlcms CSWlibcairo CSWlibfpx CSWlibrsvg CSWlibxml2
REQUIRED_PKGS += CSWopenexr CSWperl CSWpng CSWsunmath CSWtiff CSWwmf CSWzlib
REQUIRED_PKGS += CSWlibtoolrt CSWlibice CSWlibsm CSWlibxext CSWgraphviz
REQUIRED_PKGS += CSWlibx11 CSWlibxt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = ImageMagick-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

#CPPFLAGS += -I/usr/openwin/include -I/usr/openwin/include/X11

CONFIGURE_ARGS_COMMON  = $(DIRPATHS)
CONFIGURE_ARGS_COMMON += --with-perl=$(bindir)/perl
CONFIGURE_ARGS_COMMON += --enable-shared --disable-static
CONFIGURE_ARGS_COMMON += --with-dps=yes --with-gslib=yes
CONFIGURE_ARGS_COMMON += --x-includes=/opt/csw/X11/include
CONFIGURE_ARGS_COMMON += --x-libraries=/opt/csw/X11/lib 
CONFIGURE_ARGS_COMMON += --disable-openmp
CONFIGURE_ARGS_isa-amd64 += --without-gvc
CONFIGURE_ARGS_isa-amd64 += --without-rsvg
CONFIGURE_ARGS_isa-amd64 += --without-perl
CONFIGURE_ARGS_isa-sparcv9 += --without-gvc
CONFIGURE_ARGS_isa-sparcv9 += --without-rsvg
CONFIGURE_ARGS_isa-sparcv9 += --without-perl

CONFIGURE_ARGS ?= $(CONFIGURE_ARGS_COMMON) $(foreach M,$(MODULATIONS),$(CONFIGURE_ARGS_$M))

PATCHFILES += Makefile.patch
# Temporary patch until upstream make a more permenent fix
#PATCHFILES += djvu.c.diff

# Test has to be run *after* install
#TEST_TARGET = check
TEST_TARGET = 

BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#EXTRA_LDFLAGS = -L./magick/.libs 
#EXTRA_LD_OPTIONS = -L./magick/.libs 
# We want to be link with Xrender from $(prefix)/X11/lib not $(prefix)/lib
# since the latter is linked to /usr/openwin/lib/libX11.so.4
EXTRA_SOS_LD_FLAGS  = -L./magick/.libs
EXTRA_SOS_LD_FLAGS +=-L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/lib.*\.la
EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

STRIP_LIBTOOL=1

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libMagick.so.10.0.4.s $(INSTALLISADIR)$(libdir)/libMagick.so.10.0.4
	@cp $(FILEDIR)/libWand.so.10.0.4.s $(INSTALLISADIR)$(libdir)/libWand.so.10.0.4
	@cp $(FILEDIR)/libMagick++.so.10.0.4.s $(INSTALLISADIR)$(libdir)/libMagick++.so.10.0.4
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libMagick.so.10.0.4 ] ; then ln -s libMagick.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libWand.so.10.0.4 ] ; then ln -s libWand.so.10.0.4 $(INSTALLISADIR)$(libdir)/libWand.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libMagick++.so.10.0.4 ] ; then ln -s libMagick++.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick++.so.10 ; fi )
	@ln -s ImageMagick-$(GARVERSION) $(INSTALLISADIR)$(docdir)/ImageMagick
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(CURDIR)/$(FILEDIR)/lib_6.2.9_s.tar.gz |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)

post-install-isa-i386:
	@cp $(FILEDIR)/libMagick.so.10.0.4.i $(INSTALLISADIR)$(libdir)/libMagick.so.10.0.4
	@cp $(FILEDIR)/libWand.so.10.0.4.i $(INSTALLISADIR)$(libdir)/libWand.so.10.0.4
	@cp $(FILEDIR)/libMagick++.so.10.0.4.i $(INSTALLISADIR)$(libdir)/libMagick++.so.10.0.4
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libMagick.so.10.0.4 ] ; then ln -s libMagick.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libWand.so.10.0.4 ] ; then ln -s libWand.so.10.0.4 $(INSTALLISADIR)$(libdir)/libWand.so.10 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libMagick++.so.10.0.4 ] ; then ln -s libMagick++.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick++.so.10 ; fi )
	@ln -s ImageMagick-$(GARVERSION) $(INSTALLISADIR)$(docdir)/ImageMagick
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(CURDIR)/$(FILEDIR)/lib_6.2.9_i.tar.gz |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)
