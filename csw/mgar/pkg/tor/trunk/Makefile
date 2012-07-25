# $Id$
NAME = tor
VERSION = 0.2.2.37
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

RUNTIME_DEP_PKGS_CSWtor += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWtor += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWtor += CSWlibz1

sysconfdir = /etc/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PAX_ARGS = -s ',/torrc\.sample,/torrc.CSW,p'

PRESERVECONF += $(sysconfdir)/tor/tor-tsocks.conf
PRESERVECONF += $(sysconfdir)/tor/torrc

MIGRATE_FILES += tor/tor-tsocks.conf
MIGRATE_FILES += tor/torrc

include gar/category.mk
