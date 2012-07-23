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

PACKAGES = CSWgstplugins
CATALOGNAME = gstplugins
SPKG_DESC_CSWgstplugins += $(DESCRIPTION), base
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibice
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWliboil
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstdataprotocol0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibxext
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibsm
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibx11
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibogg0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibxv
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWpango
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstcontroller0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgsttag0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstvideo0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstriff0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstpbutils0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstinterfaces0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstaudio0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins += CSWlibgstapp0-10-0

PACKAGES += CSWlibgstapp0-10-0
CATALOGNAME_CSWlibgstapp0-10-0 = libgstapp0_10_0
PKGFILES_CSWlibgstapp0-10-0 += $(call baseisadirs,$(libdir),libgstapp-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstapp0-10-0 += $(call baseisadirs,$(libdir),libgstapp-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstapp0-10-0 += $(DESCRIPTION), libgstapp-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstapp0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstapp0-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgstapp0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstapp0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstapp0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstapp0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstapp0-10-0 += CSWlibxml2-2


PACKAGES += CSWlibgstaudio0-10-0
CATALOGNAME_CSWlibgstaudio0-10-0 = libgstaudio0_10_0
PKGFILES_CSWlibgstaudio0-10-0 += $(call baseisadirs,$(libdir),libgstaudio-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstaudio0-10-0 += $(call baseisadirs,$(libdir),libgstaudio-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstaudio0-10-0 += $(DESCRIPTION), libgstaudio-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgstaudio0-10-0 += CSWlibgstinterfaces0-10-0

PACKAGES += CSWlibgstcdda0-10-0
CATALOGNAME_CSWlibgstcdda0-10-0 = libgstcdda0_10_0
PKGFILES_CSWlibgstcdda0-10-0 += $(call baseisadirs,$(libdir),libgstcdda-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstcdda0-10-0 += $(call baseisadirs,$(libdir),libgstcdda-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstcdda0-10-0 += $(DESCRIPTION), libgstcdda-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibgsttag0-10-0
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgstcdda0-10-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgstfft0-10-0
CATALOGNAME_CSWlibgstfft0-10-0 = libgstfft0_10_0
PKGFILES_CSWlibgstfft0-10-0 += $(call baseisadirs,$(libdir),libgstfft-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstfft0-10-0 += $(call baseisadirs,$(libdir),libgstfft-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstfft0-10-0 += $(DESCRIPTION), libgstfft-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstfft0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstfft0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstfft0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstfft0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstfft0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstfft0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgstinterfaces0-10-0
CATALOGNAME_CSWlibgstinterfaces0-10-0 = libgstinterfaces0_10_0
PKGFILES_CSWlibgstinterfaces0-10-0 += $(call baseisadirs,$(libdir),libgstinterfaces-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstinterfaces0-10-0 += $(call baseisadirs,$(libdir),libgstinterfaces-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstinterfaces0-10-0 += $(DESCRIPTION), libgstinterfaces-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstinterfaces0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstinterfaces0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstinterfaces0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstinterfaces0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstinterfaces0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstinterfaces0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgstnetbuffer0-10-0
CATALOGNAME_CSWlibgstnetbuffer0-10-0 = libgstnetbuffer0_10_0
PKGFILES_CSWlibgstnetbuffer0-10-0 += $(call baseisadirs,$(libdir),libgstnetbuffer-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstnetbuffer0-10-0 += $(call baseisadirs,$(libdir),libgstnetbuffer-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstnetbuffer0-10-0 += $(DESCRIPTION), libgstnetbuffer-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstnetbuffer0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstnetbuffer0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstnetbuffer0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstnetbuffer0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstnetbuffer0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstnetbuffer0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgstpbutils0-10-0
CATALOGNAME_CSWlibgstpbutils0-10-0 = libgstpbutils0_10_0
PKGFILES_CSWlibgstpbutils0-10-0 += $(call baseisadirs,$(libdir),libgstpbutils-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstpbutils0-10-0 += $(call baseisadirs,$(libdir),libgstpbutils-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstpbutils0-10-0 += $(DESCRIPTION), libgstpbutils-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstpbutils0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstpbutils0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstpbutils0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstpbutils0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstpbutils0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstpbutils0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgstriff0-10-0
CATALOGNAME_CSWlibgstriff0-10-0 = libgstriff0_10_0
PKGFILES_CSWlibgstriff0-10-0 += $(call baseisadirs,$(libdir),libgstriff-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstriff0-10-0 += $(call baseisadirs,$(libdir),libgstriff-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstriff0-10-0 += $(DESCRIPTION), libgstriff-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibgsttag0-10-0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibgstaudio0-10-0
RUNTIME_DEP_PKGS_CSWlibgstriff0-10-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgstrtp0-10-0
CATALOGNAME_CSWlibgstrtp0-10-0 = libgstrtp0_10_0
PKGFILES_CSWlibgstrtp0-10-0 += $(call baseisadirs,$(libdir),libgstrtp-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstrtp0-10-0 += $(call baseisadirs,$(libdir),libgstrtp-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstrtp0-10-0 += $(DESCRIPTION), libgstrtp-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstrtp0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtp0-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgstrtp0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtp0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstrtp0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtp0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtp0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgstrtsp0-10-0
CATALOGNAME_CSWlibgstrtsp0-10-0 = libgstrtsp0_10_0
PKGFILES_CSWlibgstrtsp0-10-0 += $(call baseisadirs,$(libdir),libgstrtsp-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstrtsp0-10-0 += $(call baseisadirs,$(libdir),libgstrtsp-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstrtsp0-10-0 += $(DESCRIPTION), libgstrtsp-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstrtsp0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtsp0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtsp0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstrtsp0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtsp0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstrtsp0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgstsdp0-10-0
CATALOGNAME_CSWlibgstsdp0-10-0 = libgstsdp0_10_0
PKGFILES_CSWlibgstsdp0-10-0 += $(call baseisadirs,$(libdir),libgstsdp-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstsdp0-10-0 += $(call baseisadirs,$(libdir),libgstsdp-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstsdp0-10-0 += $(DESCRIPTION), libgstsdp-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstsdp0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstsdp0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstsdp0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstsdp0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstsdp0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstsdp0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgsttag0-10-0
CATALOGNAME_CSWlibgsttag0-10-0 = libgsttag0_10_0
PKGFILES_CSWlibgsttag0-10-0 += $(call baseisadirs,$(libdir),libgsttag-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgsttag0-10-0 += $(call baseisadirs,$(libdir),libgsttag-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgsttag0-10-0 += $(DESCRIPTION), libgsttag-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgsttag0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgsttag0-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgsttag0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgsttag0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgsttag0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgsttag0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgsttag0-10-0 += CSWlibxml2-2

PACKAGES += CSWlibgstvideo0-10-0
CATALOGNAME_CSWlibgstvideo0-10-0 = libgstvideo0_10_0
PKGFILES_CSWlibgstvideo0-10-0 += $(call baseisadirs,$(libdir),libgstvideo-0\.10\.so\.0\.20\.0)
PKGFILES_CSWlibgstvideo0-10-0 += $(call baseisadirs,$(libdir),libgstvideo-0\.10\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgstvideo0-10-0 += $(DESCRIPTION), libgstvideo-0.10.so.0
RUNTIME_DEP_PKGS_CSWlibgstvideo0-10-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgstvideo0-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgstvideo0-10-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgstvideo0-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstvideo0-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstvideo0-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstvideo0-10-0 += CSWlibxml2-2

PACKAGES += CSWgstplugins-dev
CATALOGNAME_CSWgstplugins-dev = gstplugins_dev
SPKG_DESC_CSWgstplugins-dev += $(DESCRIPTION), development files
PKGFILES_CSWgstplugins-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWgstplugins-dev += $(prefix)/share/docs/plugins/html/*.html 
PKGFILES_CSWgstplugins-dev += $(prefix)/share/docs/libs/html/*.html
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstsdp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstriff0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstcdda0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstnetbuffer0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstfft0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstinterfaces0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstpbutils0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstrtp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgsttag0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstvideo0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstrtsp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstapp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-dev += CSWlibgstaudio0-10-0

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
