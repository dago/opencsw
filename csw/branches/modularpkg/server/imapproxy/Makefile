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

MASTER_SITES = http://www.imapproxy.org/downloads/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = up-$(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = up-$(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWimapproxy,prototype,depend)
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

# files are extracted in up-imapproxy-version 
# not imapproxy-version
WORKSRC = $(WORKDIR)/up-$(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include ../category.mk

post-install:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	ginstall -D $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(GARNAME)/ChangeLog
	ginstall -D $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)/README
	ginstall -D $(WORKSRC)/README.known_issues $(DESTDIR)$(docdir)/$(GARNAME)/README.known_issues
	ginstall -D $(WORKSRC)/README.ssl $(DESTDIR)$(docdir)/$(GARNAME)/README.ssl
	ginstall -D $(WORKDIR)/imapproxy.conf $(DESTDIR)$(sysconfdir)/imapproxy.conf.CSW
	@$(MAKECOOKIE)


