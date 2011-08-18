NAME = dhcp
VERSION = 4.2.2
#RELEASE = P1
#DISTVERSION = $(VERSION)-$(RELEASE)
#SPKG_VERSION = $(VERSION)$(RELEASE)
#DISTNAME = $(NAME)-$(VERSION)-$(RELEASE)
#WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = ISC DHCP reference implementation
define BLURB
  ISC DHCP is open-source software that implements the Dynamic Host
  Configuration Protocols for connection to a local network. It is a reference
  implementation of those protocols, but it is also production-grade software,
  suitable for use in high-volume and high-reliability applications. 
endef

MASTER_SITES = http://ftp.isc.org/isc/dhcp/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = LICENSE

PACKAGES += CSWdhcp
RUNTIME_DEP_PKGS_CSWdhcp = CSWosslrt
SPKG_DESC_CSWdhcp = ISC DHCP reference implementation

PACKAGES += CSWdhcp-dev
RUNTIME_DEP_PKGS_CSWdhcp-dev = CSWdhcp
SPKG_DESC_CSWdhcp-dev = ISC DHCP development package
CATALOGNAME_CSWdhcp-dev = dhcp_dev

GARCOMPILER = GNU
TEST_TARGET = check

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/dhcp

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWdhcp-dev = $(PKGFILES_DEVEL)

#ENABLE_CHECK = 0

INSTALL_SCRIPTS = custom

INITSMF     = /etc/opt/csw/init.d/cswdhcpd
SAMPLECONF  = /etc/opt/csw/dhcpd.conf
SAMPLECONF += /etc/opt/csw/dhclient.conf
SAMPLECONF += /var/opt/csw/dhcp/db/dhcpd.leases

SPKG_SOURCEURL = https://www.isc.org/software/dhcp

CHECKPKG_OVERRIDES_CSWdhcp += surplus-dependency|CSWosslrt

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	  gmake DESTDIR=$(DESTDIR) install )
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWdhcp.cswdhcpd $(DESTDIR)/etc/opt/csw/init.d/cswdhcpd
	@chmod 755 $(DESTDIR)/etc/opt/csw/init.d/cswdhcpd
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@cp $(FILEDIR)/CSWdhcp.README.CSW $(DESTDIR)$(docdir)/$(NAME)/README.CSW
	@ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/db
	@touch $(DESTDIR)/var/opt/csw/$(NAME)/db/dhcpd.leases
	@$(MAKECOOKIE)
