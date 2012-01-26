NAME = gst-plugins-bad
VERSION = 0.10.20
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
PACKAGES = CSWgstpluginsbad
CATALOGNAME = gstplugins_bad

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS += CSWlibxml2 CSWgtk2 CSWlibx11 CSWlibice CSWlibglade2 CSWlibsm
DEP_PKGS += CSWgstreamer CSWgstplugins CSWglib2 CSWpango CSWlibatk CSWlibcairo
DEP_PKGS += CSWbzip2 CSWfaac CSWfaad2 CSWggettextrt CSWjasper CSWliboil
DEP_PKGS += CSWfconfig CSWftype2

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

PATCHFILES = patch-gstvideomeasure_collector.h patch-gstvideomeasure_ssim.h

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
