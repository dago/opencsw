GARNAME = mantis
GARVERSION = 1.1.1
SF_PROJ = mantisbt
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
DISTFILES += $(call admfiles,CSWmantis,depend postinstall preremove)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/mantis
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@cp -rp $(WORKSRC) $(DESTDIR)$(prefix)/apache2/share/htdocs/mantis
	@find $(DESTDIR)$(prefix)/apache2/share/htdocs/mantis -name .cvsignore -exec rm \{\} \;

