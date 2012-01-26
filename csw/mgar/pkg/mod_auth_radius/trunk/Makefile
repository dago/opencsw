NAME = mod_auth_radius
VERSION = 1.5.8
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Apache RADIUS authentication module
define BLURB
  This is the Apache RADIUS authentication module. It allows any Apache web-server
  to become a RADIUS client for authentication and accounting requests. You will,
  however, need to supply your own RADIUS server to perform the actual authentication.
endef

MASTER_SITES = ftp://ftp.freeradius.org/pub/radius/
DISTFILES  = $(NAME)-$(VERSION).tar
DISTFILES += CSWap2modauthradius.postinstall CSWap2modauthradius.preremove
DISTFILES += COPYING

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar

VENDOR_URL = http://freeradius.org/mod_auth_radius/

PACKAGES = CSWap2modauthradius
CATALOGNAME = ap2_mod_auth_radius

DEP_PKGS = CSWapache2
CHECKPKG_OVERRIDES_CSWap2modauthradius += surplus-dependency|CSWapache2

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_EXTRACONF = $(DESTDIR)$(AP2_ROOT)/etc/extra
AP2_SBIN      = $(AP2_ROOT)/sbin
APXS          = $(AP2_SBIN)/apxs

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

PRESERVECONF = $(prefix)/apache2/etc/extra/httpd-auth-radius.conf

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(APXS) -c mod_auth_radius-2.0.c
	$(MAKECOOKIE)

install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
install-custom:
	mkdir -p $(AP2_LIBEXEC)
	cd $(WORKSRC) && $(APXS) -S LIBEXECDIR=$(AP2_LIBEXEC) -i mod_auth_radius-2.0.la
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 $(WORKSRC)/httpd.conf $(DESTDIR)$(prefix)/apache2/etc/extra/httpd-auth-radius.conf
	ginstall -d $(DOCDEST)
	ginstall $(WORKSRC)/README $(DOCDEST)
	@$(MAKECOOKIE)




