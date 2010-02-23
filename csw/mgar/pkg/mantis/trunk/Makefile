GARNAME = mantisbt
GARVERSION = 1.2.0
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
DISTFILES += CSWmantis.preinstall
DISTFILES += CSWmantis.postmsg

PACKAGES = CSWmantis

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = doc/LICENSE
RUNTIME_DEP_PKGS = CSWapache2 CSWap2modphp5 CSWphp5mysql CSWphp5session
ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.mantisbt.org/

POSTMSG = $(docdir)/$(CATALOGNAME)/$(PACKAGES).postmsg

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs
	cd $(WORKSRC) && tar cf - . | ( cd $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs; tar xvf - )
	find $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs -name .cvsignore -exec rm \{\} \;
	ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	ln -s $(sharedstatedir)/www/mantis/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/mantis
	ginstall -d $(PKGROOT)$(docdir)/$(CATALOGNAME)/
	ginstall $(WORKDIR)/$(PACKAGES).postmsg $(PKGROOT)$(docdir)/$(CATALOGNAME)/$(PACKAGES).postmsg
	@$(MAKECOOKIE)

