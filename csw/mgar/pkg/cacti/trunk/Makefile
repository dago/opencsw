GARNAME = cacti
GARVERSION = 0.8.7e
CATEGORIES = apps

DESCRIPTION = a network graphing solution based on RRDtool
define BLURB
  Cacti is a complete network graphing solution designed to harness the power of RRDTool's data storage and graphing functionality. Cacti provides a fast poller, advanced graph templating, multiple data acquisition methods, and user management features out of the box. All of this is wrapped in an intuitive, easy to use interface that makes sense for LAN-sized installations up to complex networks with hundreds of devices.
endef

MASTER_SITES = http://www.cacti.net/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES += CSWcacti.prototype CSWcacti.preinstall
DISTFILES += CSWcacti.prototype CSWcacti.postinstall

PATCHFILES += global_settings.php.diff
PATCHFILES += install_index.php.diff	# added search paths for initial setup
PATCHFILES += global.php.diff		# path to rrd files is hard coded :(
PATCHFILES += cacti.sql.diff
PATCHFILES += config.php.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

REQUIRED_PKGS = CSWrrd CSWnetsnmp CSWmysql5client CSWcswclassutils
REQUIRED_PKGS = CSWphp5 CSWap2modphp5 CSWphp5mysql CSWphp5snmp CSWphp5session CSWphp5sockets

SPKG_CLASSES = none cswusergroup

CATALOGNAME = cacti
ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
SKIPTEST = 1

ENABLE_CHECK = 0

CACTIDIR=/opt/csw/cacti
DOCDIR=/opt/csw/share/doc/cacti
VARDIR=/var/opt/csw/cacti

include gar/category.mk

configure-custom:
	@$(MAKECOOKIE)

build-custom:
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(CACTIDIR)
	@ginstall -d $(DESTDIR)$(DOCDIR)
	@ginstall -d $(DESTDIR)$(VARDIR)
	@ginstall -d $(DESTDIR)$(VARDIR)/log
	@ginstall -d $(DESTDIR)$(VARDIR)/rra
	@cp $(WORKSRC)/LICENSE $(DESTDIR)$(DOCDIR)
	@cp $(WORKSRC)/README $(DESTDIR)$(DOCDIR)
	@cp -r $(WORKSRC)/docs $(DESTDIR)$(DOCDIR)
	@#
	@# very nasty
	@#
	@cp -r $(WORKSRC)/* $(DESTDIR)$(CACTIDIR)
	@rm -r $(DESTDIR)$(CACTIDIR)/LICENSE $(DESTDIR)$(CACTIDIR)/README $(DESTDIR)$(CACTIDIR)/docs
	@rm -r $(DESTDIR)$(CACTIDIR)/log $(DESTDIR)$(CACTIDIR)/rra
	@#
	@ginstall -d $(DESTDIR)/opt/csw/etc/pkg/CSWcacti
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWcacti/cswusergroup
