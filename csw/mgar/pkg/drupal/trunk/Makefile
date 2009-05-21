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

REQUIRED_PKGS_CSWdrupal  = CSWapache2c CSWphp5 CSWphp5gd CSWphp5mbstring
REQUIRED_PKGS_CSWdrupal += CSWphp5session CSWap2modphp5

## There are no tests for this
TEST_SCRIPTS = skip

test-skip:
	@$(MAKECOOKIE)

DRUPAL_BASE_INSTDIR = $(prefix)
DRUPAL_INST_DIR = $(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)
SETTINGS_DIR=$(DRUPAL_INST_DIR)/sites/default

install-custom:
	ginstall -d $(DESTDIR)$(DRUPAL_INST_DIR)
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -d $(DESTDIR)$(docdir)/drupal
	cd $(WORKSRC); /usr/bin/pax -rw -v * $(DESTDIR)$(DRUPAL_INST_DIR)
	gcp $(DESTDIR)$(SETTINGS_DIR)/default.settings.php $(DESTDIR)$(SETTINGS_DIR)/settings.php.CSW
	gcp $(DOWNLOADDIR)/httpd-drupal.conf.CSW $(DESTDIR)$(prefix)/apache2/etc/extra
	gcp $(DOWNLOADDIR)/README.CSW $(DESTDIR)$(docdir)/drupal/
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/LICENSE.txt $(DESTDIR)$(docdir)/drupal/license
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/COPYRIGHT.txt $(DESTDIR)$(docdir)/drupal/
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/CHANGELOG.txt $(DESTDIR)$(docdir)/drupal/
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/INSTALL.mysql.txt $(DESTDIR)$(docdir)/drupal/
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/INSTALL.pgsql.txt $(DESTDIR)$(docdir)/drupal/
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/INSTALL.txt $(DESTDIR)$(docdir)/drupal/
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/MAINTAINERS.txt $(DESTDIR)$(docdir)/drupal/
	gmv $(DESTDIR)$(DRUPAL_BASE_INSTDIR)/$(GARNAME)/$(GARVERSION)/UPGRADE.txt $(DESTDIR)$(docdir)/drupal/
	@$(MAKECOOKIE)


define CSWdrupal_postinstall
#!/bin/sh

PATH=/usr/bin:/usr/sbin

AP2CONF=/opt/csw/apache2/etc/httpd.conf
AP2EXTRADIR=/opt/csw/apache2/etc/extra
AP2USR="`sed -ne 's/^User \(.*\)/\1/p' $${AP2CONF}`"
AP2GRP="`sed -ne 's/^Group \(.*\)/\1/p' $${AP2CONF}`"

if [ -z $${AP2USR} ]; then
	AP2USR=nobody
fi
if [ -z $${AP2GRP} ]; then
	AP2GRP=nobody
fi

if [ -f $(SETTINGS_DIR)/settings.php ]; then
    echo "***** $(SETTINGS_DIR)/settings.php Found ***** "
	echo "***** Preserving Existing Config ***** "
else
	cp $(SETTINGS_DIR)/settings.php.CSW $(SETTINGS_DIR)/settings.php
	chmod o+w $(SETTINGS_DIR)/settings.php
	chmod o+w $(SETTINGS_DIR)
fi

perl -i -pne 's|_DRUPALDIR_|$(DRUPAL_INST_DIR)|' $${AP2EXTRADIR}/httpd-drupal.conf.CSW

if [ -f $${AP2EXTRADIR}/httpd-drupal.conf ]; then
	echo "***** $${AP2EXTRADIR}/httpd-drupal.conf Found *****"
	echo "***** Preserving Existing Config *****"
else
	cp $${AP2EXTRADIR}/httpd-drupal.conf.CSW $${AP2EXTRADIR}/httpd-drupal.conf
fi

if [ -n "`grep 'Include etc/extra/httpd-drupal.conf' $${AP2CONF}`" ]; then
	perl -i -pne 's|#(Include etc/extra/httpd-drupal.conf)|$$1|' $${AP2CONF}
else
	cat << END >>$${AP2CONF}
	
Include etc/extra/httpd-drupal.conf
END
fi
chown -R $${AP2USR}:$${AP2GRP} $(DRUPAL_BASE_INSTDIR)/$(GARNAME)
cat << _EOM_

*********************************************************************
*    NOTICE:
*          drupal has been enabled in $${AP2CONF}
*          You will need to restart your web server
*          To finish the install.
*********************************************************************

*********************************************************************
*	You need to install and or configure either
*   PostgreSQL: pkg-get -i postgresql
*   MySQL: pkg-get -i mysql5rt mysql5client mysql5
*	
*	For instructions on configuring Please Read
*   $$PKG_INST_ROOT/opt/csw/share/doc/drupal/README.CSW
*
*********************************************************************

_EOM_
endef

define CSWdrupal_preremove
#!/bin/sh

PATH=/usr/bin:/usr/sbin

AP2CONF=/opt/csw/apache2/etc/httpd.conf

perl -i -pne 's|(?<!#)(Include etc/extra/httpd-drupal.conf)|#$$1|' $${AP2CONF}

cat << _EOM_

*********************************************************************
*    NOTICE:
*          drupal has been disabled in $${AP2CONF}
*          You will need to restart your web server
*          To finish the removal.
*********************************************************************

_EOM_
endef

include gar/category.mk
