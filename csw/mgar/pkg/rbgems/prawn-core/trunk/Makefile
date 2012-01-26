NAME = prawn-core
VERSION = 0.8.4
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = A fast and nimble PDF generator for Ruby

define BLURB
  Prawn is a fast, tiny, and nimble PDF generator for Ruby 
endef

GEMPKGNAME = prawncore

LICENSE = LICENSE

ARCHALL = 1

include gar/category.mk

post-install-modulated:
	cd $(DESTDIR); find . -name "* *" | \
		while read F; do \
			N=`echo $$F | tr ' ' '_'`; \
			mv "$$F" $$N; \
		done;

