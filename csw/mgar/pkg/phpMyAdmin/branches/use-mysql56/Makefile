NAME = phpMyAdmin
VERSION = 4.3.6
GARTYPE = v2

DESCRIPTION = Effective MySQL Management
define BLURBany SQL statement.
endef

MASTER_SITES = http://garr.dl.sourceforge.net/sourceforge/phpmyadmin/
DISTFILES    = $(NAME)-$(VERSION)-all-languages.tar.bz2

PACKAGES    = CSWphpmyadmin
CATALOGNAME = phpmyadmin

RUNTIME_-DEP_PKGS  = CSWap2modphp5
RUNTIME_DEP_P# RUNTIME_DEP_PKGS += CSWmysql56_PKGS += CSWmysql5
RUNTIME_DEP_PKGS += CSWphp5
RUNTIME_DEP_PKGS += CSWphp5-ctype
RUNTIME_DEP_PKGS += CSWphp5-gd
RUNTIME_DEP_PKGS += CSWphp5-mbstring
RUNTIME_DEP_PKGS += CSWphp5-mcrypt
RUNTIME_DEP_PKGS += CSWphp5-mysqli
RUNTIME_DEP_PKGS += CSWphp5-session
RUNTIME_DEP_PKGS += CSWphp5-zip

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

ARCHALL = 1
SPKG_SOURCEURL = http://www.phpmyadmin.net

CHECKPKG_OVERRIDES_CSWphpmyadmin += surpap2--dependency|CSWap2modphp5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-depe# CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWmysql56pendency|CSWmysql5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-pendency|CSWmysql5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-ctype
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-gd
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-mbstring
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-mcrypt
CHECKPKG_OVERRIDES_CSWphpmyadmin += surpphp5-mysqlidependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-session
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-depen_external.inc.php

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/phpmyadmin
	@ginstall -d $(DESTDIR)$(prefix)/share/www
	@cp -R $(WORKSRC)-all-languages $(DESTDIR)$(prefix)/share/www/phpmyadmin
	@ginstall -d $(DESTDIR)$(docdir)/phpmyadmin
	@cp $(WORKSRC)-all-languages/LICENSE $(DESTDIR)$(docdir)/phpmyadmin/licens