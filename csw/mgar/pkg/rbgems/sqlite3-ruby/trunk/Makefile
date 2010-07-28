GARNAME = sqlite3-ruby
GARVERSION = 1.3.1
CATEGORIES = rbgems

DESCRIPTION = Ruby interface to SQLite3
define BLURB
  This module allows Ruby programs to interface with the SQLite3 database engine (http://www.sqlite.org). You must have the SQLite engine installed in order to build this module. Note that this module is NOT compatible with SQLite 2.x.
endef

PATCHFILES = 0001-Remove-gcc-specific-flags.patch

PACKAGES = CSWgem-sqlite3ruby
CATALOGNAME = gem_sqlite3ruby

BUILD_DEP_PKGS = CSWsqlite3devel
RUNTIME_DEP_PKGS = CSWsqlite3rt

LICENSE = LICENSE

CONFIGURE_SCRIPTS = ruby-setup
BUILD_SCRIPTS = ruby-setup
INSTALL_SCRIPTS = ruby-setup

include gar/category.mk

configure-ruby-setup:
	cd $(WORKSRC) && ruby setup.rb config
	@$(MAKECOOKIE)

build-ruby-setup:
	cd $(WORKSRC) && ruby setup.rb setup
	@$(MAKECOOKIE)

install-ruby-setup:
	cd $(WORKSRC) && ruby setup.rb install \
		--prefix=$(DESTDIR)
	@$(MAKECOOKIE)

