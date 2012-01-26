NAME = rdoc-data
VERSION = 2.5.3
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = Core ri data for use with RDoc
define BLURB
  Core ri data for use with RDoc 2.5 Includes data for 1.8.6, 1.8.7, 1.9.1
endef

PACKAGES = CSWgem-rdocdata
CATALOGNAME = gem_rdocdata

LICENSE = README.txt

ARCHALL = 1

include gar/category.mk


post-install-modulated:
	cd $(DESTDIR); find . -type d -name "* *" | \
	while read F; do \
		N=`echo $$F | tr ' =' '_-'`; \
		mv "$$F" $$N; \
	done;
	cd $(DESTDIR); find . -type f -name "* *" | \
	while read F; do \
		N=`echo $$F | tr ' =' '_-'`; \
		mv "$$F" $$N; \
	done;
