GARNAME = gstplugins_bad
GARVERSION = 0.10.17
CATEGORIES = gnome

DESCRIPTION = GStreamer plugins (Bad)
define BLURB
  GStreamer Bad Plug-ins is a set of plug-ins that aren't up to par compared 
  to the rest. They might be close to being good quality, but they're 
  missing something - be it a good code review, some documentation, a set 
  of tests, a real live maintainer, or some actual wide use. 
endef

MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-bad/
SRCNAME = gst-plugins-bad
DISTFILES  = $(SRCNAME)-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(SRCNAME)-$(GARVERSION)
PACKAGES = CSWgstpluginsbad
CATALOGNAME = gstplugins_bad

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_DEP_PKGS += CSWzlib CSWsunmath CSWneon CSWmesa CSWlibxml2 CSWlibsdl
BUILD_DEP_PKGS += CSWiconv CSWgstreamer CSWgstplugins CSWglib2 CSWggettext
BUILD_DEP_PKGS += CSWbzip2 CSWfaac CSWfaad2 CSWggettextrt CSWjasper CSWliboil
RUNTIME_DEP_PKGS = $(BUILD_DEP_PKGS)

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

LICENSE = $(WORKDIR_FIRSTMOD)/$(SRCNAME)-$(GARVERSION)/COPYING

PATCHFILES = patch-gstvideomeasure_collector.h patch-gstvideomeasure_ssim.h

# we provide that symbol
CHECKPKG_OVERRIDES_CSWgstpluginsbad += symbol-not-found|libgstcamerabin.so

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
