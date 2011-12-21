NAME = imagemagick
VERSION = 6.7.3
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
DISTNAME = ImageMagick-$(VERSION)-$(GARSUBREV)
DISTFILES  = $(DISTNAME).tar.xz

PATCHFILES += 0001-Do-not-strip-norunpath.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Compilation breaks with internal error on SOS12 and SOS12U1
GARCOMPILER = SOS12U2

VENDOR_URL = http://www.imagemagick.org

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWdjvulibredevel
BUILD_DEP_PKGS += CSWgraphvizdevel
BUILD_DEP_PKGS += CSWilmbasedevel
BUILD_DEP_PKGS += CSWliblcms-dev
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS += CSWliblqrdevel
BUILD_DEP_PKGS += CSWlibwmf-dev
BUILD_DEP_PKGS += CSWliblzma-dev
BUILD_DEP_PKGS += CSWopenexrdevel
BUILD_DEP_PKGS += CSWlibwebp-dev
BUILD_DEP_PKGS += CSWlibfpx-dev

PACKAGES += CSWlibmagick++5
PKGFILES_CSWlibmagick++5 += $(call pkgfiles_lib,libMagick++.so.5)
SPKG_DESC_CSWlibmagick++5 += Library from ImageMagick, libMagick++.so.5
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibmagickcore5
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibmagickwand5
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWlibmagick++5 += CSWliblzma5

PACKAGES += CSWlibmagickcore5
PKGFILES_CSWlibmagickcore5 += $(call pkgfiles_lib,libMagickCore.so.5)
SPKG_DESC_CSWlibmagickcore5 += Library from ImageMagick, libMagickCore.so.5
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWlibmagickcore5 += CSWliblzma5

# Gnuplot is detected by the magic cookie #!/usr/local/bin/gnuplot
# XXX: Is this correct?
# CHECKPKG_OVERRIDES_CSWlibmagickcore5 += file-with-bad-content|/usr/local|root/opt/csw/lib/libMagickCore.so.5.0.0

PACKAGES += CSWlibmagickwand5
PKGFILES_CSWlibmagickwand5 += $(call pkgfiles_lib,libMagickWand.so.5)
SPKG_DESC_CSWlibmagickwand5 += Library from ImageMagick, libMagickWand.so.5
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibmagickcore5
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWlibmagickwand5 += CSWliblzma5

PACKAGES += CSWimagemagick-dev
SPKG_DESC_CSWimagemagick-dev = Development files for ImageMagick libraries
# In man3 there is just the manpage for the Perl module
PKGFILES_DEVEL_MAN3_MANPAGE =
PKGFILES_CSWimagemagick-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWimagemagick-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWlibmagick++5
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWlibmagickcore5
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWlibmagickwand5
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWperl
# This is all in /opt/csw/share/doc
CHECKPKG_OVERRIDES_CSWimagemagick-dev += file-with-bad-content

PACKAGES += CSWimagemagick
SPKG_DESC_CSWimagemagick = A comprehensive package supporting automated and interative manipulation of images
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibmagickcore5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibmagickwand5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWilmbase
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfpx1
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjasper
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibintl8
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWfconfig
RUNTIME_DEP_PKGS_CSWimagemagick += CSWjbigkit
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibz1
RUNTIME_DEP_PKGS_CSWimagemagick += CSWftype2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWimagemagick += CSWdjvulibrert
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgraph5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWpango
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwmf0-2-7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblzma5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwebp0

PACKAGES += CSWpm-image-magick
SPKG_DESC_CSWpm-image-magick = Image::Magick: Perl binding for Imagemagick
PKGFILES_CSWpm-image-magick += $(libdir)/perl/.*
PKGFILES_CSWpm-image-magick += $(mandir)/.*\.3perl

RUNTIME_DEP_PKGS_CSWpm-image-magick += CSWperl
RUNTIME_DEP_PKGS_CSWpm-image-magick += CSWlibmagickcore5

REINPLACE_USRLOCAL += config/mime.xml

REINPLACEMENTS += gnuplot
REINPLACE_MATCH_gnuplot = /usr/local/bin/gnuplot
REINPLACE_WITH_gnuplot = $(bindir)/gnuplot
REINPLACE_FILES_gnuplot += magick/magic.c

# This is part of ImageMagick and should be automatically adjusted during configure time
REINPLACEMENTS += display
REINPLACE_MATCH_display = /usr/local/bin/display
REINPLACE_WITH_display = $(bindir)/display
REINPLACE_FILES_display += magick/delegate.c

REINPLACEMENTS += nostdcpplib
REINPLACE_MATCH_nostdcpplib = -lstdc\+\+
REINPLACE_WITH_nostdcpplib =
REINPLACE_FILES_nostdcpplib = Makefile.in

EXTRA_LINKER_FLAGS = -norunpath

# This is for libdps, skipping this line makes the following tests fail:
#   FAIL: tests/validate-formats-on-disk.sh
#   FAIL: Magick++/tests/coderInfo.sh
EXTRA_LIB = /usr/openwin/lib

# We especially don't want ISALIST for the above /usr/openwin/lib
# This should be reworked after a general rework of ISALIST in GAR
RUNPATH_ISALIST = $(libpath_install)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static
CONFIGURE_ARGS += --enable-hdri
CONFIGURE_ARGS += --with-dps=yes

# Ghostscript lib is linked to Sun X11
# CONFIGURE_ARGS += --with-gslib=no

CONFIGURE_ARGS += --with-modules=yes
CONFIGURE_ARGS += --disable-silent-rules

# Until librsvg,graphviz and perl is 64bit
CONFIGURE_ARGS-32 += --with-perl=$(bindir)/perl
CONFIGURE_ARGS-64 += --without-gvc
CONFIGURE_ARGS-64 += --without-perl
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

# One test is failing:
#   FAIL: Magick++/tests/attributes.sh
# This has been reported upstream at
#   http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=18889
SKIPTEST ?= 1

BUILD64 = 1
ISAEXEC = 1

# Only remove libtool files from the public lib directory, keep the private ones for libtool dlopn
MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/lib.*\.la

EXTRA_MERGE_EXCLUDE_FILES += .*/perllocal.pod
EXTRA_MERGE_EXCLUDE_FILES += .*/\.packlist

EXTRA_PAX_ARGS += -s ',$(bindir)/compare,$(bindir)/compare-imagemagick,'
EXTRA_PAX_ARGS += -s ',$(mandir)/man1/compare\.1,$(mandir)/man1/compare-imagemagick.1,'

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)
