# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = rsync
VERSION = 3.1.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Utility which provides fast incremental file transfer

define BLURB
  rsync is an open source utility that provides fast incremental file transfer.
  rsync is freely available under the GNU General Public License and is
  currently being maintained by Wayne Davison.
endef

MASTER_SITES = http://samba.anu.edu.au/ft+= $(DISTNAME).tar.gz
DISTFILES += cswrsyncd.xml
DISTFILES += rsyncd.conf.CSWTFILES += cswrsyncd

VENDOR_URL = http://rsync.samba.org/

PACKAGES += CSWrsync
SPKG_DESC_CSWrsync = Utility which provides fast increme# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWrsync += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWrsync += CSWlibiconv2

PACKAGES += CSWrsyncd
SPKG_DESC_CSWrsyncd = Daemon for rsyncd server
PKGFILES_CSWrsyncd += $(sysconfdir)/rsyncd.conf.CSW
PKGFILES_CSWrsyncd += $(mandir)/man5/rsyncd.conf.5
PKGFILES_CSWrsyncd += /var/opt/csw/svc/manifest/cswrsyncd.xml

# This the URL of the DTD
CHECKPKG_OVERRIDES_CSWrsyncd += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswrsyncd.xml

# rsyncd is in fact rsync --daemon
RUNTIME_DEP_PKGS_CSWrsyncd += CSWrsync
CHECKPKG_OVERRIDES_CSWrsyncd += surplus-dependency|CSWrsyncync += CSWlibiconv2

# The location of rsyncd.conf to OpenCSW standard has been done in _CSWrsyncd3.0.8
MIGRATE_FILES = rsyncd.conf
MIGRATE_PRESERVECONF += $(sysconfdir)/rsyncd.confE_SOURCE_DIR = /etc

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-rsyncd-conf=$(syscon/init.d/cswrsyncd

REINPLACE_USRLOCAL = $(mandir)/man1/rsync.1
REINPLACE_WHEN_USRLOCAL = postinstall

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = /etc/rsyncd\.conf
REINPLACE_WITH_conf = $(sysconfdir)/rsyncd.conf
REINPLACE_FILES_conf += $(mandir)/man1/rsync.1
REINPLACE_FILES_conf += $(mandir)/man5/rsyncd.conf.5
REINPLACE_WHEN_cPROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswrsyncd.xml
PROTOTYPE_CLASS_smf = manifest

# There is one ACL-test on NFSv4 failling
SKIPTEST ?= 1

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKDIR)/cswrsyncd.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswrsyncd.xmls	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -m 0644 $(WORKDIR)/rsyncd.conf.CSW $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(sharedstatedir)/rsync/support/
	ginstall -m 0755 $(WORKSRC)/support/* $(DESTDIR)$(sharedstatedir)/rsync/support/
	@$(MAKECOOKIE)
