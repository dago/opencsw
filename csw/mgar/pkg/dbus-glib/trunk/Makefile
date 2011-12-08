NAME = dbus-glib
VERSION = 0.98
CATEGORIES = lib

DESCRIPTION = DBus GLib Bindings
define BLURB
  This package provides the bindings between GLib and DBus.
  D-Bus is a message bus system, a simple way for applications to talk to one another.
  In addition to interprocess communication, D-Bus helps coordinate process lifecycle;
  it makes it simple and reliable to code a "single instance" application or daemon,
  and to launch applications and daemons on demand when their services are needed.
endef

MASTER_SITES = http://dbus.freedesktop.org/releases/dbus-glib/
DISTFILES = $(DISTNAME).tar.gz 

# New glib is Solaris 10 only
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibdbus-dev

PACKAGES += CSWlibdbus-glib1-2
SPKG_DESC_CSWlibdbus-glib1-2 = DBus glib bindings
PKGFILES_CSWlibdbus-glib1-2 += $(call pkgfiles_lib,libdbus-glib-1.so.2)
RUNTIME_DEP_PKGS_CSWlibdbus-glib1-2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib1-2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib1-2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdbus-glib1-2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib1-2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib1-2 += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWlibdbus-glib1-2 += CSWlibgio2-0-0
OBSOLETED_BY_CSWlibdbus-glib1-2 += CSWdbusglib
CATALOGNAME_CSWdbusglib = dbus_glib_stub

PACKAGES += CSWlibdbus-glib-dev
SPKG_DESC_CSWlibdbus-glib-dev = Development files for libdbus-glib-1.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibglib2-dev
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibdbus-dev
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWlibdbus-glib-dev += CSWlibglib2-0-0
OBSOLETED_BY_CSWlibdbus-glib-dev += CSWdbusglibdev
CATALOGNAME_CSWdbusglibdev = dbus_glibdev_stub

# These are docs only, ignore for now
CHECKPKG_OVERRIDES_CSWlibdbus-glib-dev += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/dbus-glib/dbus-glib-DBusGMethod.html
CHECKPKG_OVERRIDES_CSWlibdbus-glib-dev += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/dbus-glib/dbus-glib-DBus-GObject-related-functions.html
CHECKPKG_OVERRIDES_CSWlibdbus-glib-dev += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/dbus-glib/dbus-glib-DBusGProxy.html

BUILD64 = 1

include gar/category.mk

