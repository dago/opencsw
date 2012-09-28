# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tuxpaint
VERSION = 0.9.21
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Simple drwaing program
define BLURB
  Tux Paint is a free, award-winning drawing program for children ages 3 to 12 (for example, preschool and K-6). Tux Paint is used in schools around the world as a computer literacy drawing activity. It combines an easy-to-use interface, fun sound effects, and an encouraging cartoon mascot who guides children as they use the program.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = docs/COPYING.txt

GARCOMPILER = GCC4

REINPLACE_USRLOCAL +=  docs/* docs/*/* src/tuxpaint-import.sh src/tuxpaint.conf docs/*/html/*
REINPLACE_USRSHARE +=  docs/* docs/*/* docs/html/* docs/*/html/* fonts/locale/*/README.txt magic/docs/html/*
PATCHFILES += 0001-prefix-Makefile.patch

RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWpython
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibpaper
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWsdlttf
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWsdlimage
RUNTIME_DEP_PKGS_CSWtuxpaint += CSWsdlmixer

# cannot find any /usr/local in plugins!
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/alien.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/blocks_chalk_drip.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/blur.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/bricks.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/calligraphy.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/cartoon.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/confetti.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/distortion.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/emboss.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/fade_darken.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/fill.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/fisheye.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/flower.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/foam.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/fold.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/glasstile.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/grass.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/kalidescope.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/light.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/metalpaint.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/mirror_flip.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/mosaic.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/negative.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/noise.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/rails.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/rain.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/rainbow.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/realrainbow.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/ripples.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/rosette.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/sharpen.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/shift.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/smudge.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/snow.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/string.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/tint.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/toothpaste.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/tornado.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/tv.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/lib/tuxpaint/plugins/waves.so
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/share|root/opt/csw/bin/tuxpaint
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/share|root/opt/csw/share/doc/tuxpaint-dev/README.txt
CHECKPKG_OVERRIDES_CSWtuxpaint += file-with-bad-content|/usr/local|root/opt/csw/include/tuxpaint/tp_magic_api.h

CHECKPKG_OVERRIDES_CSWtuxpaint += gzipped-manpage-in-pkgmap|/opt/csw/share/man/man1/tp-magic-config.1.gz
CHECKPKG_OVERRIDES_CSWtuxpaint += gzipped-manpage-in-pkgmap|/opt/csw/share/man/man1/tuxpaint-import.1.gz
CHECKPKG_OVERRIDES_CSWtuxpaint += gzipped-manpage-in-pkgmap|/opt/csw/share/man/man1/tuxpaint.1.gz


EXTRA_LINKER_FLAGS = -lpng12 -lsocket
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
SKIPTEST = 1

BUILD_ARGS += PREFIX=$(prefix) SOL_LDFLAGS="$(EXTRA_LINKER_FLAGS)"

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
