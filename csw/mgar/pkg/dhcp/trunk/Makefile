GARNAME = dhcp
GARVERSION = 4.1.1b3
CATEGORIES = net

DESCRIPTION = ISC DHCP reference implementation
define BLURB
  ISC DHCP is open-source software that implements the Dynamic Host
  Configuration Protocols for connection to a local network. It is a reference
  implementation of those protocols, but it is also production-grade software,
  suitable for use in high-volume and high-reliability applications. 
endef

MASTER_SITES = http://ftp.isc.org/isc/dhcp/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

LICENSE = LICENSE

PACKAGES = CSWdhcp CSWdhcpdevel

REQUIRED_PKGS_CSWdhcp = CSWosslrt
SPKG_DESC_CSWdhcp = ISC DHCP reference implementation

REQUIRED_PKGS_CSWdhcpdevel = CSWdhcp
CATALOGNAME_CSWdhcpdevel = dhcp_devel
ARCHALL_CSWdhcpdevel = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = ($(GARNAME)-\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU
TEST_TARGET = check

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/dhcp

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWdhcpdevel = $(PKGFILES_DEVEL)

#ENABLE_CHECK = 0

INSTALL_SCRIPTS = custom

INITSMF = /etc/opt/csw/init.d/cswdhcpd
SAMPLECONF = /etc/opt/csw/dhcpd.conf /etc/opt/csw/dhclient.conf /var/opt/csw/dhcp/db/dhcpd.leases

SPKG_SOURCEURL = https://www.isc.org/software/dhcp

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWdhcp.cswdhcpd $(DESTDIR)/etc/opt/csw/init.d/cswdhcpd
	@chmod 755 $(DESTDIR)/etc/opt/csw/init.d/cswdhcpd
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(FILEDIR)/CSWdhcp.README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@ginstall -d $(DESTDIR)/var/opt/csw/$(GARNAME)/db
	@touch $(DESTDIR)/var/opt/csw/$(GARNAME)/db/dhcpd.leases
	@$(MAKECOOKIE)
