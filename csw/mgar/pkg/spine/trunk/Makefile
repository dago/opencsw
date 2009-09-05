#GARNAME = cacti-spine
GARNAME = spine
GARVERSION = 0.8.7e
CATEGORIES = apps

DESCRIPTION = very fast poller for cacti
define BLURB
  Spine, formally Cactid, is a poller for Cacti that primarily strives to be as fast as possible. For this reason it is written in native C, makes use of POSIX threads, and is linked directly against the net-snmp library for minmumal SNMP polling overhead. Spine is a replacement for the default cmd.php poller so you must decide if using Spine makes sense for your installation.
endef

MASTER_SITES = http://www.cacti.net/downloads/spine/
#DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES  = cacti-$(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += cswusergroup CSWspine.postinstall
DISTNAME = cacti-$(GARNAME)-$(GARVERSION)

PATCHFILES += configure.diff

NOISALIST = 1

CATALOGNAME = spine

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

REQUIRED_PKGS = CSWmysql5rt CSWnetsnmp CSWosslrt CSWzlib CSWcswclassutils

SPKG_CLASSES = none cswpreserveconf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql=/opt/csw/mysql5
CONFIGURE_ARGS += --with-snmp=/opt/csw/include/net-snmp

INSTALL_SCRIPTS = custom

SKIPTEST = 1

DOCDEST = $(DESTDIR)$(BUILD_PREFIX)/share/doc/spine
BINDIR = $(DESTDIR)$(BUILD_PREFIX)/bin
CFGDIR = $(DESTDIR)$(BUILD_PREFIX)/etc

include gar/category.mk

pre-configure-modulated:
	@echo " ==> Pre-configure in $(WORKSRC)"
	@rm $(WORKSRC)/config/ltmain.sh
	@rm $(WORKSRC)/config/config.sub
	@rm $(WORKSRC)/config/config.guess
	@ln -s /opt/csw/share/libtool/config/ltmain.sh  $(WORKSRC)/config/ltmain.sh
	@ln -s /opt/csw/share/libtool/config/config.sub  $(WORKSRC)/config/config.sub
	@ln -s /opt/csw/share/libtool/config/config.guess  $(WORKSRC)/config/config.guess
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/LICENSE $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/README $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/README-WINDOWS $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/INSTALL $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/LICENSE.LGPL $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/COPYING $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/ChangeLog $(DOCDEST)
	@ginstall -d $(BINDIR)
	@ginstall -m 755 $(WORKSRC)/spine $(BINDIR)
	@ginstall -d $(CFGDIR)
	@ginstall -m 644 $(WORKSRC)/spine.conf $(CFGDIR)/spine.conf.CSW
	@$(MAKECOOKIE)
