NAME = phpMyAdmin
VERSION = 3.5.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Effective MySQL Management
define BLURB
  phpMyAdmin is a free software tool written in PHP intended to handle the 
  administration of MySQL over the World Wide Web. phpMyAdmin supports a wide
  range of operations with MySQL. The most frequently used operations are
  supported by the user interface (managing databases, tables, fields,
  relations, indexes, users, permissions, etc), while you still have the
  ability to directly execute any SQL statement.
endef

MASTER_SITES = http://garr.dl.sourceforge.net/sourceforge/phpmyadmin/
DISTFILES    = $(NAME)-$(VERSION)-all-languages.tar.bz2

PACKAGES    = CSWphpmyadmin
CATALOGNAME = phpmyadmin

RUNTIME_DEP_PKGS  = CSWap2modphp5
RUNTIME_DEP_PKGS += CSWapache2
RUNTIME_DEP_PKGS += CSWmysql5
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

CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-session
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-zip
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-gd
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-mbstring
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-mcrypt
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWap2modphp5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWmysql5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-ctype
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5-mysqli
# Only a comment
CHECKPKG_OVERRIDES_CSWphpmyadmin += file-with-bad-content|/usr/share|root/opt/csw/share/www/phpmyadmin/libraries/vendor_config.php
# Only a comment
CHECKPKG_OVERRIDES_CSWphpmyadmin += file-with-bad-content|/usr/local|root/opt/csw/share/www/phpmyadmin/libraries/transformations/text_plain__external.inc.php

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/phpmyadmin
	@ginstall -d $(DESTDIR)$(prefix)/share/www
	@cp -R $(WORKSRC)-all-languages $(DESTDIR)$(prefix)/share/www/phpmyadmin
	@ginstall -d $(DESTDIR)$(docdir)/phpmyadmin
	@cp $(WORKSRC)-all-languages/LICENSE $(DESTDIR)$(docdir)/phpmyadmin/license
	@$(MAKECOOKIE)
