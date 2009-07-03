#####################################################################
# OpenCSW build recipe for imapproxy
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

GARNAME = imapproxy
GARVERSION = 1.2.6
CATEGORIES = server

DESCRIPTION = A caching IMAP proxy server
define BLURB
  The IMAP Proxy server is a caching IMAP proxy server. 
  It was written to reduce the load that Webmail clients 
  put on an IMAP server by keeping server connections alive 
  for reuse, thus avoiding a new server connection for each 
  Webmail transaction.
endef

PACKAGES = CSWimapproxy

REQUIRED_PKGS  = CSWtcpwrap 
REQUIRED_PKGS += CSWosslrt 
REQUIRED_PKGS += CSWcswclassutils



###### Upstream and opencsw files information #######

MASTER_SITES = http://www.imapproxy.org/downloads/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = up-$(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = up-$(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWimapproxy.prototype
DISTFILES += imapproxy.conf
DISTFILES += changelog.CSW README.CSW
# init and smf stuffs
DISTFILES += cswimapproxy.init cswimapproxy.xml svc-cswimapproxy
DISTFILES += i.smf r.smf

# imapproxy lacks include of openssl/md5.h
# PATCHFILES += md5_include.patch

# move the default configuration file location
# under /opt/csw
PATCHFILES += conf_file_location.patch

# patch to add DESTDIR support to
# imapproxy makefile
PATCHFILES += destdir.patch


##### Build and installation information #####

# files are extracted in up-imapproxy-version 
# not imapproxy-version
WORKSRC = $(WORKDIR)/up-$(GARNAME)-$(GARVERSION)
WORKSRC_FIRSTMOD = $(WORKDIR_FIRSTMOD)/up-$(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

post-merge:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)$(docdir)/$(GARNAME)/changelog.CSW
	ginstall -D $(WORKDIR_FIRSTMOD)/README.CSW $(PKGROOT)$(docdir)/$(GARNAME)/README.CSW
	ginstall -D $(WORKSRC_FIRSTMOD)/ChangeLog $(PKGROOT)$(docdir)/$(GARNAME)/ChangeLog
	ginstall -D $(WORKSRC_FIRSTMOD)/README $(PKGROOT)$(docdir)/$(GARNAME)/README
	ginstall -D $(WORKSRC_FIRSTMOD)/README.known_issues $(PKGROOT)$(docdir)/$(GARNAME)/README.known_issues
	ginstall -D $(WORKSRC_FIRSTMOD)/README.ssl $(PKGROOT)$(docdir)/$(GARNAME)/README.ssl
	ginstall -D $(WORKDIR_FIRSTMOD)/imapproxy.conf $(PKGROOT)$(sysconfdir)/imapproxy.conf.CSW
	@$(MAKECOOKIE)


