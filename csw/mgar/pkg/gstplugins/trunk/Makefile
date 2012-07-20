NAME = gst-plugins-base
VERSION = 0.10.29
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

PACKAGING_PLATFORMS = Solaris10-sparc Solaris10-i386
GARCOMPILER = SOS12U3

BUILD_DEP_PKGS += CSWpkgconfig CSWgstreamer-dev CSWliboildevel CSWlibglib2-dev 
BUILD_DEP_PKGS += CSWgnomevfs2-dev CSWlibogg-dev CSWlibgtk2-dev CSWlibatk-dev
BUILD_DEP_PKGS += CSWlibgconf-dev CSWggettextrt CSWlibxml2-dev CSWlibz-dev
BUILD_DEP_PKGS += CSWlibtheora-dev
BUILD_DEP_PKGS += CSWlibice CSWlibx11 CSWlibxvdevel CSWx11videoproto
BUILD_DEP_PKGS += CSWlibsm CSWlibxext
BUILD_DEP_PKGS += CSWlibvorbis-dev CSWpangodevel CSWlibpixman-dev 
BUILD_DEP_PKGS += CSWfconfig-dev CSWlibpng-dev CSWx11xproto CSWx11renderproto 
BUILD_DEP_PKGS += CSWlibx11devel CSWlibxcbdevel CSWlibxaudevel CSWlibxdmcpdevel

PATCHFILES += 0001-Makefile.in.patch
REINPLACE_USRSHARE += docs/plugins/html/*.html docs/libs/html/*.html

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --disable-alsa
CONFIGURE_ARGS += --disable-cdparanoia
# CONFIGURE_ARGS += --disable-xvideo
CONFIGURE_ARGS += --disable-gst_v4l
CONFIGURE_ARGS += --disable-libvisual
# CONFIGURE_ARGS += --disable-pango
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

include gar/category.mk

# I want see whats going on
AM_DEFAULT_VERBOSITY:=1

# sigh, portable code?
# post-configure-modulated:
# 	gsed -i 's/\(LIBS = -lnsl -lsocket\)/\1 -lresolv/' \
# 		$(WORKSRC)/gst/tcp/Makefile
# 	gsed -i 's/\(giosrc_mounting_LDFLAGS =\)/\1 $$(X_LIBS)/' \
# 		$(WORKSRC)/tests/examples/gio/Makefile
# 	gsed -i 's/\(volume_LDFLAGS =\)/\1 $$(X_LIBS)/' \
#  		$(WORKSRC)/tests/examples/volume/Makefile
