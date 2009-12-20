GARNAME = imagemagick
GARVERSION = 6.5.8
GARSUBREV = 6
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

REQUIRED_PKGS += CSWbzip2 CSWdjvulibre CSWfconfig CSWftype2 CSWggettextrt
REQUIRED_PKGS += CSWglib2 CSWgs CSWgtk2 CSWilmbase CSWjasper CSWjbigkit
REQUIRED_PKGS += CSWjpeg CSWlcms CSWlibcairo CSWlibfpx CSWlibrsvg CSWlibxml2
REQUIRED_PKGS += CSWopenexr CSWperl CSWpng CSWsunmath CSWtiff CSWwmf CSWzlib
REQUIRED_PKGS += CSWlibtoolrt CSWlibice CSWlibsm CSWlibxext

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = ImageMagick-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

CPPFLAGS += -I/usr/openwin/include -I/usr/openwin/include/X11

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --enable-shared --disable-static
CONFIGURE_ARGS += --with-dps=yes --with-gslib=yes
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib 
CONFIGURE_ARGS += --disable-openmp

PATCHFILES += Makefile.patch
# Temporary patch until upstream make a more permenent fix
#PATCHFILES += djvu.c.diff

# Test has to be run *after* install
TEST_SCRIPTS =

EXTRA_LD_OPTIONS = -L./magick/.libs 
MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/lib.*\.la
EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

STRIP_LIBTOOL=1

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libMagick.so.10.0.4.s $(INSTALLISADIR)$(libdir)/libMagick.so.10.0.4
	@cp $(FILEDIR)/libWand.so.10.0.4.s $(INSTALLISADIR)$(libdir)/libWand.so.10.0.4
	@cp $(FILEDIR)/libMagick++.so.10.0.4.s $(INSTALLISADIR)$(libdir)/libMagick++.so.10.0.4
	@ln -s libMagick.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick.so.10
	@ln -s libWand.so.10.0.4 $(INSTALLISADIR)$(libdir)/libWand.so.10
	@ln -s libMagick++.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick++.so.10
	@ln -s ImageMagick-$(GARVERSION) $(INSTALLISADIR)$(docdir)/ImageMagick
	echo $(DESTDIR)
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/lib_6.2.9_s.tar.gz |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)

post-install-isa-i386:
	@cp $(FILEDIR)/libMagick.so.10.0.4.i $(INSTALLISADIR)$(libdir)/libMagick.so.10.0.4
	@cp $(FILEDIR)/libWand.so.10.0.4.i $(INSTALLISADIR)$(libdir)/libWand.so.10.0.4
	@cp $(FILEDIR)/libMagick++.so.10.0.4.i $(INSTALLISADIR)$(libdir)/libMagick++.so.10.0.4
	@ln -s libMagick.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick.so.10
	@ln -s libWand.so.10.0.4 $(INSTALLISADIR)$(libdir)/libWand.so.10
	@ln -s libMagick++.so.10.0.4 $(INSTALLISADIR)$(libdir)/libMagick++.so.10
	@ln -s ImageMagick-$(GARVERSION) $(INSTALLISADIR)$(docdir)/ImageMagick
	echo $(DESTDIR)
	@( cd $(INSTALLISADIR)$(libdir) ; gzip -dc $(DESTDIR)/../../$(FILEDIR)/lib_6.2.9_i.tar.gz |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)
