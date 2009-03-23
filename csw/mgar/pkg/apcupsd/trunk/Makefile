GARNAME = apcupsd
GARVERSION = 3.14.4
CATEGORIES = utils

DESCRIPTION = A daemon for controlling APC UPS
define BLURB
	"apcupsd" can be used for controlling all APC UPS models
	It can monitor and log the current power and battery status, perform
	automatic shutdown, and can run in network mode in order to power down
	other hosts on a LAN
endef

MASTER_SITES = http://www.apcupsd.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWapcupsd, prototype postinstall)
DISTFILES += cswapcupsd

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWcswclassutils

SPKG_CLASSES = none cswinitsmf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/opt/csw/etc/apcupsd
CONFIGURE_ARGS += --with-nologin=/var/run
CONFIGURE_ARGS += --with-pwrfail-dir=/opt/csw/etc/apcupsd/powerfail
CONFIGURE_ARGS += --with-log-dir=/opt/csw/var/apcupsd
CONFIGURE_ARGS += --with-cgi-bin=/opt/csw/etc/apcupsd/cgi

GARCOMPILER = GNU

TEST_SCRIPTS=

# moving configuration file & installing init script
post-install-modulated:
	(cd $(DESTDIR)$(prefix)/etc/apcupsd; \
	for i in apcupsd.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW";     \
		fi \
	done)
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 files/cswapcupsd $(DESTDIR)/etc/opt/csw/init.d/cswapcupsd

include gar/category.mk
