NAME = libunique
VERSION = 1.1.6
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibunique CSWlibuniquedevel
CATALOGNAME_CSWlibunique = libunique
CATALOGNAME_CSWlibuniquedevel = libunique_devel

SPKG_DESC_CSWlibunique += Library for writing single instance application
SPKG_DESC_CSWlibuniquedevel += Library for writing single instance application - developer package

RUNTIME_DEP_PKGS_CSWlibunique += CSWfconfig CSWftype2 CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWlibunique += CSWgtk2 CSWlibatk CSWlibcairo CSWpango
RUNTIME_DEP_PKGS_CSWlibunique += CSWdbusglib CSWlibdbus
RUNTIME_DEP_PKGS_CSWlibuniquedevel += CSWlibunique CSWglib2devel CSWgtk2devel CSWlibatkdevel CSWlibcairodevel CSWpangodevel

BUILD_DEP_PKGS += CSWdbusglibdev

SPKG_SOURCEURL = http://live.gnome.org/LibUnique

NOISAEXEC = 1
NOISALIST = 1

# This needs to be fixed first before we can build 64 bit:
#   https://www.opencsw.org/mantis/view.php?id=4565
#BUILD64 = 1

EXTRA_LINKER_FLAGS = -lsocket -lnsl

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
# This needs a newer GTK, 2.18.x does not have it, reenable when GTK has been updated
CONFIGURE_ARGS += --enable-introspection=no

TEST_TARGET = check

ARCHALL_CSWlibuniquedoc = 1

PKGFILES_CSWlibuniquedevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibuniquedevel += $(sharedstatedir)/gtk-doc/.*

CHECKPKG_OVERRIDES_CSWlibuniquedevel += surplus-dependency|CSWlibunique
CHECKPKG_OVERRIDES_CSWlibuniquedevel += surplus-dependency|CSWlibcairodevel
CHECKPKG_OVERRIDES_CSWlibuniquedevel += surplus-dependency|CSWpangodevel
CHECKPKG_OVERRIDES_CSWlibuniquedevel += surplus-dependency|CSWlibatkdevel
CHECKPKG_OVERRIDES_CSWlibuniquedevel += surplus-dependency|CSWglib2devel
CHECKPKG_OVERRIDES_CSWlibuniquedevel += surplus-dependency|CSWgtk2devel

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
