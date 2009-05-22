GARNAME = drupal
GARVERSION = 6.12
CATEGORIES = apps

DESCRIPTION = An open source content management platform
define BLURB
	GD is an open source code library for the dynamic creation of 
	images by programmers. GD creates PNG, JPEG and GIF images, 
	among other formats. GD is commonly used to generate charts, 
	graphics, thumbnails, and most anything else, on the fly. 
	While not restricted to use on the web, the most common 
	applications of GD involve web site development.
endef

MASTER_SITES = http://ftp.drupal.org/files/projects/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += httpd-drupal.conf.CSW
DISTFILES += README.CSW
PATCHFILES = uploaddir.diff

PACKAGES = CSWdrupal
CATALOGNAME_CSWdrupal = drupal
SPKG_SOURCEURL = http://drupal.org/
SPKG_DESC_CSWdrupal = $(DESCRIPTION)


# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL_CSWdrupal = 1

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS     = 
INSTALL_SCRIPTS   = custom
TEST_SCRIPTS = 

REQUIRED_PKGS_CSWdrupal  = CSWapache2c CSWphp5 CSWphp5gd CSWphp5mbstring
REQUIRED_PKGS_CSWdrupal += CSWphp5session CSWap2modphp5

DRUPAL_INST_DIR = $(DESTDIR)$(datadir)/$(GARNAME)/$(GARVERSION)
DRUPAL_DOCFILES  = CHANGELOG.txt COPYRIGHT.txt INSTALL.mysql.txt
DRUPAL_DOCFILES += INSTALL.pgsql.txt INSTALL.txt LICENSE.txt
DRUPAL_DOCFILES += MAINTAINERS.txt UPGRADE.txt

install-custom:
	ginstall -d $(DRUPAL_INST_DIR)/documentation
	ginstall -d $(DRUPAL_INST_DIR)/contrib
	cd $(WORKSRC); /usr/bin/pax -rw -v * $(DRUPAL_INST_DIR)
	gcp $(DOWNLOADDIR)/httpd-drupal.conf.CSW $(DRUPAL_INST_DIR)/contrib
	gcp $(DOWNLOADDIR)/README.CSW $(DRUPAL_INST_DIR)/documentation
	for file in $(DRUPAL_DOCFILES); do \
		gmv $(DRUPAL_INST_DIR)/$${file} $(DRUPAL_INST_DIR)/documentation/; done
	@$(MAKECOOKIE)


define CSWdrupal_postinstall
#!/bin/sh

PATH=/usr/bin:/usr/sbin

mkdir -p /var/opt/csw/drupal/upload
chmod o+w /var/opt/csw/drupal/upload

cat << _EOM_

*********************************************************************
*    NOTICE:
*	Before you can use druppal you need to configure it.
*	
*	For instructions on configuring Please Read
*   $$PKG_INST_ROOT/drupal/documentation/README.CSW
*
*********************************************************************

_EOM_
endef

include gar/category.mk
