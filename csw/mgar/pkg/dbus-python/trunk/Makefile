GARNAME = dbus-python
GARVERSION = 0.83.0
CATEGORIES = lib

DESCRIPTION = DBUS Bindings for Python
define BLURB
	D-Bus is a message bus system, a simple way for applications to 
	talk to one another. In addition to interprocess communication,
   	D-Bus helps coordinate process lifecycle; it makes it simple and 
	reliable to code a "single instance" application or daemon, 
	and to launch applications and daemons on demand when their services 
	are needed.

	D-Bus supplies both a system daemon 
	(for events such as "new hardware device added" or "printer queue changed") 
	and a per-user-login-session daemon 
	(for general IPC needs among user applications). 
	Also, the message bus is built on top of a general one-to-one 
	message passing framework, which can be used by any two apps to 
	communicate directly (without going through the message bus daemon). 
	Currently the communicating applications are on one computer, 
	or through unencrypted TCP/IP suitable for use behind a firewall 
	with shared NFS home directories. (Help wanted with better remote 
	transports - the transport mechanism is well-abstracted and extensible.)
endef

MASTER_SITES = http://dbus.freedesktop.org/releases/dbus-python/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.freedesktop.org/wiki/Software/DBusBindings
PACKAGES = CSWdbus-python
CATALOGNAME_CSWdbus-python = dbus-python
SPKG_DESC_CSWdbus-python = $(DESCRIPTION)

REQUIRED_PKGS_CSWdbus-python  = 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
CFLAGS = -xc99
CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk
