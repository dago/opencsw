NAME = mantisbt
VERSION = 1.2.3
CATEGORIES = apps
GARTYPE = v2

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
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWmantis.preinstall
DISTFILES += CSWmantis.postmsg

PACKAGES = CSWmantis

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = doc/LICENSE
RUNTIME_DEP_PKGS = CSWapache2 CSWap2modphp5 CSWphp5mysql CSWphp5session
ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.mantisbt.org/

POSTMSG = $(docdir)/$(CATALOGNAME)/$(PACKAGES).postmsg

CHECKPKG_OVERRIDES_CSWmantis += surplus-dependency|CSWphp5mysql
CHECKPKG_OVERRIDES_CSWmantis += surplus-dependency|CSWap2modphp5
CHECKPKG_OVERRIDES_CSWmantis += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWmantis += surplus-dependency|CSWphp5session

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME)"
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs
	(echo ".git"; echo ".cvsignore") >$(WORKDIR)/tarexclude
	cd $(WORKSRC) && tar cfX - $(abspath $(WORKDIR)/tarexclude) . | ( cd $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs; tar xvf - )
	#find $(DESTDIR)$(sharedstatedir)/www/mantis/htdocs -name .cvsignore -exec rm \{\} \;
	ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	ln -s $(sharedstatedir)/www/mantis/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/mantis
	ginstall -d $(PKGROOT)$(docdir)/$(CATALOGNAME)/
	ginstall $(WORKDIR)/$(PACKAGES).postmsg $(PKGROOT)$(docdir)/$(CATALOGNAME)/$(PACKAGES).postmsg
	@$(MAKECOOKIE)

