# Known issue:
# - The libsocks build doesn't support $SOCKS_CONF. See README.CSW
#   and INSTALL with its description of `--without-glibc-secure'.
#
# Todo:
# - Look into kerberos linking issues
# - Test sockd and its init script
GARNAME = dante
GARVERSION = 1.2.0
CATEGORIES = net

DESCRIPTION = Dante SOCKS packages
define BLURB
  Dante is a circuit-level firewall/proxy that can be used to provide
  convenient and secure network connectivity to a wide range of hosts
  while requiring only the server Dante runs on to have external network
  connectivity.
  
  Once installed, Dante can in most cases be made transparent to the
  clients while offering detailed access control and logging facilities to
  the server administrator. 
endef

SPKG_SOURCEURL = http://www.inet.no/dante/
MASTER_SITES   = ftp://ftp.inet.no/pub/socks/
MASTER_SITES  += ftp://ftp.inet.no/pub/socks/old/
DISTFILES      = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX   = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

PACKAGES = CSWlibsocks CSWdante

SPKG_DESC_CSWlibsocks = Dante SOCKS runtime libraries (and socksify wrapper)
SPKG_DESC_CSWdante = Dante SOCKS (v4 and v5) proxy daemon

# There is no pkg compiling against dante right now, just drop the dev files
EXTRA_MERGE_EXCLUDE_FILES = $(includedir)/.*

PKGFILES_CSWlibsocks  = $(PKGFILES_RT) .*socks.*
PKGFILES_CSWlibsocks += $(docdir)/libsocks/.*
PKGFILES_CSWdante     = .*sockd.* /etc/opt/csw/init.d/cswdante
PKGFILES_CSWdante    += $(docdir)/dante/.*

REQUIRED_PKGS_CSWdante = CSWtcpwrap

TEST_SCRIPTS =

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

# Don't bother about the "not found" modules after the ./configure run,
# they are commercial add-ons (http://www.inet.no/dante/module.html).
# 
# Features disabled via --without will be also stated as "not found" 
# in the summary messages that ./configure displays at the end

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-socks-conf=$(sysconfdir)/socks.conf
CONFIGURE_ARGS += --with-sockd-conf=$(sysconfdir)/sockd.conf
CONFIGURE_ARGS += --with-pidfile=/var/run/cswsockd.pid
CONFIGURE_ARGS += --without-glibc-secure

# Kerberos linking fails .. looks like it is missing -L/opt/csw/lib.
# Needs investigation.
CONFIGURE_ARGS += --without-gssapi

# UPNP support requires miniupnp from http://miniupnp.free.fr/
CONFIGURE_ARGS += --without-upnp


INITSMF = /etc/opt/csw/init\.d/cswdante

include gar/category.mk

post-configure-modulated:
ifneq ($(GARFLAVOR),DBG)
	# Get rid of debugging flags which ./configure determines per default
	perl -pi -e 's#-(g|xs|xO0) ##g if /^CFLAGS =/' $(WORKSRC)/*/Makefile
endif
	@$(MAKECOOKIE)

post-install-libsocks: DOCDEST = $(DESTDIR)$(docdir)/libsocks
post-install-libsocks: DOCS = CREDITS NEWS SUPPORT
post-install-libsocks: CSWDOCS = README.CSW changelog.CSW
post-install-libsocks:
	ginstall -d $(DOCDEST)/examples
	cp $(WORKSRC)/example/socks*.conf $(DOCDEST)/examples
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(addprefix $(FILEDIR)/,$(CSWDOCS)) $(DOCDEST)
	@$(MAKECOOKIE)


post-install-dante: DOCDEST = $(DESTDIR)$(docdir)/dante
post-install-dante: DOCS = CREDITS NEWS SUPPORT
post-install-dante: CSWDOCS = changelog.CSW
post-install-dante:
	ginstall -d $(DESTDIR)/var/opt/csw/dante
	ginstall -d $(DOCDEST)/examples
	cp $(WORKSRC)/example/sockd*.conf $(DOCDEST)/examples
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(addprefix $(FILEDIR)/,$(CSWDOCS)) $(DOCDEST)

	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 0755 $(FILEDIR)/CSWdante.cswdante \
		$(DESTDIR)/etc/opt/csw/init.d/cswdante
	@$(MAKECOOKIE)

# Make the man pages reference our CSW locations instead of /etc/*.conf
fix-manpages:
	gsed -i \
		-e 's,/etc/socks.conf,$(sysconfdir)/socks.conf,' \
		-e 's,/etc/sockd.conf,$(sysconfdir)/sockd.conf,' \
		$(DESTDIR)$(mandir)/man1/socksify.1 \
		$(DESTDIR)$(mandir)/man5/socks.conf.5 \
		$(DESTDIR)$(mandir)/man5/sockd.conf.5 \
		$(DESTDIR)$(mandir)/man8/sockd.8
	@$(MAKECOOKIE)

post-install-modulated: post-install-libsocks post-install-dante fix-manpages
	@$(MAKECOOKIE)
