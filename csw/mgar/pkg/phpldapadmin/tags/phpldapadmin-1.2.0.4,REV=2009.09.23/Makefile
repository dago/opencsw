GARNAME = phpldapadmin
GARVERSION = 1.2.0.4
CATEGORIES = apps

DESCRIPTION = Web-based LDAP browser to manage your LDAP server
define BLURB
  phpLDAPadmin is a web-based LDAP client. It provides easy, anywhere-accessible,
  multi-language administration for your LDAP server. Its hierarchical tree-viewer
  and advanced search functionality make it intuitive to browse and administer your
  LDAP directory. Since it is a web application, this LDAP browser works on many
  platforms, making your LDAP server easily manageable from any location.
  phpLDAPadmin is the perfect LDAP browser for the LDAP professional and novice alike.
  Its user base consists mostly of LDAP administration professionals.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += CSWphpldapadmin.preinstall

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = https://sourceforge.net/projects/phpldapadmin/files/
UFILES_REGEX = (\d+(?:\.\d+)*).tgz

SPKG_SOURCEURL = http://phpldapadmin.sourceforge.net/

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF = $(sharedstatedir)/www/phpldapadmin/config/config.php.CSW

LICENSE = LICENSE
ARCHALL = 1

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(sharedstatedir)/www/phpldapadmin
	@ginstall -d $(DESTDIR)$(sharedstatedir)/www
	@cp -R $(WORKSRC) $(DESTDIR)$(sharedstatedir)/www/phpldapadmin
	@(cd $(DESTDIR)$(sharedstatedir)/www/phpldapadmin/config; \
		mv config.php.example config.php.CSW)
	@find $(DESTDIR)$(sharedstatedir) -name .cvsignore -exec rm \{\} \;
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/phpldapadmin
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@ln -s $(sharedstatedir)/www/phpldapadmin/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/phpldapadmin
	@$(MAKECOOKIE)

