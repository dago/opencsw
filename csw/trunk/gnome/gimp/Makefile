GARNAME = gimp
CATEGORIES = gnome

DESCRIPTION = The GNU Image Manipulation Program.
define BLURB
	The GIMP is the GNU Image Manipulation Program. It is a freely distributed
	piece of software suitable for such tasks as photo retouching, image
	composition and image authoring. It can be used as a simple paint program,
	an expert quality photo retouching program, an online batch processing
	system, a mass production image renderer, a image format converter, etc.
endef

# v2.0+ requires Glib/Gtk+ >= 2.2.0
BUILD_V20 = 1

ifeq ($(BUILD_V20),1)
GARVERSION = 2.0.1
MASTER_SITES = ftp://ftp.gimp.org/pub/gimp/v2.0/
else
GARVERSION = 1.2.5
MASTER_SITES = ftp://ftp.gimp.org/pub/gimp/v1.2/v$(GARVERSION)/
endif

DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-print
CONFIGURE_ARGS += --enable-perl=$(PERL)

ifeq ($(BUILD_V20),1)
CONFIGURE_ARGS += --disable-devel-docs
CONFIGURE_ARGS += --without-aa
# This requires pygtk
#CONFIGURE_ARGS += --enable-python
endif

# Use this instead of EXTRA_LIB/EXTRA_INC
LIBJPEG = -I/usr/sfw/include -L/usr/sfw/lib -ljpeg
LIBTIFF = -I/usr/sfw/include -L/usr/sfw/lib -ltiff -ljpeg -lz
LIBPNG  = -I/usr/sfw/include -L/usr/sfw/lib -lpng12 -lz -lm
export LIBTIFF LIBJPEG LIBPNG

# Tests don't quite work properly
TEST_SCRIPTS =
TEST_TARGET = check

include ../category.mk
