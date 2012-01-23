NAME = libnotify
VERSION = 0.4.5
CATEGORIES = gnome

DESCRIPTION = Notification library of the Galago desktop presence framework
define BLURB
endef

MASTER_SITES = http://www.galago-project.org/files/releases/source/libnotify/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibnotify CSWlibnotifydevel

CATALOGNAME_CSWlibnotify      = libnotify
CATALOGNAME_CSWlibnotifydevel = libnotify_devel

SPKG_DESC_CSWlibnotify = $(DESCRIPTION)
SPKG_DESC_CSWlibnotifydevel = Development files for libnotify

VENDOR_URL = http://www.galago-project.org

BUILD_DEP_PKGS = CSWglib2devel CSWgtk2devel CSWpangodevel

RUNTIME_DEP_PKGS_CSWlibnotify  = CSWdbusglib CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2
RUNTIME_DEP_PKGS_CSWlibnotify += CSWlibatk CSWlibcairo CSWlibdbus CSWpango

RUNTIME_DEP_PKGS_CSWlibnotifydevel = CSWlibnotify CSWglib2devel CSWgtk2devel CSWpangodevel

EXTRA_INC = $(libdir_install)/dbus-1.0/include

# Enable when CSWdbusglib is done in 64 bit
BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibnotifydevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibnotifydevel += $(sharedstatedir)/gtk-doc/.*

CHECKPKG_OVERRIDES_CSWlibnotifydevel += surplus-dependency|CSWlibnotify
CHECKPKG_OVERRIDES_CSWlibnotifydevel += surplus-dependency|CSWglib2devel
CHECKPKG_OVERRIDES_CSWlibnotifydevel += surplus-dependency|CSWgtk2devel
CHECKPKG_OVERRIDES_CSWlibnotifydevel += surplus-dependency|CSWpangodevel

CHECKPKG_OVERRIDES_CSWlibnotify += soname-not-found|libmlib.so.2|is|needed|by|opt/csw/lib/amd64/libnotify.so.1.1.3
CHECKPKG_OVERRIDES_CSWlibnotify += soname-not-found|libmlib.so.2|is|needed|by|opt/csw/bin/amd64/notify-send


include gar/category.mk
