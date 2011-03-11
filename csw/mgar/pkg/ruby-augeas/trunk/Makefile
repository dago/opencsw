NAME = ruby-augeas
VERSION = 0.3.0
CATEGORIES = ruby

DESCRIPTION = Augeas Ruby Bindings
define BLURB
endef

MASTER_SITES = http://augeas.net/download/ruby/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://augeas.net

PACKAGES = CSWrubyaugeas
CATALOGNAME = ruby_augeas
DEP_PKGS = CSWaugeas
DEP_PKGS += CSWruby

BUILD_DEP_PKGS = CSWrake
TEST_SCRIPTS = 
# TEST_TARGET = check

include gar/category.mk

install-ruby-augeas:

