# Todo
# * Compare with current catalog package WRT to config file etc.
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

PACKAGES = CSWlibsocks CSWdante

SPKG_DESC_CSWlibsocks = Dante SOCKS runtime libraries (and socksify wrapper)
SPKG_DESC_CSWdante = Dante SOCKS (v4 and v5) proxy daemon
SPKG_CLASSES_CSWdante = none cswinitsmf

# There is no pkg compiling against dante right now, just drop the .h file
EXTRA_MERGE_EXCLUDE_FILES = $(includedir)/socks.h

PKGFILES_CSWlibsocks = $(PKGFILES_RT) .*socks.*
PKGFILES_CSWlibsocks += $(addprefix $(docdir)/$(GARNAME)/,NEWS SUPPORT CREDITS )
PKGFILES_CSWlibsocks += $(docdir)/$(GARNAME)/.*CSW
PKGFILES_CSWdante = .*sockd.* /etc/opt/csw/init.d/cswdante

REQUIRED_PKGS_CSWdante = CSWlibsocks CSWcswclassutils CSWtcpwrap

# CSWlibsocks not yet installed on the build farm
ENABLE_CHECK = 0

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

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

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: DOCS = CREDITS NEWS SUPPORT
post-install-modulated: CSWDOCS = README.CSW changelog.CSW
post-install-modulated:
	@ginstall -d $(DOCDEST)/examples
	@cp $(WORKSRC)/example/*.conf $(DOCDEST)/examples
	@$(foreach D,$(DOCS),    cp $(WORKSRC)/$(D) $(DOCDEST);)
	@$(foreach D,$(CSWDOCS), cp $(FILEDIR)/$(D) $(DOCDEST);)

	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWdante.cswdante $(DESTDIR)/etc/opt/csw/init.d/cswdante

	# /var/opt/csw/run is not in CSWcommon
	@ginstall -d $(DESTDIR)/var/opt/csw/run
	@$(MAKECOOKIE)
