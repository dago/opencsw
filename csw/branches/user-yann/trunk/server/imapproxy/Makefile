GARNAME = imapproxy
GARVERSION = 1.2.5rc1
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
DISTFILES  = up-$(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWimapproxy,prototype,depend)
DISTFILES += changelog.CSW

# imapproxy lacks include of openssl/md5.h
PATCHFILES += md5_include.patch

# patch to add DESTDIR support to
# imapproxy makefile
PATCHFILES += destdir.patch

# files are extracted in up-imapproxy-version 
# not imapproxy-version
WORKSRC = $(WORKDIR)/up-$(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS)

ENABLE_TEST = 0

include ../category.mk

post-install:
	ginstall -d $(DESTDIR)/etc/init.d $(DESTDIR)/etc/rc2.d $(DESTDIR)/etc/rc0.d
	rm -rf $(DESTDIR)/etc/rc2.d/*imapproxy $(DESTDIR)/etc/rc0.d/*imapproxy
	ginstall -d $(DESTDIR)$(sysconfdir)
	@( cd $(WORKSRC); $(MAKE) DESTDIR=$(DESTDIR) install-conf install-init )
	ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	ginstall -D $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(GARNAME)/ChangeLog
	ginstall -D $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)/README
	@$(MAKECOOKIE)


