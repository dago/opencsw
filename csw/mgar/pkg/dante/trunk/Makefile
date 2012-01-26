# Known limitation:
# - The libsocks build doesn't support $SOCKS_CONF. See README.CSW
#   and INSTALL with its description of `--without-glibc-secure'.
#
# Known issues:
# - When compiled with GSSAPI/Kerberos support, socksify core dumps
#   at the end of the connection (when all data has been transmitted).
#   To reproduce: /opt/csw/bin/socksify wget -qO http://google.com
#   Observed on Solaris 10 U7 x86 with CSWkrb5lib 1.4.4,REV=2006.12.27.
#   Not investigated in depth. If anyone needs Kerberos support, feel
#   free to tackle this. Might be bug in Dante, might have to do with
#   the LIBTOOL hack (see pre-configure-modulated) or might also
#   originate in our downrev Kerberos libs.
#
NAME = dante
VERSION = 1.2.1
CATEGORIES = net
GARTYPE = v2

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

VENDOR_URL     = http://www.inet.no/dante/
MASTER_SITES   = ftp://ftp.inet.no/pub/socks/
MASTER_SITES  += ftp://ftp.inet.no/pub/socks/old/
DISTFILES      = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX   = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

# See doc/README.usage: dante is stand-alone. libsocks can be used to 
# compile or run-time link applications against the SOCKS library
PACKAGES = CSWdante CSWlibsocks

SPKG_DESC_CSWdante    = Dante SOCKS (v4 and v5) proxy daemon
SPKG_DESC_CSWlibsocks = Dante SOCKS library (and socksify wrapper) to socksify applications

PKGFILES_CSWdante     = .*sockd.* /etc/opt/csw/init.d/cswdante
PKGFILES_CSWdante    += $(docdir)/dante/.*
PKGFILES_CSWlibsocks  = $(PKGFILES_RT) .*socks.*
PKGFILES_CSWlibsocks += $(docdir)/libsocks/.*
PKGFILES_CSWlibsocks += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWdante    = CSWtcpwrap

# dante doesn't come with a test suite
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
# UPNP support requires miniupnp from http://miniupnp.free.fr/
CONFIGURE_ARGS += --without-upnp
# See "Known issues" at the top of this Makefile
CONFIGURE_ARGS += --without-gssapi

SAMPLECONF  = $(sysconfdir)/socks.conf
SAMPLECONF += $(sysconfdir)/sockd.conf
INITSMF     = /etc/opt/csw/init\.d/cswdante

EXTRA_PAX_ARGS = '-s,NEWS$$,changelog,p'

include gar/category.mk

pre-configure-modulated:
	# Kerberos linking fails with the shipped libtool, so make ./configure
	# use /opt/csw/bin/libtool (similar to what Debian does). See
	# http://article.gmane.org/gmane.os.solaris.opencsw.maintainers/5275
	# Disabled for now, c.f. "Known issues" at the top of this Makefile
	#gsed -ie 's,^LIBTOOL=.*,LIBTOOL=/opt/csw/bin/libtool,' \
	#	$(WORKSRC)/configure
	@$(MAKECOOKIE)

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

	ginstall -d $(DESTDIR)$(sysconfdir)
	cp $(FILEDIR)/socks.conf.CSW $(DESTDIR)$(sysconfdir)/socks.conf

	# /bin/sh doesn't understand "if ! test", reported to dante-bugs@inet.no
	# for 1.2.0. Should have be fixed in the next release, but wasn't with 1.2.1.
	# Upon version bump, verify and drop if obsolete.
	gsed -i -e 's,/bin/sh,/usr/bin/bash,' $(DESTDIR)$(bindir)/socksify
	@$(MAKECOOKIE)


post-install-dante: DOCDEST = $(DESTDIR)$(docdir)/dante
post-install-dante: DOCS = CREDITS NEWS SUPPORT
post-install-dante: CSWDOCS = README.CSW changelog.CSW
post-install-dante:
	ginstall -d $(DESTDIR)/var/opt/csw/dante
	ginstall -d $(DOCDEST)/examples
	cp $(WORKSRC)/example/sockd*.conf $(DOCDEST)/examples
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(addprefix $(FILEDIR)/,$(CSWDOCS)) $(DOCDEST)

	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 0755 $(FILEDIR)/cswdante \
		$(DESTDIR)/etc/opt/csw/init.d/cswdante

	ginstall -d $(DESTDIR)$(sysconfdir)
	cp $(FILEDIR)/sockd.conf.CSW $(DESTDIR)$(sysconfdir)/sockd.conf

	# This is where sockd.log goes, ref. $(FILEDIR)/sockd.conf.CSW
	ginstall -d $(DESTDIR)$(localstatedir)/dante
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
