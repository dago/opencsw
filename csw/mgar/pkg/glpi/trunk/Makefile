# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = glpi
VERSION = 0.83.6
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Inventory-Resource system for computer equipment
define BLURB
GLPI is the Information Resource-Manager with an additional Administration- Inte
rface. You can use it to build up a database with an inventory for your company 
(computer, software, printers...). It has enhanced functions to make the daily l
ife for the administrators easier, like a job-tracking-system with mail-notifica
tion and methods to build a database with basic information about your network-t
opology.
endef

VENDOR_URL = http://www.glpi-project.org/

MASTER_SITES = https://forge.indepnet.net/atta314ents/download/1253/
DISTFILES  = $(DISTNAME)-$(VERSION).tar.gz
DISTFILES += README.CSW
DISTNAME=glpi
LICENSE=COPYING.txt

NOGITPATCH = 1

POSTMSG = /opt/csw/share/doc/glpi/README.CSW

RUNTIME_DEP_PKGS_CSWglpi += CSWap2-modphp5
RUNTIME_DEP_PKGS_CSWglpi += CSWapache2
RUNTIME_DEP_PKGS_CSWglpi += CSWphp5-mysql
RUNTIME_DEP_PKGS_CSWglpi += CSWphp5-json

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

REINPLACE_USRSHARE += /config/based_config.php

# checkpkg cannot track this
CHECKPKG_OVERRIDES_CSWglpi += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWglpi += surplus-dependency|CSWap2-modphp5
CHECKPKG_OVERRIDES_CSWglpi += surplus-dependency|CSWphp5-mysql
CHECKPKG_OVERRIDES_CSWglpi += surplus-dependency|CSWphp5-jPACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386json


ARCHALL = 1

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)$(prefix)/share/www/glpi
	@ginstall -d $(DESTDIR)$(prefix)/share/www/glpi
	@cp -R $(WORKSRC) $(DESTDIR)$(prefix)/share/www
	@ginstall -d $(DESTDIR)$(docdir)/glpi
	@cp $(WORKSRC)/COPYING.txt $(DESTDIR)$(docdir)/glpi/licens