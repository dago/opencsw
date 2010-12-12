NAME = imagemagick
VERSION = 6.6.0
GARSUBREV = 5
CATEGORIES = lib

DESCRIPTION = A software suite to create, edit, and compose bitmap images
define BLURB
  ImageMagick is a robust collection of tools and libraries offered under a
  usage license to read, write, and manipulate an image in many image formats
  (over 89 major formats) including popular formats like TIFF, JPEG, PNG, PDF,
  PhotoCD, and GIF.
endef

PACKAGES = CSWimagemagick CSWimagemagickrt CSWpmimagemagick CSWimagemagickdoc CSWimagemagickdev
CATALOGNAME_CSWimagemagick = imagemagick
CATALOGNAME_CSWimagemagickdev = imagemagick_devel
CATALOGNAME_CSWimagemagickdoc = imagemagick_doc
CATALOGNAME_CSWimagemagickrt = imagemagick_rt
CATALOGNAME_CSWpmimagemagick = pm_imagemagick
SPKG_DESC_CSWimagemagick = $(DESCRIPTION)
SPKG_DESC_CSWimagemagickdev = $(DESCRIPTION) - development package
SPKG_DESC_CSWimagemagickdoc = $(DESCRIPTION) - documentation 
SPKG_DESC_CSWimagemagickrt = $(DESCRIPTION) - runtime package
SPKG_DESC_CSWpmimagemagick = $(DESCRIPTION) - perl module

PKGFILES_CSWimagemagickdev = $(PKGFILES_DEVEL)
PKGFILES_CSWimagemagickrt = $(PKGFILES_RT)
PKGFILES_CSWimagemagickrt += $(call baseisadirs,$(libdir),ImageMagick.*)
PKGFILES_CSWimagemagickrt += $(sharedstatedir)/ImageMagick.*
PKGFILES_CSWimagemagickdoc = $(docdir)/ImageMagick.*
PKGFILES_CSWpmimagemagick = $(libdir)/perl/.*

ARCHALL_CSWimagemagickdoc = 1

MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/
DISTFILES  = ImageMagick-$(VERSION)-$(GARSUBREV).tar.bz2

DISTNAME = ImageMagick-$(VERSION)-$(GARSUBREV)

SPKG_SOURCEURL = http://www.imagemagick.org

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWimagemagick += CSWbzip2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWfconfig
RUNTIME_DEP_PKGS_CSWimagemagick += CSWftype2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWimagemagickrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjpeg
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlcmsrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibice
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibsm
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibtoolrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibx11
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxext
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWtiffrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWzlib

RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWbzip2
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWdjvulibrert
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWfconfig
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWftype2
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWggettextrt
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWglib2
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWgraphviz
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWgs
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWgtk2
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWilmbase
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWjasper
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWjbigkit
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWjpeg
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlcmsrt
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibcairo
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibfpx
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibice
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibsm
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibtoolrt
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibwmf
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibx11
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibxext
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibxml2
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWlibxt
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWpng
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWsunmath
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWtiffrt
RUNTIME_DEP_PKGS_CSWimagemagickrt += CSWzlib

RUNTIME_DEP_PKGS_CSWpmimagemagick += CSWimagemagickrt
RUNTIME_DEP_PKGS_CSWpmimagemagick += CSWperl

CHECKPKG_OVERRIDES_CSWimagemagickdev += missing-dependency|CSWimagemagick

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
#
EXTRA_SOS_LD_FLAGS += -L$(shell pwd)/$(WORKSRC)/magick/.libs
EXTRA_SOS_LD_FLAGS += -L$(shell pwd)/$(WORKSRC)/wand/.libs

MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/lib.*\.la
EXTRA_MERGE_EXCLUDE_FILES = .*/perllocal.pod

STRIP_LIBTOOL=1

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)

post-install-isa-sparcv8:
	@ln -s ImageMagick-$(VERSION) $(INSTALLISADIR)$(docdir)/ImageMagick
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.2.9.s.tar.bz2 |tar xf -)
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.5.2.s.tar.bz2 |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)

post-install-isa-i386:
	@ln -s ImageMagick-$(VERSION) $(INSTALLISADIR)$(docdir)/ImageMagick
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.2.9.i.tar.bz2 |tar xf -)
	@( cd $(INSTALLISADIR)$(libdir) ; bzip2 -dc $(CURDIR)/$(FILEDIR)/6.5.2.i.tar.bz2 |tar xf -)
	@mv $(INSTALLISADIR)$(mandir)/man1/compare.1 $(INSTALLISADIR)$(mandir)/man1/compare2.1
	@mv $(INSTALLISADIR)$(bindir)/compare $(INSTALLISADIR)$(bindir)/compare2
	@$(MAKECOOKIE)
