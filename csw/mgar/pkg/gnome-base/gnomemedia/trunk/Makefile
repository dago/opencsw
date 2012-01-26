NAME = gnome-media
VERSION = 2.28.5
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Multimedia applications for the GNOME 2 desktop
define BLURB
  Multimedia applications for the GNOME 2.0 desktop.
  Includes gnome-cd, a CDDB aware CD player; gnome-volume-control, 
  for controlling the sound card's mixer; and VU-Meter
endef

MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/gnome-media/2.28/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PACKAGES = CSWgnomemedia
CATALOGNAME = gnomemedia

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS += CSWftype2 CSWgconf2 CSWggettextrt CSWglib2 CSWgstplugins
RUNTIME_DEP_PKGS += CSWgstreamer CSWgtk2 CSWlibatk CSWlibcairo CSWlibglade2
RUNTIME_DEP_PKGS += CSWlibxml2 CSWpango CSWfconfig
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS) CSWgtk2devel CSWlibxcbdevel CSWlibxcb
BUILD_DEP_PKGS += CSWlibpthreadstubs CSWlibxau CSWlibxaudevel CSWx11xproto
BUILD_DEP_PKGS += CSWx11renderproto CSWx11kbproto CSWgnomedocutils CSWpylibxml2
BUILD_DEP_PKGS += CSWscrollkeeper CSWintltool CSWlibxcbdevel CSWlibxdmcpdevel

CONFIGURE_ARGS += $(DIRPATHS)

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

ADD_X11_LIB = -L$(prefix)/X11/lib -R$(prefix)/X11/lib
EXTRA_LDFLAGS = -R $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk
post-configure-modulated:
	gsed -i 's,\tmsgfmt,\t$$(GMSGFMT),' $(WORKSRC)/profiles/help/Makefile
	gsed -i 's,\(LIBS =\),\1 -lm,' $(WORKSRC)/grecord/src/Makefile
	gsed -i 's,\tmsgfmt,\t$$(GMSGFMT),' $(WORKSRC)/grecord/doc/Makefile
	gsed -i 's,\tmsgfmt,\t$$(GMSGFMT),' $(WORKSRC)/gst-mixer/doc/Makefile
	gsed -i 's,\tmsgfmt,\t$$(GMSGFMT),' \
		$(WORKSRC)/gstreamer-properties/help/Makefile
	gsed -i 's,<getopt.h>,<unistd.h>,' $(WORKSRC)/gst-mixer/src/main.c
	@$(MAKECOOKIE)

pre-configure-modulated:
	# hack until we have fixed our libX11 issue...
	gsed -i 's,GMP_LIBS=$$pkg_cv_GMP_LIBS,GMP_LIBS="$(ADD_X11_LIB) $$pkg_cv_GMP_LIBS",' $(WORKSRC)/configure
	gsed -i 's,GSR_LIBS=$$pkg_cv_GSR_LIBS,GSR_LIBS="$(ADD_X11_LIB) $$pkg_cv_GSR_LIBS",' $(WORKSRC)/configure
	gsed -i 's,GSTMIXER_LIBS=$$pkg_cv_GSTMIXER_LIBS,GSTMIXER_LIBS="$(ADD_X11_LIB) $$pkg_cv_GSTMIXER_LIBS -lm",' $(WORKSRC)/configure
	@$(MAKECOOKIE)

pre-build-isa-sparcv8:
	# why ist sparc 32bit xsltproc broken? just cores...
	gsed -i 's,xsltproc,/opt/csw/bin/sparcv9/xsltproc,' $(WORKSRC)/grecord/doc/Makefile
	gsed -i 's,xsltproc,/opt/csw/bin/sparcv9/xsltproc,' $(WORKSRC)/gst-mixer/doc/Makefile
	gsed -i 's,xsltproc,/opt/csw/bin/sparcv9/xsltproc,' $(WORKSRC)/gstreamer-properties/help/Makefile
	gsed -i 's,xsltproc,/opt/csw/bin/sparcv9/xsltproc,' $(WORKSRC)/profiles/help/Makefile
