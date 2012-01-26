NAME = djbdns
VERSION = 1.05
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Retrieve and publish Domain Name System information
define BLURB
djbdns is a collection of Domain Name System tools.  It includes several
components:

 * The dnscache program is a local DNS cache.  It accepts recursive DNS
   queries from local clients such as web browsers.  It collects responses
   from remote DNS servers.
 * The tinydns program is a fast, UDP-only DNS server.  It makes local DNS
   information available to the Internet.  It supports load balancing and
   client differentation.
 * The walldns program is a reverse DNS wall.  It provides matching reverse
   and forward records while hiding local host information.
 * The rbldns program is an IP-address-listing DNS server.  It uses DNS to
   publish a list of IP addresses, such as RBL or DUL.
 * The dns library handles outgoing and incoming DNS packets.  It can be
   used by clients such as web browsers to look up host addresses, hot names,
   MX records, etc.  It supports asynchronous resolution.
 * The dnsfilter program is a parallel IP-address-to-host-name converter.
 * The dnsip, dnsipq, dnsname, dnstxt, and dnsmx programs are simple
   command-line interfaces to DNS.
 * The dnsq and dnstrace programs are DNS debugging tools.

If you wish to replicate DNS information to secondary djbdns servers, you will
also need to install openssh and rsync to perform the actual replication.
This is not required unless you want to replicate to a secondary djbdns server
and is not required if your secondary is a BIND DNS server.
endef

MASTER_SITES += http://cr.yp.to/djbdns/
MASTER_SITES += http://smarden.org/pape/djb/manpages/
DISTFILES += $(DISTNAME).tar.gz
#DISTFILES += doc.tar.gz
DISTFILES += $(DISTNAME)-man.tar.gz

VENDOR_URL = http://cr.yp.to/djbdns.html
LICENSE = README

FILES = axfr-get axfrdns axfrdns-conf dnscache dnscache-conf dnsfilter dnsip dnsipq dnsmx dnsname dnsq dnsqr dnstrace dnstracesort dnstxt pickdns pickdns-conf pickdns-data random-ip rbldns rbldns-conf rbldns-data tinydns tinydns-conf tinydns-data tinydns-edit tinydns-get walldns walldns-conf

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

TEST_SCRIPTS =

include gar/category.mk

configure-custom:
	@echo "==> Configuring $(NAME)"
	@echo $(prefix) >$(WORKSRC)/conf-home
	@echo $(CC) $(CFLAGS) >$(WORKSRC)/conf-cc
	@$(MAKECOOKIE)

build-custom:
	@echo "==> building $(NAME)"
	cd $(WORKSRC) && gmake
	@$(MAKECOOKIE)

install-custom:
	@echo "==> installing $(NAME)"
	@echo "==> to $(DESTDIR)$(prefix)/bin"
	rm -rf   $(DESTDIR)$(prefix)
	mkdir -p $(DESTDIR)$(prefix)/bin
	ginstall -m 755 $(addprefix $(WORKSRC)/,$(FILES)) $(DESTDIR)$(prefix)/bin 
	mkdir -p $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKDIR)/djbdns-man/*.1 $(DESTDIR)$(mandir)/man1
	mkdir -p $(DESTDIR)$(mandir)/man5
	ginstall -m 644 $(WORKDIR)/djbdns-man/*.5 $(DESTDIR)$(mandir)/man5
	mkdir -p $(DESTDIR)$(mandir)/man8
	ginstall -m 644 $(WORKDIR)/djbdns-man/*.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)
