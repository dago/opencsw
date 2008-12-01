GARNAME      = dbus-glib
GARVERSION   = 0.76
CATEGORIES   = lib

DESCRIPTION  = DBus GLib Bindings
define BLURB
This package provides the bindings between GLib and DBus

D-Bus is a message bus system, a simple way for applications to talk to one another. In addition to interprocess communication, D-Bus helps coordinate process lifecycle; it makes it simple and reliable to code a "single instance" application or daemon, and to launch applications and daemons on demand when their services are needed.
endef

MASTER_SITES  = http://dbus.freedesktop.org/releases/dbus-glib/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz 
PKGDIST       = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES    += CSWdbusglib.gspec CSWdbusglib.prototype CSWdbusglib.depend
DISTFILES    += CSWdbusglibdev.gspec CSWdbusglibdev.prototype CSWdbusglibdev.depend
# DISTFILES    += $(call admfiles,CSWdbusglib, depend)

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
# CPPFLAGS   += -I$(DESTDIR)/opt/csw/include/xfce4
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

include gar/category.mk

LIBDEPS += lib/dbus

CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --disable-tests

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

