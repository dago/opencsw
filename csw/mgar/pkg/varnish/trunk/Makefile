# $Id$
GARNAME = varnish
GARVERSION = 2.1.3
CATEGORIES = apps

DESCRIPTION = Varnish Web Cache
define BLURB
  Long description
endef

MASTER_SITES = http://www.varnish-software.com/sites/default/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.varnish-cache.org

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
