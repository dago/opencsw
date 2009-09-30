GARNAME = phpMyAdmin
GARVERSION = 3.2.2
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
DISTFILES  = $(GARNAME)-$(GARVERSION)-all-languages.tar.bz2

PACKAGES = CSWphpmyadmin
CATALOGNAME = phpmyadmin

REQUIRED_PKGS  = CSWapache2 CSWap2modphp5 CSWmysql5 CSWphp5 CSWphp5gd CSWphp5mcrypt
REQUIRED_PKGS += CSWphp5mysqli CSWphp5session CSWphp5mbstring CSWphp5ctype CSWphp5zip

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-all-languages.tar.bz2

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1
SPKG_SOURCEURL = http://www.phpmyadmin.net

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/phpmyadmin
	@ginstall -d $(DESTDIR)$(prefix)/share/www
	@cp -R $(WORKSRC)-all-languages $(DESTDIR)$(prefix)/share/www/phpmyadmin
	@ginstall -d $(DESTDIR)$(docdir)/phpmyadmin
	@cp $(WORKSRC)-all-languages/LICENSE $(DESTDIR)$(docdir)/phpmyadmin/license
	@$(MAKECOOKIE)
