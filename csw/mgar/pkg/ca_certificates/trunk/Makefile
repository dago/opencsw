#####################################################################
# OpenCSW build recipe for ca-certificates
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = cacertificates
VERSION = $(shell date '+%Y%m%d')
CATEGORIES = xtra
GARTYPE = v2

DESCRIPTION = CA certificates
define BLURB
  CA certificates
endef

PACKAGES = CSWcacertificates

ARCHALL = 1

###### Upstream and opencsw files information #######

MASTER_SITES = http://hg.mozilla.org/mozilla-central/raw-file/default/security/nss/lib/ckfw/builtins/
DISTFILES  = certdata.txt certdata2pem.pl update-ca-certificates ca-certificates.conf README.CSW
DISTFILES += CSWcacertificates.postinstall CSWcacertificates.postremove

PRESERVECONF = $(sysconfdir)/ca-certificates.conf

MIGRATE_FILES = ca-certificates.conf

##### Build and installation information #####

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

#HASH_TYPES = hash subject_hash_old
HASH_TYPES = hash

include gar/category.mk

$(WORKDIR)/hash.db: install-certificates
	#rm -f $(WORKDIR)/hash.db
	#find "$(DESTDIR)/$(sharedstatedir)/$(NAME)" -name *.pem | while read FILE; do \
	#	for HASH_TYPE in $(HASH_TYPES); do \
	#		echo "`basename $$FILE`=`/opt/csw/bin/openssl x509 -$$HASH_TYPE -fingerprint -noout -in "$$FILE" | head -n 1`.0" >> $(WORKDIR)/hash.db; \
	#	done; \
	#done

$(WORKDIR)/LICENSE: $(WORKDIR)/certdata.txt
	sed -ne '/BEGIN LICENSE BLOCK/,/END LICENSE BLOCK/p' "$(WORKDIR)/certdata.txt" | grep -v "LICENSE BLOCK" \
		> "$(WORKDIR)/LICENSE"

install-certificates: $(WORKDIR)/certdata.txt
	ginstall -d "$(DESTDIR)/$(sharedstatedir)/$(NAME)/mozilla"
	cd "$(DESTDIR)/$(sharedstatedir)/$(NAME)/mozilla" && perl "$(CURDIR)/$(WORKDIR)/certdata2pem.pl" < "$(CURDIR)/$(WORKDIR)/certdata.txt"

install-custom: install-certificates $(WORKDIR)/hash.db $(WORKDIR)/LICENSE
	ginstall -d "$(DESTDIR)/$(sysconfdir)/ssl"
	ginstall -D "$(WORKDIR)/ca-certificates.conf" "$(DESTDIR)/$(sysconfdir)/ca-certificates.conf"
	ginstall -d "$(DESTDIR)/$(sysconfdir)/ssl/certs"
	ginstall -d "$(DESTDIR)/$(sharedstatedir)/$(NAME)"
	ginstall -D "$(WORKDIR)/update-ca-certificates" "$(DESTDIR)/$(sbindir)/update-ca-certificates"
	ginstall -D "$(FILEDIR)/hash.db" "$(DESTDIR)/$(sharedstatedir)/$(NAME)/hash.db"
	ginstall -D "$(WORKDIR)/README.CSW" "$(DESTDIR)/$(docdir)/$(NAME)/README.CSW"
	ginstall -D "$(WORKDIR)/LICENSE" "$(DESTDIR)/$(docdir)/$(NAME)/license"
	
	ginstall -d "$(PKGROOT)/$(prefix)/etc/ssl"
	( cd "$(PKGROOT)/$(prefix)/etc/ssl/" && ln -s "../../../..$(sysconfdir)/ssl/certs" )
