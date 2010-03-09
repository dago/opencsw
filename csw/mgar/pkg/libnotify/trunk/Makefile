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

VENDOR_URL = http://www.galago-project.org

# Remove when move towards csw x11 has been finished
LARCH_sparcv9 = sparcv9
LARCH_amd64   = amd64
EXTRA_LINKER_FLAGS = /usr/openwin/lib/$(LARCH_$(ISA))/libXext.so

# Enable when libdbus is done in 64 bit
# BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
