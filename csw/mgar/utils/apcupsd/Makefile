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
DISTFILES += $(call admfiles,CSWapcupsd,)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/opt/csw/etc/apcupsd
CONFIGURE_ARGS += --with-nologin=/var/run

GARCOMPILER = GCC

TEST_SCRIPTS=

include ../category.mk
