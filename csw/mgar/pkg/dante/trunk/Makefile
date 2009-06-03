# Todo
# * Add changelog.CSW
# * Compare with current catalog package WRT to config file etc.
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

PACKAGES = CSWlibsocks CSWdante CSWdanteclient

SPKG_DESC_CSWlibsocks = Dante SOCKS runtime libraries
SPKG_DESC_CSWdante = Dante SOCKS (v4 and v5) proxy daemon
SPKG_DESC_CSWdanteclient = Dante SOCKS wrapper to SOCKsify applications
SPKG_CLASSES_CSWdante = none cswinitsmf

CATALOGNAME_CSWdanteclient = dante-client

# There is no pkg compiling against dante right now, just drop the
# header file
EXTRA_MERGE_EXCLUDE_FILES = $(includedir)/socks.h

# Would have liked to keep it simple and just put *.sockd.* and
# *.socks.* in the server/client package, but then some _RT end up in
# the client package also. Seems as if files can be matched by multiple
# packages.
PKGFILES_CSWlibsocks = $(PKGFILES_RT)
PKGFILES_CSWdante = .*sockd.* /etc/opt/csw/init.d/cswdante
PKGFILES_CSWdanteclient = $(mandir)/.*socks.*
PKGFILES_CSWdanteclient += $(docdir)/.*socks.*
PKGFILES_CSWdanteclient += $(bindir)/.*socks.*

REQUIRED_PKGS_CSWdante = CSWlibsocks CSWcswclassutils CSWtcpwrap
REQUIRED_PKGS_CSWdanteclient = CSWlibsocks

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

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: DOCS = CREDITS NEWS SUPPORT
post-install-modulated:
	@ginstall -d $(DOCDEST)/examples
	@cp $(WORKSRC)/example/*.conf $(DOCDEST)/examples
	@$(foreach D,$(DOCS),cp $(WORKSRC)/$(D) $(DOCDEST);)

	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWdante.cswdante $(DESTDIR)/etc/opt/csw/init.d/cswdante

	# /var/opt/csw/run is not in CSWcommon
	@ginstall -d /var/opt/csw/run
	@$(MAKECOOKIE)
