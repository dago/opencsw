NAME = imagemagick
VERSION = 6.6.0
GARSUBREV = 9
CATEGORIES = lib

DESCRIPTION = A comprehensive package supporting automated and interative manipulation of images
define BLURB
  ImageMagick is a robust collection of tools and libraries offered under a
  usage license to read, write, and manipulate an image in many image formats
  (over 89 major formats) including popular formats like TIFF, JPEG, PNG, PDF,
  PhotoCD, and GIF.
endef

MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/
DISTFILES  = ImageMagick-$(VERSION)-$(GARSUBREV).tar.bz2

DISTNAME = ImageMagick-$(VERSION)-$(GARSUBREV)

SPKG_SOURCEURL = http://www.imagemagick.org

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWimagemagick += CSWbzip2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWdjvulibrert
RUNTIME_DEP_PKGS_CSWimagemagick += CSWfconfig
RUNTIME_DEP_PKGS_CSWimagemagick += CSWftype2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWggettextrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWglib2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgraph5
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
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblqr
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibsm
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibtoolrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibx11
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxext
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxml2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWperl
RUNTIME_DEP_PKGS_CSWimagemagick += CSWpng
RUNTIME_DEP_PKGS_CSWimagemagick += CSWsunmath
RUNTIME_DEP_PKGS_CSWimagemagick += CSWtiff
RUNTIME_DEP_PKGS_CSWimagemagick += CSWzlib
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibintl3
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibintl8
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwmf
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibltdl7

# these should go when rsvg & xml fixed on unstable
CHECKPKG_OVERRIDES_CSWimagemagick += missing-dependency|CSWlibxml2-2
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWggettextrt
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibcairo
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibtoolrt
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibxml2
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibwmf

BUILD_DEP_PKGS += CSWdjvulibredevel
BUILD_DEP_PKGS += CSWgraphvizdevel
BUILD_DEP_PKGS += CSWilmbasedevel
BUILD_DEP_PKGS += CSWlcmsdevel
BUILD_DEP_PKGS += CSWlibcairodevel
BUILD_DEP_PKGS += CSWliblqrdevel
BUILD_DEP_PKGS += CSWlibwmfdevel
BUILD_DEP_PKGS += CSWopenexrdevel
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWimagemagick)

# I want to say something rude about libtool and the entire shared lib world!
# Hoping most of this will get fixed by uninstalling imagemagic during build.
CHECKPKG_OVERRIDES_CSWimagemagick += non-uniform-lib-versions-in-package|sonames=libMagick++.so.10,libMagick++.so.2,libMagick++.so.3,libMagick.so.10,libMagickCore.so.2,libMagickCore.so.3,libMagickWand.so.2,libMagickWand.so.3,libWand.so.10
CHECKPKG_OVERRIDES_CSWimagemagick += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libMagickCore.so
CHECKPKG_OVERRIDES_CSWimagemagick += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libMagickWand.so
CHECKPKG_OVERRIDES_CSWimagemagick += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libMagick++.so
CHECKPKG_OVERRIDES_CSWimagemagick += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libMagickCore.so
CHECKPKG_OVERRIDES_CSWimagemagick += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libMagickWand.so
CHECKPKG_OVERRIDES_CSWimagemagick += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libMagick++.so
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/lib/libMagick++.so.10.0.4
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/SUNWspro/lib/v8|opt/csw/lib/libMagick++.so.3.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/lib/libMagick++.so.3.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/SUNWspro/lib/rw7|opt/csw/lib/libMagick++.so.3.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/lib|opt/csw/lib/libMagick++.so.3.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/studio/SOS11/SUNWspro/lib/rw7|opt/csw/lib/libMagick++.so.2.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/studio/SOS11/SUNWspro/lib/v8|opt/csw/lib/libMagick++.so.2.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/studio/SOS11/SUNWspro/lib|opt/csw/lib/libMagick++.so.2.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/lib/libMagick++.so.2.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/SUNWspro/lib/v8|opt/csw/lib/libMagick++.so.2.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/lib|opt/csw/lib/libMagick++.so.2.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/studio/SOS8/SUNWspro/lib/rw7|opt/csw/lib/libMagick++.so.10.0.4
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/studio/SOS8/SUNWspro/lib/v8|opt/csw/lib/libMagick++.so.10.0.4
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/studio/SOS8/SUNWspro/lib|opt/csw/lib/libMagick++.so.10.0.4
CHECKPKG_OVERRIDES_CSWimagemagick += bad-rpath-entry|/opt/SUNWspro/lib/v8|opt/csw/lib/libMagick++.so.10.0.4

# pffft!  don't bug me!
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/ImageMagick-6.6.0/config/mime.xml
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/ImageMagick-6.6.0/ChangeLog
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/api/MagickCore/magick-config_8h-source.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/api/MagickCore/version_8h.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/perl-magick.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/api/MagickCore/magick-config_8h.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/resources.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/advanced-unix-installation.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/changelog.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/lib/libMagickCore.so.2.0.0
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ImageMagick/www/install-source.html
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/lib/libMagick.so.10.0.4
CHECKPKG_OVERRIDES_CSWimagemagick += file-with-bad-content|/usr/local|root/opt/csw/lib/libMagickCore.so.3.0.0

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = ImageMagick-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

CONFIGURE_ARGS_COMMON  = $(DIRPATHS)
CONFIGURE_ARGS_COMMON += --with-perl=$(bindir)/perl
CONFIGURE_ARGS_COMMON += --enable-shared --disable-static
CONFIGURE_ARGS_COMMON += --with-dps=yes
# Ghostscript lib is linked to Sun X11
CONFIGURE_ARGS_COMMON += --with-gslib=no
CONFIGURE_ARGS_COMMON += --x-includes=/opt/csw/X11/include
CONFIGURE_ARGS_COMMON += --x-libraries=/opt/csw/X11/lib 
# Solaris 8 and 9 doesn't have complex.h
CONFIGURE_ARGS_COMMON += --without-fftw
CONFIGURE_ARGS_COMMON += --with-modules=yes
# Let's try to use openmp and see what it does for performance
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
