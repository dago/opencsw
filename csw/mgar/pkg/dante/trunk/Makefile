# Todo
# * Ponder about the SOCKS_CONF / issetguid() issue
GARNAME = dante
GARVERSION = 1.1.19
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

MASTER_SITES = ftp://ftp.inet.no/pub/socks/
MASTER_SITES += ftp://ftp.inet.no/pub/socks/old/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
SPKG_SOURCEURL = http://www.inet.no/dante/
LICENSE = LICENSE

PACKAGES = CSWlibsocks CSWdante

SPKG_DESC_CSWlibsocks = Dante SOCKS runtime libraries (and socksify wrapper)
SPKG_DESC_CSWdante = Dante SOCKS (v4 and v5) proxy daemon
SPKG_CLASSES_CSWdante = none cswinitsmf

# There is no pkg compiling against dante right now, just drop the .h file
EXTRA_MERGE_EXCLUDE_FILES = $(includedir)/socks.h

PKGFILES_CSWlibsocks = $(PKGFILES_RT) .*socks.*
PKGFILES_CSWlibsocks += $(docdir)/libsocks/.*
PKGFILES_CSWdante = .*sockd.* /etc/opt/csw/init.d/cswdante
PKGFILES_CSWdante += $(docdir)/dante/.*

REQUIRED_PKGS_CSWdante = CSWlibsocks CSWcswclassutils CSWtcpwrap

# CSWlibsocks not yet installed on the build farm
ENABLE_CHECK = 0

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Make the man pages reference our CSW locations instead of /etc/*.conf
PATCHFILES = man-conflocations.diff

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-socks-conf=$(sysconfdir)/socks.conf
CONFIGURE_ARGS += --with-sockd-conf=$(sysconfdir)/sockd.conf
CONFIGURE_ARGS += --with-pidfile=/var/opt/csw/run/sockd.pid

# Don't bother about the "not found" modules after the ./configure run,
# they are commercial add-ons (http://www.inet.no/dante/module.html).

PROTOTYPE_FILTER  = awk '\
	$$$$3 ~ /\/init.d\/cswdante$$$$/ { $$$$2 = "cswinitsmf" } \
    { print }'

include gar/category.mk

# The SOCKS_CONF and issetugid() issue needs some thought. Are there any
# secure alternative to the simple get{ug}id below? Could ask upstream.
#
# Fix missing issetugid on Solaris 8, it is not nice, but the best i can
# come up with for now, ref. 
#   http://bugs.gentoo.org/attachment.cgi?id=180390
#   issetugid(2) on a Solaris 10 box (WRT to concerns)
#
# If at all this needs to be revamped into a patch for libscompat/issetugid.c
#post-extract-modulated:
#	@perl -pi -e '\
#		s/int issetugid __P\(\(void\)\)/#define issetugid() (getuid() != geteuid()) || (getgid() != getegid())/' \
#			$(WORKSRC)/include/common.h
#	@$(MAKECOOKIE)


post-configure-modulated:
	# Get rid of -misalign which is meant for /usr/ucb/cc
	@perl -pi -e 's|-misalign || if /^CFLAGS =/' $(WORKSRC)/*/Makefile
ifneq ($(GARFLAVOR),DBG)
	# Get rid of -g. 
	# configure wants to use -g even if --disable-debugging (default)
	@perl -pi -e 's#-(g|xs|xO0) ##g if /^CFLAGS =/' $(WORKSRC)/*/Makefile
endif
	@$(MAKECOOKIE)

post-install-libsocks: DOCDEST = $(DESTDIR)$(docdir)/libsocks
post-install-libsocks: DOCS = CREDITS NEWS SUPPORT
post-install-libsocks: CSWDOCS = README.CSW changelog.CSW
post-install-libsocks:
	@ginstall -d $(DOCDEST)/examples
	@cp $(WORKSRC)/example/socks*.conf $(DOCDEST)/examples
	@$(foreach D,$(DOCS),    cp $(WORKSRC)/$(D) $(DOCDEST);)
	@$(foreach D,$(CSWDOCS), cp $(FILEDIR)/$(D) $(DOCDEST);)
	@$(MAKECOOKIE)


post-install-dante: DOCDEST = $(DESTDIR)$(docdir)/dante
post-install-dante: DOCS = CREDITS NEWS SUPPORT
post-install-dante: CSWDOCS = changelog.CSW
post-install-dante:
	@ginstall -d $(DOCDEST)/examples
	@cp $(WORKSRC)/example/sockd*.conf $(DOCDEST)/examples
	@$(foreach D,$(DOCS),    cp $(WORKSRC)/$(D) $(DOCDEST);)
	@$(foreach D,$(CSWDOCS), cp $(FILEDIR)/$(D) $(DOCDEST);)

	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 0755 $(FILEDIR)/CSWdante.cswdante \
		$(DESTDIR)/etc/opt/csw/init.d/cswdante

	# /var/opt/csw/run is not in CSWcommon
	@ginstall -d $(DESTDIR)/var/opt/csw/run
	@$(MAKECOOKIE)


post-install-modulated: post-install-libsocks post-install-dante
	@$(MAKECOOKIE)
