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

REQUIRED_PKGS_CSWlibunique += CSWfconfig CSWftype2 CSWggettextrt CSWglib2
REQUIRED_PKGS_CSWlibunique += CSWgtk2 CSWlibatk CSWlibcairo CSWlibx11 CSWpango
REQUIRED_PKGS_CSWlibuniquedevel += CSWlibunique
REQUIRED_PKGS_CSWlibuniquedoc += CSWlibunique

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/LibUnique

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

#NO_ISAEXEC = 1
#NOISALIST = 1
#BUILD64 = 1

PKGFILES_CSWlibuniquedevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibuniquedoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibuniquedoc = 1

LIBS = -lsocket -lnsl
export LIBS

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
