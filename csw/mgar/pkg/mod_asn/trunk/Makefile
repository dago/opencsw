NAME = mod_asn
VERSION = 1.5
GARTYPE = v2

DESCRIPTION = An Apache module to look up routing data

MASTER_SITES += http://mirrorbrain.org/files/releases/
DISTFILES += $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWap2-mod-asn.postinstall
DISTFILES += CSWap2-mod-asn.preremove
DISTFILES += asn_import.conf

PATCHFILES += 0001-Do-not-download-routeviews.patch

VENDOR_URL = http://mirrorbrain.org/mod_asn/

LICENSE = debian/copyright

PACKAGES = CSWap2-mod-asn
SPKG_DESC_CSWap2-mod-asn = An Apache module to look up routing data
RUNTIME_DEP_PKGS_CSWap2-mod-asn += CSWapache2

PACKAGES += CSWmod-asn-utils
SPKG_DESC_CSWmod-asn-utils = Utilities to maintain the database for mod_asn
PKGFILES_CSWmod-asn-utils += $(sysconfdir)/.*
PKGFILES_CSWmod-asn-utils += $(bindir)/.*
PKGFILES_CSWmod-asn-utils += .*/asn\.sql
ARCHALL_CSWmod-asn-utils = 1
# The data, checkpkg cannot detect that
RUNTIME_DEP_PKGS_CSWmod-asn-utils += CSWroute-views-data
CHECKPKG_OVERRIDES_CSWmod-asn-utils += surplus-dependency|CSWroute-views-data
# For asn_import
RUNTIME_DEP_PKGS_CSWmod-asn-utils += CSWpy-psycopg2
CHECKPKG_OVERRIDES_CSWmod-asn-utils += surplus-dependency|CSWpy-psycopg2

REINPLACEMENTS += cswpython
REINPLACE_MATCH_cswpython = \#!/usr/bin/env\ python
REINPLACE_WITH_cswpython = \#!/opt/csw/bin/python
REINPLACE_FILES_cswpython += asn_get_routeviews.py
REINPLACE_FILES_cswpython += asn_import.py

REINPLACEMENTS += importconf
REINPLACE_MATCH_importconf = /etc/asn_import.conf
REINPLACE_WITH_importconf = $(sysconfdir)/asn_import.conf
REINPLACE_FILES_importconf += asn_import.py

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(AP2_ROOT)/libexec
AP2_APXS      = $(AP2_ROOT)/sbin/apxs
AP2_MODS = 1
AP2_MODFILES += mod_geoip2.so

# No test suite available
TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

PRESERVECONF += $(prefix)/apache2/etc/extra/mod_asn.conf
PRESERVECONF += $(sysconfdir)/asn_import.conf

include gar/category.mk

build-custom:
	$(BUILD_ENV) $(AP2_APXS) -c $(WORKSRC)/mod_asn.c
	$(MAKECOOKIE)

install-custom: DOCDEST=$(DESTDIR)$(docdir)/ap2_mod_asn
install-custom:
	ginstall -d -m 755 $(DESTDIR)$(AP2_LIBEXEC)
	cd $(WORKSRC) && $(AP2_APXS) -S LIBEXECDIR=$(DESTDIR)$(AP2_LIBEXEC) -i mod_asn.la
	ginstall -d -m 755 $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 $(WORKSRC)/mod_asn.conf $(DESTDIR)$(prefix)/apache2/etc/extra/mod_asn.conf
	ginstall -d -m 755 $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/asn_get_routeviews.py $(DESTDIR)$(bindir)/asn_get_routeviews
	ginstall -m 0755 $(WORKSRC)/asn_import.py $(DESTDIR)$(bindir)/asn_import
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)
	ginstall -m 0644 $(WORKDIR)/asn_import.conf $(DESTDIR)$(sysconfdir)
	ginstall -d -m 755 $(DOCDEST)
	ginstall -m 644 $(WORKSRC)/asn.sql $(DOCDEST)/asn.sql
	$(MAKECOOKIE)

