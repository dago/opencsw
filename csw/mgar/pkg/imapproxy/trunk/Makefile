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
GARTYPE = v2

DESCRIPTION = A caching IMAP proxy server
define BLURB
  The IMAP Proxy server is a caching IMAP proxy server. 
  It was written to reduce the load that Webmail clients 
  put on an IMAP server by keeping server connections alive 
  for reuse, thus avoiding a new server connection for each 
  Webmail transaction.
endef

PACKAGES = CSWimapproxy

RUNTIME_DEP_PKGS = CSWlibssl1-0-0

# Default paths referenced in documentation files, can be safely ignored
CHECKPKG_OVERRIDES_CSWimapproxy += file-with-bad-content|/usr/local|root/opt/csw/share/doc/imapproxy/README
CHECKPKG_OVERRIDES_CSWimapproxy += file-with-bad-content|/usr/local|root/opt/csw/share/doc/imapproxy/README.ssl
CHECKPKG_OVERRIDES_CSWimapproxy += file-with-bad-content|/usr/local|root/opt/csw/share/doc/imapproxy/README.known_issues

# DTD paths referenced in smf manifest file, can be safely ignored
CHECKPKG_OVERRIDES_CSWimapproxy += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswimapproxy.xml

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

###### Upstream and opencsw files information #######

# Imapproxy is now Squirrelmail IMAP Proxy and is now available
# in squirrelaim sourceforge projet
SF_PROJ = squirrelmail
MASTER_SITES = $(SF_MIRRORS)

UPSTREAM_MASTER_SITES = http://squirrelmail.org/download.php#imap_proxy

DISTFILES  = squirrelmail-imap_proxy-$(VERSION).tar.gz
DISTFILES += imapproxy.conf
DISTFILES += changelog.CSW README.CSW
# init and smf stuffs
DISTFILES += cswimapproxy cswimapproxy.xml

DISTNAME = squirrelmail-imap_proxy-$(VERSION)

INITSMF = /etc/opt/csw/init.d/cswimapproxy
PRESERVECONF = /etc/opt/csw/imapproxy.conf

MIGRATE_FILES = imapproxy.conf

# imapproxy lacks include of openssl/md5.h
# PATCHFILES += md5_include.patch

# move the default configuration file location
# under /opt/csw
PATCHFILES += conf_file_location.patch

# patch to add DESTDIR support to
# imapproxy makefile
PATCHFILES += destdir.patch

# LDFLAGS is not present in the Makefile
# for the pimpstat compilation, this patch fixes this
PATCHFILES += 0003-Missing-LDFLAGS-in-Makefile-fix.patch

##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libwrap=no

EXTRA_LDFLAGS = -z ignore -Bdirect 

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
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswimapproxy" "$(PKGROOT)/etc/opt/csw/init.d/cswimapproxy"
	@$(MAKECOOKIE)


