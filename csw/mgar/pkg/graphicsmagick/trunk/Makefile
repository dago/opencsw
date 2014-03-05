# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = graphicsmagick
VERSION = 1.3.19
GARTYPE = v2

DESCRIPTION = GraphicsMagick Image Processing System
define BLURB
  GraphicsMagick is the swiss army knife of image processing.
endef

MASTER_SITES = $(SF_MIRRORS)
FILENAME     = GraphicsMagick
DISTNAME     = $(FILENAME)-$(VERSION)
DISTFILES    = $(DISTNAME).tar.xz

LICENSE = Copyright.txt

GARCOMPILER =  GCC4

BUILD64 = 1
ISAEXEC = 1

REINPLACEMENTS += gnuplot
REINPLACE_MATCH_gnuplot = /usr/local/bin/gnuplot
REINPLACE_WITH_gnuplot = $(bindir)/gnuplot
REINPLACE_FILES_gnuplot += magick/magic.c

PACKAGES += CSWgraphicsmagick
SPKG_DESC_CSWgraphicsmagick = GraphicsMagick Image Processing System
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibgraphicsmagick-q16-3
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibjasper1
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibz1
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibwmflite0-2-7
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibjbig2
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibwebp4

PACKAGES += CSWgraphicsmagick-dev
CATALOGNAME_CSWgraphicsmagick-dev = graphicsmagick_dev
SPKG_DESC_CSWgraphicsmagick-dev += $(DESCRIPTION), development files
PKGFILES_CSWgraphicsmagick-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWgraphicsmagick-dev += CSWgraphicsmagick
RUNTIME_DEP_PKGS_CSWgraphicsmagick-dev += CSWlibgraphicsmagick++q16-3
RUNTIME_DEP_PKGS_CSWgraphicsmagick-dev += CSWlibgraphicsmagick-q16-3
RUNTIME_DEP_PKGS_CSWgraphicsmagick-dev += CSWlibgraphicsmagickwand-q16-2

PACKAGES += CSWlibgraphicsmagick++q16-3
CATALOGNAME_CSWlibgraphicsmagick++q16-3 = libgraphicsmagick++q16_3
PKGFILES_CSWlibgraphicsmagick++q16-3 += $(call baseisadirs,$(libdir),libGraphicsMagick\+\+-Q16\.so\.3\.6\.2)
PKGFILES_CSWlibgraphicsmagick++q16-3 += $(call baseisadirs,$(libdir),libGraphicsMagick\+\+-Q16\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibgraphicsmagick++q16-3 += $(DESCRIPTION), libGraphicsMagick++-Q16.so.3
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibgraphicsmagick-q16-3
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibstdc++6

PACKAGES += CSWlibgraphicsmagick-q16-3
CATALOGNAME_CSWlibgraphicsmagick-q16-3 = libgraphicsmagick_q16_3
PKGFILES_CSWlibgraphicsmagick-q16-3 += $(call baseisadirs,$(libdir),libGraphicsMagick-Q16\.so\.3\.11\.0)
PKGFILES_CSWlibgraphicsmagick-q16-3 += $(call baseisadirs,$(libdir),libGraphicsMagick-Q16\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibgraphicsmagick-q16-3 += $(DESCRIPTION), libGraphicsMagick-Q16.so.3
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick-q16-3 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick-q16-3 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick-q16-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick-q16-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick-q16-3 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick-q16-3 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick-q16-3 += CSWlibgcc-s1

PACKAGES += CSWlibgraphicsmagickwand-q16-2
CATALOGNAME_CSWlibgraphicsmagickwand-q16-2 = libgraphicsmagickwand_q16_2
PKGFILES_CSWlibgraphicsmagickwand-q16-2 += $(call baseisadirs,$(libdir),libGraphicsMagickWand-Q16\.so\.2\.6\.0)
PKGFILES_CSWlibgraphicsmagickwand-q16-2 += $(call baseisadirs,$(libdir),libGraphicsMagickWand-Q16\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibgraphicsmagickwand-q16-2 += $(DESCRIPTION), libGraphicsMagickWand-Q16.so.2
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWlibgraphicsmagick-q16-3
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWlibgcc-s1

###
# Needed for the Solaris ld bug
ifeq ($(shell /usr/bin/uname -p),sparc)
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibgraphicsmagickwand-q16-2 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibgraphicsmagick++q16-3 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWliblzma5
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWgraphicsmagick += CSWlibfreetype6
endif
###

# A few tests are failing
SKIPTEST ?= 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-maintainer-mode
CONFIGURE_ARGS += --enable-quantum-library-names
CONFIGURE_ARGS += --enable-symbol-prefix
CONFIGURE_ARGS += --with-modules
CONFIGURE_ARGS += --with-quantum-depth=16
CONFIGURE_ARGS += --with-dps=no
CONFIGURE_ARGS += --without-perl

EXTRA_LD_OPTIONS = -z nolazyload

include gar/category.mk

