NAME      = dbus-glib
VERSION   = 0.86
CATEGORIES   = lib

DESCRIPTION  = DBus GLib Bindings
define BLURB
  This package provides the bindings between GLib and DBus.
  D-Bus is a message bus system, a simple way for applications to talk to one another.
  In addition to interprocess communication, D-Bus helps coordinate process lifecycle;
  it makes it simple and reliable to code a "single instance" application or daemon,
  and to launch applications and daemons on demand when their services are needed.
endef

MASTER_SITES  = http://dbus.freedesktop.org/releases/dbus-glib/
DISTFILES     = $(NAME)-$(VERSION).tar.gz 
PKGDIST       = $(DISTFILE)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWdbusglib    = $(DESCRIPTION)
SPKG_DESC_CSWdbusglibdev = $(DESCRIPTION) development package

PACKAGES = CSWdbusglib CSWdbusglibdev

CATALOGNAME_CSWdbusglib         = dbus_glib
CATALOGNAME_CSWdbusglibdev      = dbus_glibdev

BUILD_DEP_PKGS = CSWglib2devel CSWlibdbusdev
RUNTIME_DEP_PKGS_CSWdbusglib    = CSWexpat CSWggettextrt CSWglib2 CSWlibdbus
RUNTIME_DEP_PKGS_CSWdbusglibdev = CSWdbusglib CSWglib2devel CSWlibdbusdev

PKGFILES_CSWdbusglibdev  = $(PKGFILES_DEVEL)

NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1

# These development dependencies are needed
CHECKPKG_OVERRIDES_CSWdbusglibdev += surplus-dependency|CSWdbusglib
CHECKPKG_OVERRIDES_CSWdbusglibdev += surplus-dependency|CSWlibdbusdev
CHECKPKG_OVERRIDES_CSWdbusglibdev += surplus-dependency|CSWglib2devel

include gar/category.mk

