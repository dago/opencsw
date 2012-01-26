NAME = gstreamer
VERSION = 0.10.26
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Open source multimedia framework
define BLURB
  GStreamer is a library for constructing graphs of media-handling components.
  The applications it supports range from simple Ogg/Vorbis playback,
  audio/video streaming to complex audio (mixing) and video (non-linear
  editing) processing.
endef

PACKAGES = CSWgstreamer
CATALOGNAME = gstreamer

MASTER_SITES = http://gstreamer.freedesktop.org/src/gstreamer/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug

RUNTIME_DEP_PKGS += CSWglib2 CSWggettextrt CSWlibxml2
BUILD_DEP_PKGS   += CSWbison CSWflex-new CSWglib2devel CSWpkgconfig
BUILD_DEP_PKGS   += CSWlibxml2devel
BUILD_DEP_PKGS   += $(RUNTIME_DEP_PKGS)

STRIP_LIBTOOL = 1

# no tests..
TEST_SCRIPTS =

include gar/category.mk

# select the right flex parser aka CSWflex-new
CONFIGURE_ENV  += FLEX_PATH=/opt/csw/bin/flex-2.5.35
