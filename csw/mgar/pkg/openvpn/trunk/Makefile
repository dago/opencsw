NAME = openvpn
VERSION = 2.0.9
GARTYPE = v1
CATEGORIES = server

DESCRIPTION = secure IP tunnel daemon
define BLURB
OpenVPN is a full-featured SSL VPN solution which can accomodate a wide range of configurations, including remote access, site-to-site VPNs, WiFi security, and enterprise-scale remote access solutions with load balancing, failover, and fine-grained access-controls
endef

# master files
MASTER_SITES = http://openvpn.net/release/
DISTFILES = $(NAME)-$(VERSION).tar.gz

# we require
RUNTIME_DEP_PKGS = CSWosslrt CSWlzo

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = --prefix=$(prefix) --mandir=/opt/csw/share/man
PATCHFILES = patch.openvpn-2.0.9.tun.c

# use classes for install/removal
PRESERVECONF = $(sysconfdir)/$(NAME)/$(NAME).conf.CSW
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
		$(DESTDIR)$(sysconfdir)/$(NAME)/$(NAME).conf.CSW
	@echo "Installing start/stop script"
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswopenvpn  \
		$(DESTDIR)/etc/opt/csw/init.d/cswopenvpn
	@$(MAKECOOKIE)
