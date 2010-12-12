NAME      = dbus
VERSION   = 1.3.1
CATEGORIES   = lib

DESCRIPTION  = DBus Message Bus System
define BLURB
D-Bus is a message bus system, a simple way for applications to talk to one another. In addition to interprocess communication, D-Bus helps coordinate process lifecycle; it makes it simple and reliable to code a "single instance" application or daemon, and to launch applications and daemons on demand when their services are needed.

D-Bus supplies both a system daemon (for events such as "new hardware device added" or "printer queue changed") and a per-user-login-session daemon (for general IPC needs among user applications). Also, the message bus is built on top of a general one-to-one message passing framework, which can be used by any two apps to communicate directly (without going through the message bus daemon). Currently the communicating applications are on one computer, or through unencrypted TCP/IP suitable for use behind a firewall with shared NFS home directories. (Help wanted with better remote transports - the transport mechanism is well-abstracted and extensible.) 
endef

MASTER_SITES  = http://dbus.freedesktop.org/releases/dbus/
DISTFILES     = $(NAME)-$(VERSION).tar.gz 
PKGDIST       = $(DISTFILE)

# Generate description fields
SPKG_DESC_CSWdbus          = $(DESCRIPTION)
SPKG_DESC_CSWlibdbus       = $(DESCRIPTION) libraries
SPKG_DESC_CSWlibdbusdev    = $(DESCRIPTION) development package

PACKAGES                   = CSWdbus CSWlibdbus CSWlibdbusdev
CATALOGNAME_CSWdbus        = dbus
CATALOGNAME_CSWlibdbus     = libdbus
CATALOGNAME_CSWlibdbusdev  = libdbusdev
DISTFILES                 += CSWdbus.preinstall
DISTFILES                 += cswdbus

# Dynamic CSWlibdbusdev prototype
PKGFILES_CSWlibdbusdev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibdbusdev += $(libdir)/dbus-1.0/.*

# Dynamic CSWlibdbus prototype
PKGFILES_CSWlibdbus     = $(PKGFILES_RT)

# Dependencies tracking
RUNTIME_DEP_PKGS_CSWdbus        = CSWexpat CSWlibdbus CSWcswclassutils
RUNTIME_DEP_PKGS_CSWlibdbusdev  = CSWlibdbus

CHECKPKG_OVERRIDES_CSWlibdbusdev += surplus-dependency|CSWlibdbus
CHECKPKG_OVERRIDES_CSWdbus += action-class-only-in-pkginfo|cswinitsmf
CHECKPKG_OVERRIDES_CSWdbus += action-class-only-in-pkginfo|cswcpsampleconf

# SMF support
SPKG_CLASSES_CSWdbus = none cswcpsampleconf cswinitsmf 
PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswdbus$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/system.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/session.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } { print }'
	
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-tests --with-xml=expat 

EXTRA_CPPFLAGS = -D_XPG4_2

BUILD64 = 1

PATCHFILES += dbus-sysdeps-unix.c.diff
PATCHFILES += dbus-sysdeps.h.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk

# moving configuration file & installing init script
post-install:
	( OLDDIR=`pwd` && cd $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))/opt/csw/etc/dbus-1 && \
          for i in *.conf ; do mv $$i $$i.CSW ; done && cd $$OLDDIR ; \
	  ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))/etc/opt/csw/init.d  ; \
	  cp -fr $(FILEDIR)/cswdbus $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))/etc/opt/csw/init.d  ; \
	  ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))/etc/rc3.d/ ; \
	  ln -s ../init.d/cswdbus $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))/etc/rc3.d/S52cswdbus  ; )
	@$(MAKECOOKIE)


