GARNAME = euler
GARVERSION = 1.61.0
CATEGORIES = apps

DESCRIPTION = EULER interactive computing with real, complex numbers and matrices
define BLURB
  This is the GTK+ based version of EULER for Unix / Linux systems. It has been ported
  to GTK+ by Eric Boucharé (bouchare dot eric at wanadoo dot fr) on the base of Dr Ren
  Grothmann's X11 version. Euler was started by Dr Grothmann. He also maintains a version
  for Windows systems.

  EULER is a program for quickly and interactively computing with real and complex
  numbers and matrices, or with intervals, in the style of MatLab, Octave,...
  It can draw and animate your functions in two and three dimensions.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
PATCHFILES = 0001-Remove-static-setting-of-CFLAGS.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tz

REQUIRED_PKGS = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2
REQUIRED_PKGS += CSWlibatk CSWlibcairo CSWlibxext CSWpango
PREREQUISITE_PKGS = $(REQUIRED_PKGS)
PREREQUISITE_PKGS += CSWglib2devel CSWgtk2devel
PREREQUISITE_PKGS += CSWlibcairodevel CSWlibxextdevel CSWpangodevel

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

EXTRA_LDFLAGS = -lm /usr/openwin/lib/libXext.so

BUILD_OVERRIDE_DIRS = CFLAGS
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
