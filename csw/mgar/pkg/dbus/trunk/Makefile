GARNAME      = dbus
GARVERSION   = 1.2.4
CATEGORIES   = libs

DESCRIPTION  = DBus Message Bus System
define BLURB
D-Bus is a message bus system, a simple way for applications to talk to one another. In addition to interprocess communication, D-Bus helps coordinate process lifecycle; it makes it simple and reliable to code a "single instance" application or daemon, and to launch applications and daemons on demand when their services are needed.

D-Bus supplies both a system daemon (for events such as "new hardware device added" or "printer queue changed") and a per-user-login-session daemon (for general IPC needs among user applications). Also, the message bus is built on top of a general one-to-one message passing framework, which can be used by any two apps to communicate directly (without going through the message bus daemon). Currently the communicating applications are on one computer, or through unencrypted TCP/IP suitable for use behind a firewall with shared NFS home directories. (Help wanted with better remote transports - the transport mechanism is well-abstracted and extensible.) 
endef

MASTER_SITES  = http://dbus.freedesktop.org/releases/dbus/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz 
PKGDIST       = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES    += CSWdbus.gspec CSWdbus.prototype CSWdbus.depend CSWdbus.postinstall CSWdbus.preinstall checkinstall 
DISTFILES    += space i.smfno i.smfyes svc-dbus dbus.xml cswdbus CSWdbus.preremove
DISTFILES    += CSWlibdbus.gspec CSWlibdbus.prototype CSWlibdbus.depend
DISTFILES    += CSWlibdbusdev.gspec CSWlibdbusdev.prototype CSWlibdbusdev.depend
# DISTFILES    += $(call admfiles,CSWdbus, depend)

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

GREP = ggrep

include gar/category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --disable-tests --with-xml=expat

post-install:
	( mkdir -p $(DESTDIR)/etc/init.d )
	( mkdir -p $(DESTDIR)/etc/rc3.d )
	( cp -fr $(FILEDIR)/csw$(GARNAME) $(DESTDIR)/etc/init.d )
	( rm -f $(DESTDIR)/etc/rc3.d/S52$(GARNAME) )
	( ln -s /etc/init.d/csw$(GARNAME) $(DESTDIR)/etc/rc3.d/S52$(GARNAME) )
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

