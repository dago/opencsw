NAME = gst-plugins-ugly
VERSION = 0.10.13
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GStreamer plugins (Ugly)
define BLURB
  GStreamer Ugly Plug-ins is a set of plug-ins that have good quality and 
  correct functionality, but distributing them might pose problems. 
  The license on either the plug-ins or the supporting libraries might not 
  be how we'd like. The code might be widely known to present patent problems. 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-ugly/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PACKAGES = CSWgstpluginsugly
CATALOGNAME = gstplugins_ugly

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_DEP_PKGS += CSWgstreamer CSWgstplugins CSWglib2 CSWggettext CSWggettextrt
BUILD_DEP_PKGS += CSWlibdvdread CSWlibid3tag CSWlibmad CSWliboil CSWlibxml2
BUILD_DEP_PKGS += CSWsunmath CSWzlib CSWliba52
RUNTIME_DEP_PKGS = $(BUILD_DEP_PKGS)

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

include gar/category.mk
