GARNAME      = dbus-glib
GARVERSION   = 0.86
CATEGORIES   = lib

DESCRIPTION  = DBus GLib Bindings
define BLURB
This package provides the bindings between GLib and DBus

D-Bus is a message bus system, a simple way for applications to talk to one another. In addition to interprocess communication, D-Bus helps coordinate process lifecycle; it makes it simple and reliable to code a "single instance" application or daemon, and to launch applications and daemons on demand when their services are needed.
endef

MASTER_SITES  = http://dbus.freedesktop.org/releases/dbus-glib/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz 
PKGDIST       = $(DISTFILE)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWdbusglib    = $(DESCRIPTION)
SPKG_DESC_CSWdbusglibdev = $(DESCRIPTION) development package

PACKAGES = CSWdbusglib CSWdbusglibdev

CATALOGNAME_CSWdbusglib         = dbus_glib
CATALOGNAME_CSWdbusglibdev      = dbus_glibdev

RUNTIME_DEP_PKGS_CSWdbusglibdev	= CSWdbusglib
RUNTIME_DEP_PKGS_CSWdbusglib    = CSWexpat CSWggettextrt CSWglib2 CSWiconv CSWsunmath CSWlibdbus

PKGFILES_CSWdbusglibdev  = $(PKGFILES_DEVEL)
# PKGFILES_CSWdbusglibdev += $(prefix)/include/.*
# PKGFILES_CSWdbusglibdev += $(prefix)/lib/.*\.a
# PKGFILES_CSWdbusglibdev += $(prefix)/lib/pkgconfig/.*

#CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
#CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-tests 

# BUILD64 = 1

include gar/category.mk

