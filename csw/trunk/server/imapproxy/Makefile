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
DISTFILES += imapproxy.conf
DISTFILES += changelog.CSW
# init and smf stuffs
DISTFILES += cswimapproxy imapproxy.xml 
DISTFILES += i.smf r.smf

# imapproxy lacks include of openssl/md5.h
PATCHFILES += md5_include.patch

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

ENABLE_TEST = 0

include ../category.mk

post-install:
	ginstall -d $(DESTDIR)/etc/init.d 
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	ginstall -D $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(GARNAME)/ChangeLog
	ginstall -D $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)/README
	ginstall -D $(WORKSRC)/README.known_issues $(DESTDIR)$(docdir)/$(GARNAME)/README.known_issues
	ginstall -D $(WORKSRC)/README.ssl $(DESTDIR)$(docdir)/$(GARNAME)/README.ssl
	ginstall -D $(WORKDIR)/i.smf $(DESTDIR)/i.smf
	ginstall -D $(WORKDIR)/r.smf $(DESTDIR)/r.smf
#	ginstall -D $(WORKDIR)/i.init $(DESTDIR)/i.init
#	ginstall -D $(WORKDIR)/r.init $(DESTDIR)/r.init
	ginstall -D $(WORKDIR)/imapproxy.conf $(DESTDIR)$(sysconfdir)/imapproxy.conf.CSW
	ginstall -D $(WORKDIR)/imapproxy.xml $(DESTDIR)$(localstatedir)/svc/manifest/network/imapproxy.xml
	ginstall -D $(WORKDIR)/cswimapproxy $(DESTDIR)/etc/init.d/cswimapproxy
	ginstall -D $(WORKDIR)/svc-imapproxy $(DESTDIR)$(libdir)/svc/method/svc-imapproxy
	@$(MAKECOOKIE)


