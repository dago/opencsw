NAME = gstreamer
VERSION = 0.10.29
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
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = Solaris10-sparc Solaris10-i386

RUNTIME_DEP_PKGS += CSWglib2 CSWggettextrt CSWlibxml2
BUILD_DEP_PKGS   += CSWbison CSWflex-new CSWglib2devel CSWpkgconfig
BUILD_DEP_PKGS   += CSWlibxml2devel
BUILD_DEP_PKGS   += $(RUNTIME_DEP_PKGS)

STRIP_LIBTOOL = 1

PATCHFILES += 0001-gtk-doc.mak.patch
PATCHFILES += 0002-gtk-doc-plugins.mak.patch
PATCHFILES += 0003-Makefile.in.patch
PATCHFILES += 0004-Makefile.in.patch
PATCHFILES += 0005-Makefile.in.patch

# root/opt/csw/share/gtk-doc/html/gstreamer-0.10/gstreamer-GstBufferList.html
# ./docs/plugins/html ./docs/libs/html ./docs/gst/html
REINPLACE_USRSHARE += docs/plugins/html/*.html docs/libs/html/*.html docs/gst/html/*.html

 # REINPLACE_USRSHARE += $(prefix)/share/gtk-doc/html/gstreamer-plugins-0.10/.*
# REINPLACE_USRSHARE += $(prefix)/share/gtk-doc/html/gstreamer-libs-0.10/.*
# REINPLACE_USRSHARE += $(prefix)/share/gtk-doc/html/gstreamer-0.10/.*
# REINPLACE_WHEN_USRSHARE = postinstall

REINPLACE_USRLOCAL += $(prefix)/share/gtk-doc/html/gstreamer-0.10/gst-running.html
REINPLACE_USRLOCAL += $(mandir)/man1/gst-feedback-0.10.1
REINPLACE_USRLOCAL += $(bindir)/gst-feedback-0.10
REINPLACE_WHEN_USRLOCAL = postinstall


PACKAGES += CSWlibgstbase0-10-0
CATALOGNAME_CSWlibgstbase0-10-0 = libgstbase0_10_0
PKGFILES_CSWlibgstbase0-10-0 += $(call baseisadirs,$(libdir),libgstbase-0\.10\.so\.0\.25\.0)
PKGFILES_CSWlibgstbase0-10-0 += $(call baseisadirs,$(libdir),libgstbase-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstbase0-10-0 += $(DESCRIPTION), libgstbase-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstbase0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstbase0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstbase0-10-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgstbase0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstbase0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstbase0-10-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgstcheck0-10-0
CATALOGNAME_CSWlibgstcheck0-10-0 = libgstcheck0_10_0
PKGFILES_CSWlibgstcheck0-10-0 += $(call baseisadirs,$(libdir),libgstcheck-0\.10\.so\.0\.25\.0)
PKGFILES_CSWlibgstcheck0-10-0 += $(call baseisadirs,$(libdir),libgstcheck-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstcheck0-10-0 += $(DESCRIPTION), libgstcheck-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstcheck0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcheck0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcheck0-10-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgstcheck0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstcheck0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcheck0-10-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgstcontroller0-10-0
CATALOGNAME_CSWlibgstcontroller0-10-0 = libgstcontroller0_10_0
PKGFILES_CSWlibgstcontroller0-10-0 += $(call baseisadirs,$(libdir),libgstcontroller-0\.10\.so\.0\.25\.0)
PKGFILES_CSWlibgstcontroller0-10-0 += $(call baseisadirs,$(libdir),libgstcontroller-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstcontroller0-10-0 += $(DESCRIPTION), libgstcontroller-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstcontroller0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcontroller0-10-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgstcontroller0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstcontroller0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcontroller0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcontroller0-10-0 += CSWlibgthread2-0-0

PACKAGES += CSWlibgstdataprotocol0-10-0
CATALOGNAME_CSWlibgstdataprotocol0-10-0 = libgstdataprotocol0_10_0
PKGFILES_CSWlibgstdataprotocol0-10-0 += $(call baseisadirs,$(libdir),libgstdataprotocol-0\.10\.so\.0\.25\.0)
PKGFILES_CSWlibgstdataprotocol0-10-0 += $(call baseisadirs,$(libdir),libgstdataprotocol-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstdataprotocol0-10-0 += $(DESCRIPTION), libgstdataprotocol-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstdataprotocol0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstdataprotocol0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstdataprotocol0-10-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgstdataprotocol0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstdataprotocol0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstdataprotocol0-10-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgstnet0-10-0
CATALOGNAME_CSWlibgstnet0-10-0 = libgstnet0_10_0
PKGFILES_CSWlibgstnet0-10-0 += $(call baseisadirs,$(libdir),libgstnet-0\.10\.so\.0\.25\.0)
PKGFILES_CSWlibgstnet0-10-0 += $(call baseisadirs,$(libdir),libgstnet-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstnet0-10-0 += $(DESCRIPTION), libgstnet-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstnet0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstnet0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstnet0-10-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgstnet0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstnet0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstnet0-10-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgstreamer0-10-0
CATALOGNAME_CSWlibgstreamer0-10-0 = libgstreamer0_10_0
PKGFILES_CSWlibgstreamer0-10-0 += $(call baseisadirs,$(libdir),libgstreamer-0\.10\.so\.0\.25\.0)
PKGFILES_CSWlibgstreamer0-10-0 += $(call baseisadirs,$(libdir),libgstreamer-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstreamer0-10-0 += $(DESCRIPTION), libgstreamer-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstreamer0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstreamer0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstreamer0-10-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgstreamer0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstreamer0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstreamer0-10-0 += CSWlibxml2-2

PACKAGES += CSWgstreamer-dev
CATALOGNAME_CSWgstreamer-dev = gstreamer_dev
SPKG_DESC_CSWgstreamer-dev += $(DESCRIPTION), development files
PKGFILES_CSWgstreamer-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWgstreamer-dev += $(prefix)/share/gtk-doc/.*
RUNTIME_DEP_PKGS_CSWgstreamer-dev += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWgstreamer-dev += CSWlibgstnet0-10-0
RUNTIME_DEP_PKGS_CSWgstreamer-dev += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWgstreamer-dev += CSWlibgstdataprotocol0-10-0
RUNTIME_DEP_PKGS_CSWgstreamer-dev += CSWlibgstcontroller0-10-0
RUNTIME_DEP_PKGS_CSWgstreamer-dev += CSWlibgstcheck0-10-0

PACKAGES += CSWgstreamer
SPKG_DESC_CSWgstreamer += $(DESCRIPTION), base
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgstbase0-10-0
# RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgstdataprotocol0-10-0
# RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgstcontroller0-10-0
# RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgstnet0-10-0
# RUNTIME_DEP_PKGS_CSWgstreamer += CSWlibgstcheck0-10-0

# no tests..
TEST_SCRIPTS =

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug

include gar/category.mk

# remove -L/opt/csw/lib
LDFLAGS = $(strip $($(GARCOMPILER)_LD_FLAGS))

# select the right flex parser aka CSWflex-new
CONFIGURE_ENV  += FLEX_PATH=/opt/csw/bin/flex-2.5.35
