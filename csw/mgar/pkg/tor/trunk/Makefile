# $Id$
NAME = tor
VERSION = 0.2.1.28
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Secure network traffic router
define BLURB
endef

MASTER_SITES = http://www.torproject.org/dist/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.torproject.org
LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWtor += CSWosslrt
RUNTIME_DEP_PKGS_CSWtor += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWtor += CSWzlib

sysconfdir = /etc/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PAX_ARGS = -s ',/torrc\.sample,/torrc.CSW,p'

PRESERVECONF += $(sysconfdir)/tor/tor-tsocks.conf
PRESERVECONF += $(sysconfdir)/tor/torrc

MIGRATE_FILES += tor/tor-tsocks.conf
MIGRATE_FILES += tor/torrc

# New libevent has not been released
CHECKPKG_OVERRIDES_CSWtor += soname-not-found|libevent-2.0.so.5|is|needed|by|opt/csw/bin/tor
CHECKPKG_OVERRIDES_CSWtor += soname-not-found|libevent-2.0.so.5|is|needed|by|opt/csw/bin/tor-resolve
CHECKPKG_OVERRIDES_CSWtor += soname-not-found|libevent-2.0.so.5|is|needed|by|opt/csw/bin/tor-gencert
CHECKPKG_OVERRIDES_CSWtor += unidentified-dependency|CSWlibevent2-0-5
CHECKPKG_OVERRIDES_CSWtor += surplus-dependency|CSWlibevent2-0-5

include gar/category.mk
