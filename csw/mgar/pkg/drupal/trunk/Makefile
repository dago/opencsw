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

ALLOW_RELOCATE = 1
RELOCATE_PREFIX = /opt/csw/share

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

DRUPAL_INST_DIR = $(DESTDIR)$(docdir)/$(GARNAME)/$(GARVERSION)
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

DRUPAL_DIR=$${PKG_INST_ROOT}$${BASEDIR}/$(GARNAME)/$(GARVERSION)
SETTINGS_DIR=$${DRUPAL_DIR}/sites/default
CONTRIB_DIR=$${DRUPAL_DIR}/contrib
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

if [ -f $${SETTINGS_DIR}/settings.php ]; then
	echo "***** $${SETTINGS_DIR}/settings.php Found ***** "
	echo "***** Preserving Existing Config ***** "
else
	cp $${SETTINGS_DIR}/default.settings.php $${SETTINGS_DIR}/settings.php
	chmod o+w $${SETTINGS_DIR}/settings.php
	chmod o+w $${SETTINGS_DIR}
fi
perl -i -pne "s|_DRUPALDIR_|$${DRUPAL_DIR}|" $${CONTRIB_DIR}/httpd-drupal.conf.CSW
cp $${CONTRIB_DIR}/httpd-drupal.conf.CSW $${AP2EXTRADIR}/httpd-drupal.conf.CSW

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
mkdir -p /var/opt/csw/drupal/upload
chmod o+w /var/opt/csw/drupal/upload
chown -R $${AP2USR}:$${AP2GRP} /var/opt/csw/drupal/upload
chown -R $${AP2USR}:$${AP2GRP} $${DRUPAL_DIR}

cat << _EOM_
*********************************************************************
*    NOTICE:
*          drupal has been enabled in $${AP2CONF}
*          You will need to restart your web server
*          To finish the install.
*********************************************************************

*********************************************************************
*   NOTICE:
*         Before you can use druppal you need to configure it.
*
*         For instructions on configuring Please Read
*         $${PKG_INST_ROOT}$${BASEDIR}/$(GARNAME)/$(GARVERSION)/documentation/README.CSW
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
