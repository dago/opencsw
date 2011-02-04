NAME = mod_auth_kerb
VERSION = 5.4
CATEGORIES = server

DESCRIPTION = Apache Kerberos authentication module
define BLURB
  This is the Apache RADIUS authentication module. It allows any Apache web-server
  to become a RADIUS client for authentication and accounting requests. You will,
  however, need to supply your own RADIUS server to perform the actual authentication.
endef

SF_PROJ = modauthkerb
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWap2modauthkerb.postinstall
DISTFILES += CSWap2modauthkerb.preremove

PATCHFILES += 0001-Fix-install-destination.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://modauthkerb.sourceforge.net/
LICENSE = LICENSE

PACKAGES = CSWap2modauthkerb
CATALOGNAME = ap2_mod_auth_kerb
RUNTIME_DEP_PKGS_CSWap2modauthkerb += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWap2modauthkerb += CSWapache2
CHECKPKG_OVERRIDES_CSWap2modauthkerb += surplus-dependency|CSWapache2

# That path is almost ok
CHECKPKG_OVERRIDES_CSWap2modauthkerb += bad-rpath-entry|/opt/csw/lib/|opt/csw/apache2/libexec/mod_auth_kerb.so

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --without-krb4
CONFIGURE_ARGS += --with-krb5=$(prefix)
CONFIGURE_ARGS += --with-apache=$(prefix)/apache2

# The package does not provide a check
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS = AP2_LIBEXEC
INSTALL_OVERRIDE_VAR_AP2_LIBEXEC = $(AP2_LIBEXEC)

include gar/category.mk

pre-install-modulated:
	ginstall -d $(AP2_LIBEXEC)
	ginstall -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	ginstall $(WORKSRC)/README $(WORKSRC)/INSTALL $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@$(MAKECOOKIE)
