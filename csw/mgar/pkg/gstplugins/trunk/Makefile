GARNAME = gstplugins
GARVERSION = 0.10.26
CATEGORIES = gnome

DESCRIPTION = an essential exemplary set of elements for gstreamer
define BLURB
  GStreamer Base Plug-ins is a well-groomed and well-maintained collection 
  of GStreamer plug-ins and elements, spanning the range of possible types 
  of elements one would want to write for GStreamer. It also contains helper 
  libraries and base classes useful for writing elements. A wide range of 
  video and audio decoders, encoders, and filters are included. 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-base/
SRCNAME = gst-plugins-base
DISTFILES  = $(SRCNAME)-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(SRCNAME)-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_DEP_PKGS += CSWgstreamer CSWliboil CSWglib2 CSWgnomevfs2 CSWlibogg
BUILD_DEP_PKGS += CSWgconf2 CSWggettextrt CSWlibxml2 CSWtheora CSWvorbis
RUNTIME_DEP_PKGS = $(BUILD_DEP_PKGS)

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --disable-alsa
CONFIGURE_ARGS += --disable-cdparanoia
CONFIGURE_ARGS += --disable-xvideo
CONFIGURE_ARGS += --disable-gst_v4l
CONFIGURE_ARGS += --disable-libvisual
CONFIGURE_ARGS += --disable-pango

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

LICENSE = $(WORKDIR_FIRSTMOD)/$(SRCNAME)-$(GARVERSION)/COPYING

# we are providing those symbols
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstaudio-0.10.so.0.19.0
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstriff-0.10.so.0.19.0
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstgnomevfs.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstapp.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstvolume.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstplaybin.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstogg.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstdecodebin.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstaudioconvert.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstadder.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgsttheora.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstdecodebin2.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstvideoscale.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstximagesink.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstvorbis.so
CHECKPKG_OVERRIDES_CSWgstplugins += symbol-not-found|libgstcdda-0.10.so.0.19.0

include gar/category.mk

# sigh, portable code?
post-configure-modulated:
	perl -pi -e 's/(LIBS = -lnsl -lsocket)/$$1 -lresolv/' \
		$(WORKSRC)/gst/tcp/Makefile
