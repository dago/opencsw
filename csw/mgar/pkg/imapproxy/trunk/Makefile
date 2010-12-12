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

NAME = imapproxy
VERSION = 1.2.7
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

RUNTIME_DEP_PKGS  = CSWtcpwrap 
RUNTIME_DEP_PKGS += CSWosslrt 

SPKG_CLASSES = none cswpreserveconf cswinitsmf

###### Upstream and opencsw files information #######

MASTER_SITES = http://www.imapproxy.org/downloads/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = up-$(NAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = up-$(NAME)-$(VERSION).tar.gz
DISTFILES += imapproxy.conf
DISTFILES += changelog.CSW README.CSW
# init and smf stuffs
DISTFILES += cswimapproxy cswimapproxy.xml

DISTNAME = up-$(NAME)-$(VERSION)

INITSMF = /etc/init.d/cswimapproxy
PRESERVECONF = /opt/csw/etc/imapproxy.conf

# imapproxy lacks include of openssl/md5.h
# PATCHFILES += md5_include.patch

# move the default configuration file location
# under /opt/csw
PATCHFILES += conf_file_location.patch

# patch to add DESTDIR support to
# imapproxy makefile
PATCHFILES += destdir.patch

##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

post-merge:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)$(docdir)/$(NAME)/changelog.CSW
	ginstall -D $(WORKDIR_FIRSTMOD)/README.CSW $(PKGROOT)$(docdir)/$(NAME)/README.CSW
	ginstall -D $(WORKSRC_FIRSTMOD)/ChangeLog $(PKGROOT)$(docdir)/$(NAME)/ChangeLog
	ginstall -D $(WORKSRC_FIRSTMOD)/README $(PKGROOT)$(docdir)/$(NAME)/README
	ginstall -D $(WORKSRC_FIRSTMOD)/README.known_issues $(PKGROOT)$(docdir)/$(NAME)/README.known_issues
	ginstall -D $(WORKSRC_FIRSTMOD)/README.ssl $(PKGROOT)$(docdir)/$(NAME)/README.ssl
	ginstall -D $(WORKDIR_FIRSTMOD)/imapproxy.conf $(PKGROOT)$(sysconfdir)/imapproxy.conf.CSW
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswimapproxy.xml" "$(PKGROOT)/var/opt/csw/svc/manifest/network/cswimapproxy.xml"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswimapproxy" "$(PKGROOT)/etc/init.d/cswimapproxy"
	@$(MAKECOOKIE)


