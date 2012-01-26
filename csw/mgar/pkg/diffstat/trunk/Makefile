NAME = diffstat
VERSION = 1.55
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A utility which provides statistics based on the output of diff
define BLURB
endef

MASTER_SITES = ftp://invisible-island.net/diffstat/
DISTFILES += $(DISTNAME).tgz

VENDOR_URL = http://invisible-island.net/diffstat/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-install-prefix=$(DESTDIR)

include gar/category.mk

post-extract-modulated:
	-test -f $(WORKSRC)/diffstat.1 && perl -n -e 'next if( !/^\.\\"/ ); s/\.\\"//; print "*$$_"' $(WORKSRC)/diffstat.1 >$(WORKSRC)/COPYING
	@$(MAKECOOKIE)
