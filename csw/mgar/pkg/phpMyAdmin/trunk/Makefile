GARNAME = phpMyAdmin
GARVERSION = 3.1.2
CATEGORIES = apps

DESCRIPTION = Effective MySQL Management
define BLURB
  phpMyAdmin is a free software tool written in PHP intended to handle the 
  administration of MySQL over the World Wide Web. phpMyAdmin supports a wide range of 
  operations with MySQL. The most frequently used operations are supported by the user 
  interface (managing databases, tables, fields, relations, indexes, users, permissions, 
  etc), while you still have the ability to directly execute any SQL statement.
endef

MASTER_SITES = http://garr.dl.sourceforge.net/sourceforge/phpmyadmin/
DISTFILES  = $(GARNAME)-$(GARVERSION)-all-languages.tar.bz2
DISTFILES += $(call admfiles,CSWphpmyadmin,)

#SPKG_DESC_CSWap2modphp5  = PHP 5 - Apache 2.2.x Module
#SPKG_DESC_CSWmysql5      = MySQL 5 database management system - server files
#SPKG_DESC_CSWphp5gd      = PHP 5 - GD Extension
#SPKG_DESC_CSWphp5mcrypt  = PHP 5 - libmcrypt Extension
#SPKG_DESC_CSWphp5mysqli  = PHP 5 - MySQLi Extension
#SPKG_DESC_CSWphp5session = PHP 5 - Session Extension

REQUIRED_PKGS = CSWapache2 CSWap2modphp5 CSWmysql5 CSWphp5 CSWphp5gd CSWphp5mcrypt CSWphp5mysqli CSWphp5session

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*)-all-languages.tar.bz2

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.phpmyadmin.net

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/phpmyadmin
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@cp -R $(WORKSRC)-all-languages $(DESTDIR)$(prefix)/apache2/share/htdocs/phpmyadmin
	@ginstall -d $(DESTDIR)$(docdir)/phpmyadmin
	@cp $(WORKSRC)-all-languages/LICENSE $(DESTDIR)$(docdir)/phpmyadmin
	@$(MAKECOOKIE)
