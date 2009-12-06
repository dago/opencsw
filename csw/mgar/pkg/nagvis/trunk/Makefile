GARNAME = nagvis
GARVERSION = 1.4.5
CATEGORIES = apps

SPKG_DESC_CSWnagvis = visualization addon for nagios

define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

DISTFILES += CSWnagvis.prototype

PATCHFILES += nagvis.ini.php-sample.diff

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWnagvis
CATALOGNAME_CSWnagvis = nagvis

REQUIRED_PKGS_CSWnagvis  = CSWnagios CSWphp5gd CSWphp5mysql CSWphp5mbstring CSWphp5session
REQUIRED_PKGS_CSWnagvis += CSWphp5xmlreader CSWphp5xmlwriter CSWgraphviz2 CSWphp5gettext
REQUIRED_PKGS_CSWnagvis += CSWap2modphp5 CSWcswclassutils

SPKG_CLASSES_CSWnagvis = none cswpreserveconf

ARCHALL_CSWnagvis = 1

#CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
SKIPTEST = 1

ENABLE_CHECK = 0

NAGVISDIR = /opt/csw/nagios/share/nagvis

include gar/category.mk

configure-custom:
	@$(MAKECOOKIE)

build-custom:
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(NAGVISDIR)
	#$(WORKSRC)/install.sh -n $(DESTDIR)/opt/csw/nagios \
	#-B $(DESTDIR)/opt/csw/nagios/bin/nagios \
	#-m $(DESTDIR)/opt/csw/nagios/ndoutils/bin/ndo2db-3x \
	#-b $(DESTDIR)/opt/csw/bin \
	#-p $(DESTDIR)/opt/csw/nagios/share/nagvis \
	#-W /nagios/nagvis \
	#-u nobody \
	#-g nobody \
	#-w /opt/csw/apache2/etc \
	#-i ndo2db
	@
	@#
	@# not nice but easy
	@#
	@cp $(WORKSRC)/etc/maps/__automap.cfg $(WORKSRC)/etc/maps/__automap.cfg.CSW
	@cp $(WORKSRC)/etc/maps/demo.cfg  $(WORKSRC)/etc/maps/demo.cfg.CSW
	@cp $(WORKSRC)/etc/maps/demo2.cfg  $(WORKSRC)/etc/maps/demo2.cfg.CSW
	@cp $(WORKSRC)/etc/maps/demo-map.cfg  $(WORKSRC)/etc/maps/demo-map.cfg.CSW
	@cp $(WORKSRC)/etc/maps/demo-server.cfg  $(WORKSRC)/etc/maps/demo-server.cfg.CSW
	@cp $(WORKSRC)/etc/nagvis.ini.php-sample $(WORKSRC)/etc/nagvis.ini.php.CSW
	@#
	@#
	@#
	@cp -r $(WORKSRC)/* $(DESTDIR)$(NAGVISDIR)
