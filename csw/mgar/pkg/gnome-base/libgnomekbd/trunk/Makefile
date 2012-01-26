NAME = libgnomekbd
VERSION = 2.28.2
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Package contains xkb hooks used by the GNOME desktop. 
define BLURB
  blubb
endef

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/libgnomekbd/2.28/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PACKAGES = CSWlibgnomekbd CSWlibgnomekbddevel
CATALOGNAME_CSWlibgnomekbd = libgnomekbd
CATALOGNAME_CSWlibgnomekbddevel = libgnomekbd_devel

SPKG_DESC_CSWlibgnomekbd = $(DESCRIPTION)
SPKG_DESC_CSWlibgnomekbddevel = $(DESCRIPTION) development files

PKGFILES_CSWlibgnomekbddevel = $(PKGFILES_DEVEL)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS += CSWdbusglib
RUNTIME_DEP_PKGS += CSWfconfig
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWgconf2
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWgtk2
RUNTIME_DEP_PKGS += CSWlibatk
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWlibdbus
RUNTIME_DEP_PKGS += CSWlibx11
RUNTIME_DEP_PKGS += CSWlibxklavier
RUNTIME_DEP_PKGS += CSWlibxml2
RUNTIME_DEP_PKGS += CSWpango

RUNTIME_DEP_PKGS_CSWlibgnomekbddevel += CSWlibgnomekbd

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWlibglade2
BUILD_DEP_PKGS += CSWgtk2devel
BUILD_DEP_PKGS += CSWlibxcb CSWlibxcbdevel
BUILD_DEP_PKGS += CSWlibpthreadstubs
BUILD_DEP_PKGS += CSWlibxau CSWlibxaudevel
BUILD_DEP_PKGS += CSWxproto
BUILD_DEP_PKGS += CSWlibxklavierdevel
BUILD_DEP_PKGS += CSWkbproto
BUILD_DEP_PKGS += CSWgnomedocutils
BUILD_DEP_PKGS += CSWscrollkeeper
BUILD_DEP_PKGS += CSWintltool
BUILD_DEP_PKGS += CSWgnulinks
BUILD_DEP_PKGS += CSWdbusglibdev
BUILD_DEP_PKGS += CSWlibdbusdev
BUILD_DEP_PKGS += CSWgtk2devel
BUILD_DEP_PKGS += CSWlibatkdevel

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib/$(MM_LIBDIR)

STRIP_LIBTOOL = 1

TEST_SCRIPTS =

EXTRA_LIB += /opt/csw/X11/lib

LICENSE = COPYING.LIB

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	# patch away GNUish
	gsed -i 's,-Wall,,' $(WORKSRC)/libgnomekbd/Makefile.in
	gsed -i 's,-Wall,,' $(WORKSRC)/capplet/Makefile.in
	gsed -i 's,-Wall,,' $(WORKSRC)/test/Makefile.in
	@$(MAKECOOKIE)

pre-build-modulated:
	# add math library
	gsed -i 's,^\(LDFLAGS = .*\)$$,\1 -lm,' $(WORKSRC)/libgnomekbd/Makefile
	# this is ugly, so is our X11 library problem....
	gsed -i 's,^\(CFLAGS = .*\)$$,\1 -L/opt/csw/X11/lib,' \
		$(WORKSRC)/test/Makefile
	@$(MAKECOOKIE)
