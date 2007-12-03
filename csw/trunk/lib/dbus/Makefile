GARNAME      = dbus
GARVERSION   = 1.1.1
CATEGORIES   = libs

DESCRIPTION  = DBus Message Bus System
define BLURB
D-Bus is a message bus system, a simple way for applications to talk to one another. In addition to interprocess communication, D-Bus helps coordinate process lifecycle; it makes it simple and reliable to code a "single instance" application or daemon, and to launch applications and daemons on demand when their services are needed.

D-Bus supplies both a system daemon (for events such as "new hardware device added" or "printer queue changed") and a per-user-login-session daemon (for general IPC needs among user applications). Also, the message bus is built on top of a general one-to-one message passing framework, which can be used by any two apps to communicate directly (without going through the message bus daemon). Currently the communicating applications are on one computer, or through unencrypted TCP/IP suitable for use behind a firewall with shared NFS home directories. (Help wanted with better remote transports - the transport mechanism is well-abstracted and extensible.) 
endef

MASTER_SITES  = http://dbus.freedesktop.org/releases/dbus/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz 
PKGDIST       = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES    += CSWdbus.gspec CSWdbus.prototype CSWdbus.depend CSWdbus.postinstall
DISTFILES    += CSWlibdbus.gspec CSWlibdbus.prototype CSWlibdbus.depend
DISTFILES    += CSWlibdbusdev.gspec CSWlibdbusdev.prototype CSWlibdbusdev.depend
# DISTFILES    += $(call admfiles,CSWdbus, depend)

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
# CPPFLAGS   += -I$(DESTDIR)/opt/csw/include/xfce4
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

include ../category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --disable-tests --with-xml=libxml

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | grep ELF | grep -e 'executable' -e 'dynamic lib' | grep 'not stripped' && strip {}"  \; )

