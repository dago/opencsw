GARNAME = libnotify
GARVERSION = 0.4.5
CATEGORIES = gnome

DESCRIPTION = Notification library of the Galago desktop presence framework
define BLURB
endef

MASTER_SITES = http://www.galago-project.org/files/releases/source/libnotify/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibnotify CSWlibnotifydevel

CATALOGNAME_CSWlibnotify      = libnotify
CATALOGNAME_CSWlibnotifydevel = libnotify_devel

SPKG_DESC_CSWlibnotify = $(DESCRIPTION)
SPKG_DESC_CSWlibnotifydevel = Development files for libnotify

VENDOR_URL = http://www.galago-project.org

BUILD_DEP_PKGS = CSWglib2devel CSWgtk2devel CSWpangodevel

RUNTIME_DEP_PKGS_CSWlibnotify  = CSWdbusglib CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2
RUNTIME_DEP_PKGS_CSWlibnotify += CSWlibatk CSWlibcairo CSWlibdbus CSWpango

RUNTIME_DEP_PKGS_CSWlibnotifydevel = CSWlibnotify

# Remove when move towards csw x11 has been finished
LARCH_sparcv9 = sparcv9
LARCH_amd64   = amd64
EXTRA_LINKER_FLAGS = /usr/openwin/lib/$(LARCH_$(ISA))/libXext.so

# Enable when libdbus is done in 64 bit
# BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

PKGFILES_CSWlibnotifydevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibnotifydevel += $(sharedstatedir)/gtk-doc/.*

include gar/category.mk
