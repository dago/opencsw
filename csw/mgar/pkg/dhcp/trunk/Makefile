NAME = dhcp
VERSION = 4.2.0
RELEASE = P2
DISTVERSION = $(VERSION)-$(RELEASE)
SPKG_VERSION = $(VERSION)$(RELEASE)
DISTNAME = $(NAME)-$(VERSION)-$(RELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)
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

PACKAGES = CSWdhcp CSWdhcpdevel

RUNTIME_DEP_PKGS_CSWdhcp = CSWosslrt
SPKG_DESC_CSWdhcp = ISC DHCP reference implementation

RUNTIME_DEP_PKGS_CSWdhcpdevel = CSWdhcp
SPKG_DESC_CSWdhcpdevel = ISC DHCP development package
CATALOGNAME_CSWdhcpdevel = dhcp_devel
ARCHALL_CSWdhcpdevel = 1

UFILES_REGEX = ($(NAME)-\d+(?:\.\d+)*).tar.gz

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

CHECKPKG_OVERRIDES_CSWdhcpdevel += archall-devel-package

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
