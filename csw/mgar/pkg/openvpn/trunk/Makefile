NAME = openvpn
VERSION = 2.0.9
GARTYPE = v2

DESCRIPTION = Sver

DESCRIPTION = secure IP tunnel daemon
define BLURB
OpenVPN is a full-featured SSL VPN solution which can accomodate a wide range of configurations, including remote access, site-to-site VPNs, WiFi security, and enterprise-scale remote access solutions with load balancing, failover, and fine-grained access-controls
endef

# master files
MASTER_SITES = http://openvpn.net/release/
DISTFILES = $(NAME)-$(VERSION).tar.gz

# we require
RUlibssl1-0-0 CSWliblzo2-2

# The references are located in document or sample files and are harmless
CHECKPKG_OVERRIDES_CSWopenvpn += file-with-bad-content|/usr/share|root/opt/csw/share/doc/openvpn/easy-rsa/vars
CHECKPKG_OVERRIDES_CSWopenvpn += file-with-bad-content|/usr/share|root/opt/csw/share/doc/openvpn/easy-rsa/2.0/vars
CHECKPKG_OVERRIDES_CSWopenvpn += file-with-bad-content|/usr/share|root/opt/csw/share/doc/openvpn/easy-rsa/2.0/Makefile
CHECKPKG_OVERRIDES_CSWopenvpn += file-with-bad-content|/usr/share|root/opt/csw/share/man/man8/openvpn.8
CHECKPKG_OVERRIDES_CSWopenvpn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/openvpn/sample-scripts/openvpn.init

# The perl script use SUNW perl and not CSW perl
CHECKPKG_OVERRIDES_CSWopenvpn += missing-dependency|CSWperlS = CSWosslrt CSWlzo

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = --prefix=$(prefix) --mandir=/opt/csw/share/man
PATCHFILES = patch.openvpn-2.0.9.tun.c

# use classes for install/removal
PRESERVECONF = $(sysconfdir)/ME)/$(NAME).conf.CSW
INITSMF = /etc/opt/csw/init.d/cswopenvpn

# no build tests
SKIPTEST = 1

include gar/category.mk

post-install-modulated:
	@echo "Installing sample files"
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	@cp -pr $(WORKSRC)/easy-rsa $(DESTDIR)$(docdir)/$(NAME)
	@cp -pr $(WORKSRC)/sample-scripts $(DESTDIR)$(docdir)/$(NAME)
	@cp -pr $(WORKSRC)/sample-config-files $(DESTDIR)$(docdir)/$(NAME)
	@echo "Installing $(NAME).conf.CSW"
	@ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/$(NAME)
	@cp -pr $(WORKSRC)/sample-config-files/server.conf \
		$(DESTDIR)$(sysconfdir)/ME)/$(NAME).conf.CSW
	@echo "Installing start/stop script"
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswopenvpn  \
		$(DESTDIR)/etc/opt/csw/init.d/cswopen