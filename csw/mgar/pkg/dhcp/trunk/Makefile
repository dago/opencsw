GARNAME = dhcp
GARVERSION = 4.1.1b2
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

PACKAGES = CSWdhcp CSWdhcpdevel
CATALOGNAME_CSWdhcpdevel = dhcp_devel
SPKG_DESC_CSWdhcp = ISC DHCP reference implementation
LICENSE = LICENSE

REQUIRED_PKGS_CSWdhcp = CSWcswclassutils CSWosslrt
REQUIRED_PKGS_CSWdhcpdevel = CSWdhcp

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

GARCOMPILER = GNU
TEST_TARGET = check

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/dhcp

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWdhcpdevel = $(PKGFILES_DEVEL)

#ENABLE_CHECK = 0

INSTALL_SCRIPTS = custom

PROTOTYPE_FILTER  = awk ' \
  $$$$3 ~ /\/init.d\/cswdhcpd$$$$/ { $$$$2 = "cswinitsmf" } \
  $$$$3 ~ /\/dhcpd.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
  $$$$3 ~ /\/dhclient.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
  $$$$3 ~ /\/dhcpd.leases.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
  { print }'

SPKG_SOURCEURL = https://www.isc.org/software/dhcp
SPKG_CLASSES_CSWdhcp = none cswcpsampleconf cswinitsmf

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWdhcp.cswdhcpd $(DESTDIR)/etc/opt/csw/init.d/cswdhcpd
	@chmod 755 $(DESTDIR)/etc/opt/csw/init.d/cswdhcpd
	@( cd $(DESTDIR)/etc/opt/csw ; \
	   mv dhcpd.conf dhcpd.conf.CSW ; \
	   mv dhclient.conf dhclient.conf.CSW )
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(FILEDIR)/CSWdhcp.README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@ginstall -d $(DESTDIR)/var/opt/csw/$(GARNAME)/db
	@touch $(DESTDIR)/var/opt/csw/$(GARNAME)/db/dhcpd.leases.CSW
	@$(MAKECOOKIE)
