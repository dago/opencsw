NAME = gst-plugins-ugly
VERSION = 0.10.17
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

BUILD_DEP_PKGS += CSWgstreamer-dev
BUILD_DEP_PKGS += CSWgstplugins-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWlibdvdread-dev 
BUILD_DEP_PKGS += CSWlibid3tag
BUILD_DEP_PKGS += CSWlibmad-dev
BUILD_DEP_PKGS += CSWliboil
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWsunmath
BUILD_DEP_PKGS += CSWzlib
BUILD_DEP_PKGS += CSWliba52

GARCOMPILER = GCC4

PACKAGES = CSWgstplugins-ugly
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstrtp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstsdp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibdvdread4
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWliba52
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibx264-133
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstaudio0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstpbutils0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstriff0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibmad0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgsttag0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstrtsp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibgstvideo0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-ugly += CSWlibglib2-0-0

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
# CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
# CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

include gar/category.mk
