NAME = gst-plugins-good
VERSION = 0.10.18
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GStreamer plugins (Good)
define BLURB
  GStreamer Good Plug-ins is a set of plug-ins that we consider to have 
  good quality code, correct functionality, our preferred license 
  (LGPL for the plug-in code, LGPL or LGPL-compatible for the supporting 
  library). 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-good/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWgstpluginsgood
CATALOGNAME = gstplugins_good

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS += CSWzlib CSWspeex CSWpng CSWlibice CSWlibx11 CSWgtk2 CSWvorbis
DEP_PKGS += CSWlibxml2 CSWliboil CSWlibcairo CSWjpeg CSWglib2 CSWgconf2
DEP_PKGS += CSWgstreamer CSWgstplugins CSWflac CSWesound CSWbzip2 CSWlibsm
DEP_PKGS += CSWggettextrt CSWlibogg CSWlibshout CSWtheora CSWlibxext

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))


STRIP_LIBTOOL = 1

TEST_SCRIPTS =

PATCHFILES = patch-matroska-demux.c

include gar/category.mk
post-configure-modulated:
	@# we do not have a hyperbolic tangent float function on solaris8,
	@# using hyperbolic tangent double instead
	perl -pi -e 's,tanhf,tanh,' \
		$(WORKSRC)/gst/replaygain/gstrglimiter.c
	@# [bus_message_cb]:ube: error: SIGNAL: Segmentation Fault
	@# <@Dagobert> Yes, try lowering the optimizer level from -xO3 down to
	@# -xO2 and may further down.
	perl -pi -e 's,xO3,xO1,' $(WORKSRC)/tests/icles/Makefile
	gsed -i 's/\(demo_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/equalizer/Makefile
	gsed -i 's/\(demo_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/spectrum/Makefile
	gsed -i 's/\(demo_osssrc_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/spectrum/Makefile
	gsed -i 's/\(demo_audiotest_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/spectrum/Makefile
	gsed -i 's/\(spectrum_example_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/spectrum/Makefile
