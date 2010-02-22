GARNAME = gstreamer
GARVERSION = 0.10.26
CATEGORIES = gnome

DESCRIPTION = open source multimedia framework
define BLURB
  GStreamer is a library for constructing graphs of media-handling components.
  The applications it supports range from simple Ogg/Vorbis playback,
  audio/video streaming to complex audio (mixing) and video (non-linear
  editing) processing.
endef

PACKAGES = CSWgstreamer
CATALOGNAME = gstreamer

MASTER_SITES = http://gstreamer.freedesktop.org/src/gstreamer/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug

RUNTIME_DEP_PKGS = CSWglib2 CSWggettextrt CSWlibxml2
BUILD_DEP_PKGS = CSWbison CSWflex-new $(RUNTIME_DEP_PKGS)

STRIP_LIBTOOL = 1

CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|gst-inspect-0.10
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|gst-xmlinspect-0.10
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|gst-xmllaunch-0.10
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|gst-launch-0.10
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|gst-typefind-0.10
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|libgstbase-0.10.so.0.23.0
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|libgstcoreindexers.so
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|libgstcoreelements.so
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|libgstcheck-0.10.so.0.23.0
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|libgstdataprotocol-0.10.so.0.23.0
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|libgstcontroller-0.10.so.0.23.0
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|libgstnet-0.10.so.0.23.0
CHECKPKG_OVERRIDES_CSWgstreamer += symbol-not-found|gst-plugin-scanner

TEST_SCRIPTS =

include gar/category.mk
