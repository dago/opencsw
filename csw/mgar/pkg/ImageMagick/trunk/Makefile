GARNAME = imagemagick
GARVERSION = 6.6.0
GARSUBREV = 5
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

RUNTIME_DEP_PKGS_CSWimagemagick += CSWbzip2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWdjvulibrert
RUNTIME_DEP_PKGS_CSWimagemagick += CSWfconfig
RUNTIME_DEP_PKGS_CSWimagemagick += CSWftype2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWggettextrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWglib2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWgraphviz
RUNTIME_DEP_PKGS_CSWimagemagick += CSWgs
RUNTIME_DEP_PKGS_CSWimagemagick += CSWgtk2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWilmbase
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjasper
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjbigkit
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjpeg
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlcmsrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcairo
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfpx
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibice
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibsm
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibtoolrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwmf
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibx11
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxext
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxml2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWperl
RUNTIME_DEP_PKGS_CSWimagemagick += CSWpng
RUNTIME_DEP_PKGS_CSWimagemagick += CSWsunmath
RUNTIME_DEP_PKGS_CSWimagemagick += CSWtiffrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = ImageMagick-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

CONFIGURE_ARGS_COMMON  = $(DIRPATHS)
CONFIGURE_ARGS_COMMON += --with-perl=$(bindir)/perl
CONFIGURE_ARGS_COMMON += --enable-shared --disable-static
CONFIGURE_ARGS_COMMON += --with-dps=yes --with-gslib=yes
CONFIGURE_ARGS_COMMON += --x-includes=/opt/csw/X11/include
CONFIGURE_ARGS_COMMON += --x-libraries=/opt/csw/X11/lib 
CONFIGURE_ARGS_COMMON += --with-modules=yes
#CONFIGURE_ARGS_COMMON += --disable-openmp
CONFIGURE_ARGS_COMMON += --disable-silent-rules
# Until librsvg,graphviz and perl is 64bit
#CONFIGURE_ARGS_isa-amd64 += --without-gvc
#CONFIGURE_ARGS_isa-amd64 += --without-rsvg
#CONFIGURE_ARGS_isa-amd64 += --without-perl
#CONFIGURE_ARGS_isa-sparcv9 += --without-gvc
#CONFIGURE_ARGS_isa-sparcv9 += --without-rsvg
#CONFIGURE_ARGS_isa-sparcv9 += --without-perl

CONFIGURE_ARGS = $(CONFIGURE_ARGS_COMMON) $(foreach M,$(MODULATIONS),$(CONFIGURE_ARGS_$M))

PATCHFILES += Makefile.patch
PATCHFILES += configure.diff

# Test has to be run *after* install
#TEST_TARGET = check
TEST_TARGET = 

#Dependencies not 64-bit yet
#BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#EXTRA_LDFLAGS = -L./magick/.libs 
#EXTRA_LD_OPTIONS = -L./magick/.libs 
#
EXTRA_SOS_LD_FLAGS += -L$(shell pwd)/$(WORKSRC)/magick/.libs
EXTRA_SOS_LD_FLAGS += -L$(shell pwd)/$(WORKSRC)/wand/.libs
# We want to be link with Xrender from $(prefix)/X11/lib not $(prefix)/lib
# since the latter is linked to /usr/openwin/lib/libX11.so.4
EXTRA_SOS_LD_FLAGS += -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/lib.*\.la
EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

STRIP_LIBTOOL=1

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)

post-install-isa-sparcv8:
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.2.9.s.tar.bz2 |tar xf -)
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.5.2.s.tar.bz2 |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)

post-install-isa-i386:
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.2.9.i.tar.bz2 |tar xf -)
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.5.2.i.tar.bz2 |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)
