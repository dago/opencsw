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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
