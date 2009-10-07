GARNAME = npadmin
GARVERSION = 0.14
CATEGORIES = apps

DESCRIPTION =  Command line SNMP based network adminstration tool for printers
define BLURB
endef

SF_PROJ = lpr
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://lpr.sourceforge.net/

ARCHALL = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && rm -f config.cache config.status
