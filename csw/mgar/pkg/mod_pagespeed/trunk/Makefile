NAME = mod_pagespeed
VERSION = 0.10.21.2
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Apache Kerberos authentication module
define BLURB
  This is the Apache RADIUS authentication module. It allows any Apache web-server
  to become a RADIUS client for authentication and accounting requests. You will,
  however, need to supply your own RADIUS server to perform the actual authentication.
endef

GOOGLE_PROJ = modpagespeed
MASTER_SITES = svn-http://modpagespeed.googlecode.com/svn/tags/
DISTFILES += $(VERSION)
NOCHECKSUM += $(VERSION)
DISTNAME = $(VERSION)

VENDOR_URL = http://code.google.com/p/modpagespeed/

PACKAGES = CSWap2-mod-pagespeed
RUNTIME_DEP_PKGS_CSWap2-mod-pagespeed += CSWapache2
CHECKPKG_OVERRIDES_CSWap2-mod-pagespeed += surplus-dependency|CSWapache2

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-apache=$(prefix)/apache2

# The package does not provide a check
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS = AP2_LIBEXEC
INSTALL_OVERRIDE_VAR_AP2_LIBEXEC = $(AP2_LIBEXEC)

AP2_MODS = 1
AP2_MODFILES += \*auth_kerb\*so

include gar/category.mk

pre-install-modulated:
	ginstall -d $(AP2_LIBEXEC)
	ginstall -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	ginstall $(WORKSRC)/README $(WORKSRC)/INSTALL $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@$(MAKECOOKIE)
