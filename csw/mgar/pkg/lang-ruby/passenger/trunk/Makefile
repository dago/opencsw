NAME = passenger
VERSION = 2.2.15
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = Passenger is an Apache module for Ruby on Rails support
define BLURB
  Passenger is an Apache module for Ruby on Rails support.
endef

PACKAGES = CSWgem-passenger
CATALOGNAME = gem_passenger

LICENSE = LICENSE

CHECKPKG_OVERRIDES_CSWgem-passenger += discouraged-path-in-pkgmap|/opt/csw/lib/ruby/gems/1.8/gems/passenger-2.2.15/test/stub/wsgi/passenger_wsgi.pyc
CHECKPKG_OVERRIDES_CSWgem-passenger += missing-dependency|CSWpython

include gar/category.mk

post-install-modulated:
	cd $(DESTDIR); find . -name "* *" | \
		while read F; do \
			N=`echo $$F | tr ' ' '_'`; \
			mv "$$F" $$N; \
		done;


