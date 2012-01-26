NAME = gst-plugins-base
VERSION = 0.10.26
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Base GStreamer plugins handling various media types
define BLURB
  GStreamer Base Plug-ins is a well-groomed and well-maintained collection 
  of GStreamer plug-ins and elements, spanning the range of possible types 
  of elements one would want to write for GStreamer. It also contains helper 
  libraries and base classes useful for writing elements. A wide range of 
  video and audio decoders, encoders, and filters are included. 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-base/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWgstplugins
CATALOGNAME = gstplugins

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS += CSWgstreamer CSWliboil CSWglib2 CSWgnomevfs2 CSWlibogg
DEP_PKGS += CSWgconf2 CSWggettextrt CSWlibxml2 CSWtheora CSWvorbis
DEP_PKGS += CSWlibice CSWlibx11 CSWlibsm CSWlibxext

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --disable-alsa
CONFIGURE_ARGS += --disable-cdparanoia
CONFIGURE_ARGS += --disable-xvideo
CONFIGURE_ARGS += --disable-gst_v4l
CONFIGURE_ARGS += --disable-libvisual
CONFIGURE_ARGS += --disable-pango
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

include gar/category.mk

# sigh, portable code?
post-configure-modulated:
	gsed -i 's/\(LIBS = -lnsl -lsocket\)/\1 -lresolv/' \
		$(WORKSRC)/gst/tcp/Makefile
	gsed -i 's/\(giosrc_mounting_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/gio/Makefile
	gsed -i 's/\(volume_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/volume/Makefile
