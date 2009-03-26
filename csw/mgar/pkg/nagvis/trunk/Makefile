GARNAME = nagvis
GARVERSION = 1.3.2
CATEGORIES = apps

DESCRIPTION = visualization addon for nagios
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnagvis, prototype)

PATCHFILES += nagvis.ini.php.diff

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

REQUIRED_PKGS  = CSWnagios CSWphp5gd CSWphp5mysql CSWphp5mbstring CSWphp5session
REQUIRED_PKGS += CSWphp5xmlreader CSWphp5xmlwriter CSWgraphviz2
REQUIRED_PKGS += CSWcswclassutils

SPKG_CLASSES = none cswpreserveconf

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
	@#
	@# not nice but easy
	@#
	@cp $(WORKSRC)/etc/maps/__automap.cfg $(WORKSRC)/etc/maps/__automap.cfg.CSW
	@cp $(WORKSRC)/etc/maps/demo.cfg  $(WORKSRC)/etc/maps/demo.cfg.CSW
	@cp $(WORKSRC)/etc/maps/demo2.cfg  $(WORKSRC)/etc/maps/demo2.cfg.CSW
	@cp $(WORKSRC)/etc/nagvis.ini.php-sample $(WORKSRC)/etc/nagvis.ini.php.CSW
	@#
	@#
	@#
	@cp -r $(WORKSRC)/* $(DESTDIR)$(NAGVISDIR)
