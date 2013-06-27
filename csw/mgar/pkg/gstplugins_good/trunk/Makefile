NAME = gst-plugins-good
VERSION = 0.10.28
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GStreamer plugins (Good)
define BLURB
  GStreamer Good Plug-ins is a set of plug-ins that we consider to have 
  good quality code, correct functionality, our preferred license 
  (LGPL for the plug-in code, LGPL or LGPL-compatible for the supporting 
  library). 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-good/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWgstplugins-good
CATALOGNAME = gstplugins_good

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GCC4
PACKAGING_PLATFORMS += Solaris10-sparc Solaris10-i386

BUILD_DEP_PKGS += CSWgstreamer-dev CSWgstplugins-dev CSWlibflac-dev CSWesound 
BUILD_DEP_PKGS += CSWlibsmdevel CSWlibesd-dev CSWtaglib-devel CSWlibcairo-dev
BUILD_DEP_PKGS += CSWlibaudiofile-dev CSWlibjpeg-dev

PACKAGES = CSWgstplugins-good
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstsdp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstriff0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstinterfaces0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstrtp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstnetbuffer0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibx11
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibsoup-gnome2-4-1
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgsttag0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstrtsp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibz1
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstfft0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstpbutils0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstvideo0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstaudio0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibesd0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibxext
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibflac8
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgstcontroller0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgstplugins-good += CSWlibsoup2-4-1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)
CONFIGURE_ARGS += --disable-silent-rules

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

# PATCHFILES = patch-matroska-demux.c

# EXTRA_CFLAGS = -UHAVE_GCC_ASM 
BUILD_ARGS = CCAS=gcc

include gar/category.mk

# post-configure-modulated:
# 	@# we do not have a hyperbolic tangent float function on solaris8,
# 	@# using hyperbolic tangent double instead
# 	perl -pi -e 's,tanhf,tanh,' \
# 		$(WORKSRC)/gst/replaygain/gstrglimiter.c
# 	@# [bus_message_cb]:ube: error: SIGNAL: Segmentation Fault
# 	@# <@Dagobert> Yes, try lowering the optimizer level from -xO3 down to
# 	@# -xO2 and may further down.
# 	perl -pi -e 's,xO3,xO1,' $(WORKSRC)/tests/icles/Makefile
# 	gsed -i 's/\(demo_LDFLAGS =\)/\1 $$(X_LIBS)/' \
# 		$(WORKSRC)/tests/examples/equalizer/Makefile
# 	gsed -i 's/\(demo_LDFLAGS =\)/\1 $$(X_LIBS)/' \
# 		$(WORKSRC)/tests/examples/spectrum/Makefile
# 	gsed -i 's/\(demo_osssrc_LDFLAGS =\)/\1 $$(X_LIBS)/' \
# 		$(WORKSRC)/tests/examples/spectrum/Makefile
# 	gsed -i 's/\(demo_audiotest_LDFLAGS =\)/\1 $$(X_LIBS)/' \
# 		$(WORKSRC)/tests/examples/spectrum/Makefile
# 	gsed -i 's/\(spectrum_example_LDFLAGS =\)/\1 $$(X_LIBS)/' \
# 		$(WORKSRC)/tests/examples/spectrum/Makefile

PATH := $(PATH):/opt/csw/gcc4/bin/
