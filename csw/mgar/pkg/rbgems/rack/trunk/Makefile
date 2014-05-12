NAME = rack
VERSION = 1.5.2
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = A minimal interface for developing web applications in Ruby
define BLURB
  Rack provides minimal, modular and adaptable interface for developing web applications in Ruby.
  By wrapping HTTP requests and responses in the simplest way possible, it unifies and distills
  the API for web servers, web frameworks, and software in between (the so-called middleware)
  into a single method call. Also see http://rack.rubyforge.org.
endef

PACKAGES = CSWgem-rack
CATALOGNAME = gem_rack

LICENSE = COPYING

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWgem-rack += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/rack-1.5.2/README.rdoc
CHECKPKG_OVERRIDES_CSWgem-rack += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/doc/rack-1.5.2/rdoc/files/README_rdoc.html

include gar/category.mk
