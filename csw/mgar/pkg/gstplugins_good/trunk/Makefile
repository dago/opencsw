GARNAME = gstplugins_good
GARVERSION = 0.10.18
CATEGORIES = gnome

DESCRIPTION = GStreamer plugins (Good)
define BLURB
  GStreamer Good Plug-ins is a set of plug-ins that we consider to have 
  good quality code, correct functionality, our preferred license 
  (LGPL for the plug-in code, LGPL or LGPL-compatible for the supporting 
  library). 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-good/
SRCNAME = gst-plugins-good
DISTFILES  = $(SRCNAME)-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(SRCNAME)-$(GARVERSION)
PACKAGES = CSWgstpluginsgood
CATALOGNAME = gstplugins_good

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_DEP_PKGS += CSWzlib CSWsunmath CSWspeex CSWpng CSWpango CSWorbit2
BUILD_DEP_PKGS += CSWlibxml2 CSWliboil CSWlibcairo CSWlibatk CSWjpeg CSWgtk2
BUILD_DEP_PKGS += CSWgstreamer CSWgstplugins CSWglib2 CSWggettext CSWgconf2
BUILD_DEP_PKGS += CSWflac CSWesound CSWaudiofile CSWaalib CSWbzip2
BUILD_DEP_PKGS += CSWggettextrt CSWlibogg CSWlibshout CSWncurses CSWtheora
BUILD_DEP_PKGS += CSWvorbis
RUNTIME_DEP_PKGS = $(BUILD_DEP_PKGS)

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

LICENSE = $(WORKDIR_FIRSTMOD)/$(SRCNAME)-$(GARVERSION)/COPYING

PATCHFILES = patch-matroska-demux.c

include gar/category.mk
post-configure-modulated:
	# we do not have a hyperbolic tangent float function on solaris8,
	# using hyperbolic tangent double instead
	perl -pi -e 's,tanhf,tanh,' \
		$(WORKSRC)/gst/replaygain/gstrglimiter.c
