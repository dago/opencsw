GARNAME = prawn-core
GARVERSION = 0.8.4
CATEGORIES = rbgems

DESCRIPTION = A fast and nimble PDF generator for Ruby

define BLURB
  Prawn is a fast, tiny, and nimble PDF generator for Ruby 
endef

PACKAGES = CSWgem-prawncore
CATALOGNAME = gem_prawncore

LICENSE = LICENSE

ARCHALL = 1

include gar/category.mk

post-install-modulated:
	cd $(DESTDIR); find . -name "* *" | \
		while read F; do \
			N=`echo $$F | tr ' ' '_'`; \
			mv "$$F" $$N; \
		done;

