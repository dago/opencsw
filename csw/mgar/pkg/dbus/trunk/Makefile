# $Id: Makefile 15327 2011-08-12 21:35:23Z dmichelsen $
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! test position of pidfile in compilation and cswdbus
# ! cleanup of /usr/share, /usr/local occurrences

NAME = dbus
VERSION = 1.5.6
CATEGORIES = lib

DESCRIPTION  = DBus Message Bus System
define BLURB
  D-Bus is a message bus system, a simple way for applications to talk to one another.
  In addition to interprocess communication, D-Bus helps coordinate process lifecycle;
  it makes it simple and reliable to code a "single instance" application or daemon,
  and to launch applications and daemons on demand when their services are needed.

  D-Bus supplies both a system daemon (for events such as "new hardware device added"
  or "printer queue changed") and a per-user-login-session daemon (for general IPC needs
  among user applications). Also, the message bus is built on top of a general one-to-one
  message passing framework, which can be used by any two apps to communicate directly
  (without going through the message bus daemon). Currently the communicating applications
  are on one computer, or through unencrypted TCP/IP suitable for use behind a firewall
  with shared NFS home directories. (Help wanted with better remote transports -
  the transport mechanism is well-abstracted and extensible.) 
endef

MASTER_SITES  = http://dbus.freedesktop.org/releases/dbus/
DISTFILES = $(DISTNAME).tar.gz 
DISTFILES += cswusergroup
DISTFILES += cswdbus

# Use this patch until this issue is fixed:
#   http://bugs.freedesktop.org/show_bug.cgi?id=40235
#PATCHFILES += dbus-sysdeps-unix.c.diff

#PATCHFILES += dbus-sysdeps.h.diff

# Use patch until this is fixed:
#   http://bugs.freedesktop.org/show_bug.cgi?id=40313
PATCHFILES += 0002-Add-missing-inclusion-of-inttypes.h.patch

# Use this custom-patch unless this is fixed:
#   http://bugs.freedesktop.org/show_bug.cgi?id=39987
PATCHFILES += 0001-Use-LOG_PERROR-only-when-available.patch

PATCHFILES += attachment-50480.patch

PACKAGES += CSWdbus
CATALOGNAME_CSWdbus = dbus
SPKG_DESC_CSWdbus = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWdbus += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWdbus += CSWlibdbus1-3
# These are search pathes:
#   /opt/csw/share:/usr/local/share:/usr/share:
CHECKPKG_OVERRIDES_CSWdbus += file-with-bad-content|/usr/local|root/opt/csw/libexec/dbus-daemon-launch-helper
CHECKPKG_OVERRIDES_CSWdbus += file-with-bad-content|/usr/share|root/opt/csw/libexec/dbus-daemon-launch-helper
CHECKPKG_OVERRIDES_CSWdbus += file-with-bad-content|/usr/local|root/opt/csw/bin/dbus-daemon
CHECKPKG_OVERRIDES_CSWdbus += file-with-bad-content|/usr/share|root/opt/csw/bin/dbus-daemon
# This is an example
CHECKPKG_OVERRIDES_CSWdbus += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/dbus-daemon.1

PACKAGES += CSWlibdbus1-3
SPKG_DESC_CSWlibdbus1-3 = DBus message bus system, libdbus-1.so.3
PKGFILES_CSWlibdbus1-3 += $(call pkgfiles_lib,libdbus-1.so.3)
OBSOLETED_BY_CSWlibdbus1-3 += CSWlibdbus
# These are search pathes:
#   /opt/csw/share:/usr/local/share:/usr/share:
CHECKPKG_OVERRIDES_CSWlibdbus1-3 += file-with-bad-content|/usr/local|root/opt/csw/lib/libdbus-1.so.3.6.3
CHECKPKG_OVERRIDES_CSWlibdbus1-3 += file-with-bad-content|/usr/share|root/opt/csw/lib/libdbus-1.so.3.6.3
CHECKPKG_OVERRIDES_CSWlibdbus1-3 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libdbus-1.so.3.6.3
CHECKPKG_OVERRIDES_CSWlibdbus1-3 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libdbus-1.so.3.6.3
CHECKPKG_OVERRIDES_CSWlibdbus1-3 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libdbus-1.so.3.6.3
CHECKPKG_OVERRIDES_CSWlibdbus1-3 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libdbus-1.so.3.6.3

PACKAGES += CSWlibdbus-dev
SPKG_DESC_CSWlibdbus-dev = Development files for libdbus
PKGFILES_CSWlibdbus-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibdbus-dev += $(call baseisadirs,$(libdir),dbus-1.0/.*)
PKGFILES_CSWlibdbus-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWlibdbus-dev += CSWlibdbus1-3
OBSOLETED_BY_CSWlibdbus-dev += CSWlibdbusdev
# These are docs
CHECKPKG_OVERRIDES_CSWlibdbus-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/dbus/api/group__DBusSysdeps.html
CHECKPKG_OVERRIDES_CSWlibdbus-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/dbus/api/dbus-sysdeps-unix_8c_source.html
CHECKPKG_OVERRIDES_CSWlibdbus-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/dbus/api/dbus-sysdeps-unix_8c_source.html
CHECKPKG_OVERRIDES_CSWlibdbus-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/dbus/api/group__DBusSysdeps.html
CHECKPKG_OVERRIDES_CSWlibdbus-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/dbus/system-activation.txt

INITSMF += /etc/opt/csw/init.d/cswdbus
PRESERVECONF += /etc/opt/csw/dbus-1/system.conf
PRESERVECONF += /etc/opt/csw/dbus-1/session.conf

MIGRATECONF += dbus-1/session.conf
MIGRATECONF += dbus-1/system.conf

USERGROUP = /etc/opt/csw/pkg/CSWdbus/cswusergroup

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-tests
CONFIGURE_ARGS += --with-xml=expat 

# Needed for sockaddr_in6
EXTRA_CFLAGS += -D__EXTENSIONS__

BUILD64_LIBS_ONLY = 1

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswdbus $(PKGROOT)/etc/opt/csw/init.d/cswdbus
	ginstall -d $(PKGROOT)/etc/opt/csw/pkg/CSWdbus
	ginstall $(WORKDIR)/cswusergroup $(PKGROOT)/etc/opt/csw/pkg/CSWdbus/cswusergroup

