GARNAME = avantfax
GARVERSION = 3.1.2
SF_PROJ = avantfax
CATEGORIES = apps

DESCRIPTION = AvantFAX is a web application for managing faxes on HylaFAX fax servers
define BLURB
  AvantFAX allows users on any platform to view and send faxes without
  having to install special software. It also allows administrators to
  manage users, their permissions, fax lines, fax categories, etc.
  AvantFAX can be accessed from the local network and remotely via
  Internet using standard networking equipment.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWavantfax,depend preinstall postinstall)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=160107
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.avantfax.com

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(sharedstatedir)/www/avantfax
	@ginstall -d $(DESTDIR)$(sharedstatedir)/www/avantfax
	@cp -rp $(WORKSRC) $(DESTDIR)$(sharedstatedir)/www/avantfax/htdocs
	@find $(DESTDIR)$(sharedstatedir)/www/avantfax/htdocs -name .cvsignore -exec rm \{\} \;
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/avantfax
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@ln -s $(sharedstatedir)/www/avantfax/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/avantfax

