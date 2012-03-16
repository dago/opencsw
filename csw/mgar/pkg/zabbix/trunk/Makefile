# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = zabbix
VERSION = 1.8.10
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Zabbix monitoring system
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# This is just for the server which is in 64 bit only on Solars 10
BUILD64-5.9 =
BUILD64-5.10 = 1
BUILD64 = $(BUILD64-$(GAROSREL))
ISAEXEC = 1

PACKAGES += CSWzabbix-agent
SPKG_DESC_CSWzabbix-agent = Zabbix monitoring system agent
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWzabbix-agent += CSWlibiconv2

PACKAGES-5.10 += CSWzabbix-server
PACKAGES += $(PACKAGES-$(GAROSREL))
SPKG_DESC_CSWzabbix-server = Zabbix monitoring system server
PKGFILES_CSWzabbix-server += $(call baseisadirs,$(sbindir),zabbix_server)
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibz1
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibidn11

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-libcurl
CONFIGURE_ARGS += --enable-agent
CONFIGURE_ARGS += --enable-ipv6

# We build the server only on Solaris 10 and only on 64 bit
CONFIGURE_ARGS-5.9-32 += --disable-server
CONFIGURE_ARGS-5.10-32 += --disable-server
CONFIGURE_ARGS-5.10-64 += --enable-server
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL)-$(MEMORYMODEL))

include gar/category.mk

