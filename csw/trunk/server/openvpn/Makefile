GARNAME = openvpn
GARVERSION = 2.0.7
CATEGORIES = server

DESCRIPTION = secure IP tunnel daemon
define BLURB
OpenVPN is a full-featured SSL VPN solution which can accomodate a wide range of configurations, including remote access, site-to-site VPNs, WiFi security, and enterprise-scale remote access solutions with load balancing, failover, and fine-grained access-controls
endef

MASTER_SITES = http://openvpn.net/release/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWopenvpn, prototype )

CONFIGURE_ARGS  = --prefix=$(prefix) --mandir=/opt/csw/share/man

TEST_SCRIPTS =

include ../category.mk

post-install:
	( cp -r $(WORKSRC)/../../../files/etc $(DESTDIR)/etc )
	( mkdir -p $(DESTDIR)/etc/csw/easy-rsa )
	( cp -r $(WORKSRC)/easy-rsa $(DESTDIR)/etc/csw/easy-rsa )
	@$(MAKECOOKIE)
