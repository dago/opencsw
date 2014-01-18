NAME      = imagemagick
VERSION   = 6.8.8
GARSUBREV = 2
GARTYPE   = v2

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

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GCC4

VENDOR_URL = http://www.imagemagick.org

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWliblcms-dev
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS += CSWlibwmf-dev
BUILD_DEP_PKGS += CSWliblzma-dev
BUILD_DEP_PKGS += CSWopenexr-dev
BUILD_DEP_PKGS += CSWlibwebp-dev
BUILD_DEP_PKGS += CSWlibfpx-dev
BUILD_DEP_PKGS += CSWlibdjvulibre-dev
BUILD_DEP_PKGS += CSWilmbase-dev
BUILD_DEP_PKGS += CSWliblqr-dev
BUILD_DEP_PKGS += CSWopenjpeg-dev
BUILD_DEP_PKGS += CSWlibrsvg-dev
BUILD_DEP_PKGS += CSWliblcms2-dev
BUILD_DEP_PKGS += CSWgraphviz-dev
BUILD_DEP_PKGS += CSWlibfftw-dev

PACKAGES += CSWlibmagickcore6q16hdri2
CATALOGNAME_CSWlibmagickcore6q16hdri2 = libmagickcore6q16hdri2
SPKG_DESC_CSWlibmagickcore6q16hdri2 += Library from ImageMagick, libMagickCore-6.Q16HDRI.so.2
PKGFILES_CSWlibmagickcore6q16hdri2 += $(call baseisadirs,$(libdir),libMagickCore-6\.Q16HDRI\.so\.2\.0\.0)
PKGFILES_CSWlibmagickcore6q16hdri2 += $(call baseisadirs,$(libdir),libMagickCore-6\.Q16HDRI\.so\.2(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibmagickcore6q16hdri2 += CSWlibmagickcore6q16hdri1

PACKAGES += CSWlibmagickwand6q16hdri2
CATALOGNAME_CSWlibmagickwand6q16hdri2 = libmagickwand6q16hdri2
SPKG_DESC_CSWlibmagickwand6q16hdri2 += Library from ImageMagick, libMagickWand-6.Q16HDRI.so.2
PKGFILES_CSWlibmagickwand6q16hdri2 += $(call baseisadirs,$(libdir),libMagickWand-6\.Q16HDRI\.so\.2\.0\.0)
PKGFILES_CSWlibmagickwand6q16hdri2 += $(call baseisadirs,$(libdir),libMagickWand-6\.Q16HDRI\.so\.2(\.\d+)*)
PKGFILES_CSWlibmagickwand6q16hdri2 += $(call baseisadirs,$(libdir),libMagickWand-6\.Q16HDRI\.so\.2\.0\.0)
PKGFILES_CSWlibmagickwand6q16hdri2 += $(call baseisadirs,$(libdir),libMagickWand-6\.Q16HDRI\.so\.2(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibmagickcore6q16hdri2
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibmagickwand6q16hdri2 += CSWlibmagickwand6q16hdri1

PACKAGES += CSWlibmagick++6q16hdri3
CATALOGNAME_CSWlibmagick++6q16hdri3 = libmagick++6q16hdri3
PKGFILES_CSWlibmagick++6q16hdri3 += $(call baseisadirs,$(libdir),libMagick\+\+-6\.Q16HDRI\.so\.3\.0\.0)
PKGFILES_CSWlibmagick++6q16hdri3 += $(call baseisadirs,$(libdir),libMagick\+\+-6\.Q16HDRI\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibmagick++6q16hdri3 += Library from ImageMagick, libMagick++-6.Q16HDRI.so.3
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibmagickcore6q16hdri2
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibmagickwand6q16hdri2
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibstdc++6
OBSOLETED_BY_CSWlibmagick++6q16hdri3 += CSWlibmagick++6q16hdri2

PACKAGES += CSWimagemagick-dev
SPKG_DESC_CSWimagemagick-dev = Development files for ImageMagick libraries
# In man3 there is just the manpage for the Perl module
PKGFILES_DEVEL_MAN3_MANPAGE =
PKGFILES_CSWimagemagick-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWimagemagick-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWimagemagick
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWlibmagickcore6q16hdri2
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWlibmagickwand6q16hdri2
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWlibmagick++6q16hdri3
RUNTIME_DEP_PKGS_CSWimagemagick-dev += CSWperl

PACKAGES += CSWimagemagick
SPKG_DESC_CSWimagemagick = A comprehensive package supporting automated and interative manipulation of images
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibmagickcore6q16hdri2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibmagickwand6q16hdri2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfpx1
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibz1
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibilmimf-imf2-0-20
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblzma5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwebp4
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibjbig2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibdjvulibre21
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibopenjp2-6
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgs9
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgvc6


### 
# Needed for the Solaris ld bug
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmagickcore6q16hdri2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibmagickwand6q16hdri2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibimath2-0-10
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibintl8
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibilmthread2-0-10
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibiex2-0-10
RUNTIME_DEP_PKGS_CSWimagemagick += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibhalf10
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWimagemagick += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWliblqr1-0
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWlibmagick++6q16hdri3 += CSWlibglib2-0-0
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibfftw3-3
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWliblqr1-0
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWliblcms2-2
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibglib2-0-0
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibltdl7
CHECKPKG_OVERRIDES_CSWlibmagick++6q16hdri3 += surplus-dependency|CSWlibgomp1
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibfftw3-3
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWliblqr1-0
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWliblcms2-2
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibglib2-0-0
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibmagickwand6q16hdri2 += surplus-dependency|CSWlibltdl7
CHECKPKG_OVERRIDES_CSWlibmagickcore6q16hdri2 += surplus-dependency|CSWlibglib2-0-0
CHECKPKG_OVERRIDES_CSWlibmagickcore6q16hdri2 += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibfftw3-3
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibhalf10
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibimath2-0-10
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWliblqr1-0
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWliblcms2-2
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibilmthread2-0-10
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibiex2-0-10
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibcdt5
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibltdl7
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWimagemagick += surplus-dependency|CSWlibgomp1
###

#PACKAGES += CSWpm-image-magick
#SPKG_DESC_CSWpm-image-magick = Image::Magick: Perl binding for Imagemagick
#PKGFILES_CSWpm-image-magick += $(libdir)/perl/.*
#PKGFILES_CSWpm-image-magick += $(mandir)/.*\.3perl

#RUNTIME_DEP_PKGS_CSWpm-image-magick += CSWperl
#RUNTIME_DEP_PKGS_CSWpm-image-magick += CSWlibmagickcore6q16hdri1

# No binary in that package, since no 64 bit perl
#CHECKPKG_OVERRIDES_CSWpm-image-magick += 64-bit-binaries-missing

REINPLACE_USRLOCAL += config/mime.xml

EXTRA_LINKER_FLAGS = -lsocket -lnsl
EXTRA_LD_OPTIONS = -z nolazyload

# We especially don't want ISALIST for the above /usr/openwin/lib
# This should be reworked after a general rework of ISALIST in GAR
RUNPATH_ISALIST = $(libpath_install)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared 
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-maintainer-mode

# This one causes the Q16HDR in the lib name
CONFIGURE_ARGS += --enable-hdri

# For some reason, on x86, DPS is only available as a 32 bit lib, and
# really, it's not the future anymore: drop it.
CONFIGURE_ARGS += --without-dps

CONFIGURE_ARGS += --with-modules=yes
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --with-wmf
CONFIGURE_ARGS += --with-rsvg
CONFIGURE_ARGS += --with-gvc
CONFIGURE_ARGS += --with-gslib
CONFIGURE_ARGS += --with-openjp2

# Disable perl completely until it's rebuilt with GCC
CONFIGURE_ARGS += --without-perl
#CONFIGURE_ARGS-32 += --with-perl=$(bindir)/perl
#CONFIGURE_ARGS-64 += --without-perl
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

# One test is failing:
#   FAIL: Magick++/tests/attributes.sh
# This has been reported upstream at
#   http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=18889
SKIPTEST ?= 1

BUILD64 = 1
ISAEXEC = 1

REINPLACEMENTS += gnuplot
REINPLACE_MATCH_gnuplot = /usr/local/bin/gnuplot
REINPLACE_WITH_gnuplot = $(bindir)/gnuplot
REINPLACE_FILES_gnuplot += magick/magic.c

# Only remove libtool files from the public lib directory, keep the private ones for libtool dlopn
MERGE_EXCLUDE_LIBTOOL ?= $(libdir)/lib.*\.la

EXTRA_MERGE_EXCLUDE_FILES += .*/perllocal.pod
EXTRA_MERGE_EXCLUDE_FILES += .*/\.packlist

EXTRA_PAX_ARGS += -s ',$(bindir)/compare,$(bindir)/compare-imagemagick,'
EXTRA_PAX_ARGS += -s ',$(mandir)/man1/compare\.1,$(mandir)/man1/compare-imagemagick.1,'

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(GARSUBREV)
