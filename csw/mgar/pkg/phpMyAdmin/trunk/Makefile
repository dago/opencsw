NAME = phpMyAdmin
VERSION = 3.4.5
CATEGORIES = apps

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
DISTFILES  = $(NAME)-$(VERSION)-all-languages.tar.bz2

PACKAGES = CSWphpmyadmin
CATALOGNAME = phpmyadmin

RUNTIME_DEP_PKGS  = CSWapache2 CSWap2modphp5 CSWmysql5 CSWphp5 CSWphp5gd CSWphp5mcrypt
RUNTIME_DEP_PKGS += CSWphp5mysqli CSWphp5session CSWphp5mbstring CSWphp5ctype CSWphp5zip

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1
SPKG_SOURCEURL = http://www.phpmyadmin.net

CHECKPKG_OVERRIDES_CSWphpmyadmin += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5session
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5zip
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5gd
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5mbstring
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5mcrypt
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWap2modphp5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWmysql5
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5ctype
CHECKPKG_OVERRIDES_CSWphpmyadmin += surplus-dependency|CSWphp5mysqli
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
