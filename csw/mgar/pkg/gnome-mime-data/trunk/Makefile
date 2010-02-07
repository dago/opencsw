GARNAME = gnome-mime-data
GARVERSION = 2.18.0
CATEGORIES = gnome

DESCRIPTION = Library for writing single instance application
define BLURB
	Unique is a library for writing single instance application. If you launch
	a single instance application twice, the second instance will either just
	quit or will send a message to the running instance.

	Unique makes it easy to write this kind of applications, by providing a
	base class, taking care of all the IPC machinery needed to send messages
	to a running instance, and also handling the startup notification side. 
endef

GNOME_PROJ = gnome-mime-data
MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTNAME  = $(GNOME_PROJ)-$(GARVERSION)

PACKAGES = CSWgmimedata CSWgmimedatadevel CSWgmimedatadoc
CATALOGNAME_CSWgmimedata = gmimedata
CATALOGNAME_CSWgmimedatadevel = gmimedata_devel
CATALOGNAME_CSWgmimedatadoc = gmimedata_doc

SPKG_DESC_CSWgmimedata += Library for writing single instance application
SPKG_DESC_CSWgmimedatadevel += Library for writing single instance application - developer package
SPKG_DESC_CSWgmimedatadoc += Library for writing single instance application - documentation

#REQUIRED_PKGS_CSWgmimedata += CSWfconfig CSWftype2 CSWggettextrt CSWglib2
#REQUIRED_PKGS_CSWgmimedata += CSWgtk2 CSWlibatk CSWlibcairo CSWlibx11 CSWpango
#REQUIRED_PKGS_CSWgmimedata += CSWdbusglib CSWlibdbus CSWlibxext
REQUIRED_PKGS_CSWgmimedatadevel += CSWgmimedata
REQUIRED_PKGS_CSWgmimedatadoc += CSWgmimedata

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/gmimedata

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1

PKGFILES_CSWgmimedatadevel = $(PKGFILES_DEVEL)
PKGFILES_CSWgmimedatadoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgmimedatadoc = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
