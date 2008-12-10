GARNAME = mantisbt
GARVERSION = 1.1.6
CATEGORIES = apps

DESCRIPTION = Mantis is a free popular web-based bugtracking system
define BLURB
  Mantis is a free popular web-based bugtracking system.
  It is written in the PHP scripting language and works with MySQL,
  MS SQL, and PostgreSQL databases and a webserver. Mantis has been
  installed on Windows, Linux, Mac OS, OS/2, and others. Almost any
  web browser should be able to function as a client. It is released
  under the terms of the GNU General Public License (GPL).
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmantis,depend preinstall postinstall)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.mantisbt.org/

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(sharedstatedir)/www/mantis
	@ginstall -d $(DESTDIR)$(sharedstatedir)/www/mantis
	@cp -rp $(WORKSRC) $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs
	@find $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs -name .cvsignore -exec rm \{\} \;
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/mantis
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@ln -s $(sharedstatedir)/www/mantis/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/mantis

