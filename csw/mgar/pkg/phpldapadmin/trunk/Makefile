GARNAME = phpldapadmin
GARVERSION = 1.1.0.6
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWphpldapadmin,depend postinstall preremove)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=61828
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/phpldapadmin
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@cp -R $(WORKSRC) $(DESTDIR)$(prefix)/apache2/share/htdocs/phpldapadmin
	@cp $(DESTDIR)$(prefix)/apache2/share/htdocs/phpldapadmin/config/config.php.example \
		$(DESTDIR)/$(prefix)/apache2/share/htdocs/phpldapadmin/config/config.php.CSW
	@find $(DESTDIR)$(prefix) -name .cvsignore -exec rm \{\} \;
	@$(MAKECOOKIE)

