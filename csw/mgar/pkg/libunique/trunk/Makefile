GARNAME = libunique
GARVERSION = 1.1.6
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

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTNAME  = $(GARNAME)-$(GARVERSION)

PACKAGES = CSWlibunique CSWlibuniquedevel CSWlibuniquedoc
CATALOGNAME_CSWlibunique = libunique
CATALOGNAME_CSWlibuniquedevel = libunique_devel
CATALOGNAME_CSWlibuniquedoc = libunique_doc

SPKG_DESC_CSWlibunique += Library for writing single instance application
SPKG_DESC_CSWlibuniquedevel += Library for writing single instance application - developer package
SPKG_DESC_CSWlibuniquedoc += Library for writing single instance application - documentation

RUNTIME_DEP_PKGS_CSWlibunique += CSWfconfig CSWftype2 CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWlibunique += CSWgtk2 CSWlibatk CSWlibcairo CSWlibx11 CSWpango
RUNTIME_DEP_PKGS_CSWlibunique += CSWdbusglib CSWlibdbus CSWlibxext
RUNTIME_DEP_PKGS_CSWlibuniquedevel += CSWlibunique
RUNTIME_DEP_PKGS_CSWlibuniquedoc += CSWlibunique

BUILD_DEP_PKGS += CSWdbusglibdev

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/LibUnique

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#NOISAEXEC = 1
#NOISALIST = 1
# libdbus not 64-bit yet
#BUILD64 = 1

PKGFILES_CSWlibuniquedevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibuniquedoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibuniquedoc = 1

LIBS = -lsocket -lnsl
export LIBS

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
