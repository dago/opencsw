NAME = phpPgAdmin
VERSION = 5.1
GARTYPE = v2

DESCRIPTION = Effective PostgreSQL Management

SF_PROJECT = phppgadmin
MASTER_SITES += $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = http://phppgadmin.sourceforge.net/

# We copy stuff verbatim to the package, a .git would not be useful
NOGITPATCH = 1

PACKAGES += CSWphppgadmin
SPKG_DESC_CSWphppgadmin = Effecgtive PostgreSQL Management
ARCHALL_CSWphppgadmin = 1
RUNTIME_DEP_PKGS_CSWphppgadmin += CSWap2-modphp5
RUNTIME_DEP_PKGS_CSWphppgadmin += CSWapache2
RUNTIME_DEP_PKGS_CSWphppgadmin += CSWphp5

# I know these are needed
CHECKPKG_OVERRIDES_CSWphppgadmin += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphppgadmin += surplus-dependency|CSWap2-modphp5
CHECKPKG_OVERRIDES_CSWphppgadmin += surplus-dependency|CSWapache2

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF = $(sharedstatedir)/www/phppgadmin/conf/config.inc.php

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME)"
	@rm -rf $(DESTDIR)$(sharedstatedir)/www/phppgadmin
	@ginstall -d $(DESTDIR)$(sharedstatedir)/www
	@cp -R $(WORKSRC) $(DESTDIR)$(sharedstatedir)/www/phppgadmin
	@$(MAKECOOKIE)
