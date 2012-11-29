# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = davical
VERSION = 1.1.1
GARTYPE = v2

DESCRIPTION = CalDAV Server
define BLURB
The DAViCal CalDAV Server is designed to trivially store
CalDAV calendars, such as those from Evolution, Sunbird/Lightning,
Mulberry, iCal, iPhone or SOHO Organizer, in a central location,
providing shared calendars, free/busy publication and a basic
administration interface.
endef

MASTER_SITES =  http://debian.mcmillan.net.nz/packages/davical/
DISTFILES  = $(DISTNAME).tar.gz

ARCHALL = 1
NOGITPATCH=1

REINPLACE_USRSHARE += docs/api/* docs/api/*/* docs/api/*/*/*
REINPLACE_USRSHARE += inc/*
REINPLACE_USRSHARE += dba/*
REINPLACE_USRSHARE += htdocs/* htdocs/.*
REINPLACE_USRSHARE += config/apache-davical.conf 
REINPLACE_USRSHARE += docs/website/installation.php

REINPLACE_USRLOCAL += dba/create-database.sh
REINPLACE_USRLOCAL += htdocs/always.php
REINPLACE_USRLOCAL += docs/api/davical/_htdocs---always.php.html

EXTRA_MERGE_EXCLUDE_FILES += .*\.in

RUNTIME_DEP_PKGS += CSWpostgresql84
RUNTIME_DEP_PKGS += CSWap2-modphp5
RUNTIME_DEP_PKGS += CSWpm-dbi
RUNTIME_DEP_PKGS += CSWpm-yaml
RUNTIME_DEP_PKGS += CSWpm-dbd-pg
RUNTIME_DEP_PKGS += CSWphp5-pdopgsql
RUNTIME_DEP_PKGS += CSWphp5-iconv
RUNTIME_DEP_PKGS += CSWphp5-curl
RUNTIME_DEP_PKGS += CSWphp5-calendar
RUNTIME_DEP_PKGS += CSWphp5-awl
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWphp5-calendar
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWpm-dbi
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWphp5-pdopgsql
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWap2-modphp5
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWphp5-curl
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWphp5-iconv
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWpostgresql84
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWpm-dbd-pg
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWpm-yaml
CHECKPKG_OVERRIDES_CSWdavical += surplus-dependency|CSWphp5-awl


CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/$(NAME)
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/inc $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/htdocs $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/config $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/dba $(DESTDIR)$(prefix)/share/www/$(NAME)
	@cp -rp $(WORKSRC)/docs/* $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)

