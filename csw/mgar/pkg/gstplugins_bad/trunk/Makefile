NAME = gst-plugins-bad
VERSION = 0.10.21
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GStreamer plugins (Bad)
define BLURB
  GStreamer Bad Plug-ins is a set of plug-ins that aren't up to par compared 
  to the rest. They might be close to being good quality, but they're 
  missing something - be it a good code review, some documentation, a set 
  of tests, a real live maintainer, or some actual wide use. 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-bad/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PACKAGES = CSWgstplugins-bad

BUILD_DEP_PKGS += CSWlibxml2
BUILD_DEP_PKGS += CSWgtk2
BUILD_DEP_PKGS += CSWlibx11
BUILD_DEP_PKGS += CSWlibice
BUILD_DEP_PKGS += CSWlibglade2
BUILD_DEP_PKGS += CSWlibsm
BUILD_DEP_PKGS += CSWgstreamer
BUILD_DEP_PKGS += CSWgstplugins-dev
BUILD_DEP_PKGS += CSWglib2
BUILD_DEP_PKGS += CSWpango
BUILD_DEP_PKGS += CSWlibatk
BUILD_DEP_PKGS += CSWlibcairo
BUILD_DEP_PKGS += CSWbzip2
BUILD_DEP_PKGS += CSWfaac
BUILD_DEP_PKGS += CSWlibfaad-dev
BUILD_DEP_PKGS += CSWggettextrt
BUILD_DEP_PKGS += CSWjasper
BUILD_DEP_PKGS += CSWliboil
BUILD_DEP_PKGS += CSWfconfig
BUILD_DEP_PKGS += CSWftype2
BUILD_DEP_PKGS += CSWlibsndfile-dev

GARCOMPILER = GCC4

REINPLACE_USRLOCAL += gst/frei0r/gstfrei0r.c
REINPLACE_USRLOCAL += gst/real/gstreal.h

PACKAGES += CSWgstplugins-bad
SPKG_DESC_CSWgstplugins-bad += $(DESCRIPTION), base package
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstsdp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstinterfaces0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstrtp0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibfaad2
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibsndfile1
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgsttag0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWfaac
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstvideo0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstaudio0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstcontroller0-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgstplugins-bad += CSWlibgstpluginsbase-bad-10-0

PACKAGES += CSWlibgstpluginsbase-bad-10-0
CATALOGNAME_CSWlibgstpluginsbase-bad-10-0 = libgstpluginsbase_bad_10_0
SPKG_DESC_CSWlibgstpluginsbase-bad-10-0 += $(DESCRIPTION), base libs
PKGFILES_CSWlibgstpluginsbase-bad-10-0 += $(call baseisadirs,$(libdir),libgstbasevideo-0\.10\.so\.0\.0\.0)
PKGFILES_CSWlibgstpluginsbase-bad-10-0 += $(call baseisadirs,$(libdir),libgstbasevideo-0\.10\.so\.0(\.\d+)*)
PKGFILES_CSWlibgstpluginsbase-bad-10-0 += $(call baseisadirs,$(libdir),libgstphotography-0\.10\.so\.0\.0\.0)
PKGFILES_CSWlibgstpluginsbase-bad-10-0 += $(call baseisadirs,$(libdir),libgstphotography-0\.10\.so\.0(\.\d+)*)
PKGFILES_CSWlibgstpluginsbase-bad-10-0 += $(call baseisadirs,$(libdir),libgstsignalprocessor-0\.10\.so\.0\.0\.0)
PKGFILES_CSWlibgstpluginsbase-bad-10-0 += $(call baseisadirs,$(libdir),libgstsignalprocessor-0\.10\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgstpluginsbase-bad-10-0 += CSWlibgstbase0-10-0
RUNTIME_DEP_PKGS_CSWlibgstpluginsbase-bad-10-0 += CSWlibgstreamer0-10-0
RUNTIME_DEP_PKGS_CSWlibgstpluginsbase-bad-10-0 += CSWlibgstcontroller0-10-0
RUNTIME_DEP_PKGS_CSWlibgstpluginsbase-bad-10-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgstpluginsbase-bad-10-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgstpluginsbase-bad-10-0 += CSWlibgstvideo0-10-0
RUNTIME_DEP_PKGS_CSWlibgstpluginsbase-bad-10-0 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibgstpluginsbase-bad-10-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libgstbasevideo-0.10.so.0.0.0|soname=libgstbasevideo-0.10.so.0|pkgname=CSWlibgstpluginsbase-bad-10-0|expected=CSWlibgstbasevideo0-10-0
CHECKPKG_OVERRIDES_CSWlibgstpluginsbase-bad-10-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libgstphotography-0.10.so.0.0.0|soname=libgstphotography-0.10.so.0|pkgname=CSWlibgstpluginsbase-bad-10-0|expected=CSWlibgstphotography0-10-0
CHECKPKG_OVERRIDES_CSWlibgstpluginsbase-bad-10-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libgstsignalprocessor-0.10.so.0.0.0|soname=libgstsignalprocessor-0.10.so.0|pkgname=CSWlibgstpluginsbase-bad-10-0|expected=CSWlibgstsignalprocessor0-10-0

PACKAGES += CSWgstplugins-bad-dev
CATALOGNAME_CSWgstplugins-bad-dev = gstplugins_bad_dev
SPKG_DESC_CSWgstplugins-bad-dev += $(DESCRIPTION), development files
PKGFILES_CSWgstplugins-bad-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWgstplugins-bad-dev += CSWlibgstpluginsbase-bad-10-0
RUNTIME_DEP_PKGS_CSWgstplugins-bad-dev += CSWgstplugins-bad

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

PATCHFILES = patch-gstvideomeasure_collector.h patch-gstvideomeasure_ssim.h
# see: GStreamer (bugzilla.gnome.org) 
# [Bug 645053] shm: multiple compile failures on Solaris 10
PATCHFILES = 0001-fix-solaris10-compiler-errors.patch

include gar/category.mk

post-configure-modulated:
	perl -pi -e 's,(LIBS = -lnsl -lsocket),$$1 -lresolv,' \
		$(WORKSRC)/gst/dccp/Makefile
	perl -pi -e 's,#include <stdint.h>,,' \
		$(WORKSRC)/gst/dtmf/tone_detect.c
	perl -pi -e 's,powf,pow,' \
		$(WORKSRC)/gst/hdvparse/gsthdvparse.c
	perl -pi -e 's,(#include) "stdint.h",$$1 <sys/types.h>,' \
		$(WORKSRC)/gst/librfb/d3des.c
	perl -pi -e 's,(#include) "stdint.h",,' \
		$(WORKSRC)/gst/librfb/vncauth.c
	perl -pi -e 's,INADDR_NONE,~INADDR_ANY,' \
		$(WORKSRC)/gst/pcapparse/gstpcapparse.c
	perl -pi -e 's,(LIBS = -lnsl -lsocket),$$1 -lm,' \
		$(WORKSRC)/tests/examples/scaletempo/Makefile
	@# because of our legacy libXrender
	gsed -i 's/^\(LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/camerabin/Makefile
	gsed -i 's/\(mxfdemux_structure_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/mxf/Makefile
	gsed -i 's/\(scaletempo_demo_LDFLAGS =\)/\1 $$(X_LIBS)/' \
		$(WORKSRC)/tests/examples/scaletempo/Makefile
