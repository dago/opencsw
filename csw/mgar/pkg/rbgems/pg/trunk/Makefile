NAME = pg
VERSION = 0.9.0
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = Access a PostgreSQL database from Ruby
define BLURB
  This is the extension library to access a PostgreSQL database from Ruby. This library works with PostgreSQL 7.4 and later.
endef

PATCHFILES  = 0001-Remove-gcc-specific-Wall.patch
PATCHFILES += 0002-Add-DESTDIR-support.patch

PACKAGES = CSWgem-pg
CATALOGNAME = gem_pg

BUILD_DEP_PKGS = CSWpostgresql CSWgem-rakecompiler CSWgem-rdoc
RUNTIME_DEP_PKGS = CSWlibpq

LICENSE = LICENSE

# This must go into the runpath
NOISALIST = 1
EXTRA_LIB = /opt/csw/postgresql/lib

#CONFIGURE_SCRIPTS = ruby-setup
#BUILD_SCRIPTS = ruby-setup
INSTALL_SCRIPTS = ruby-setup

include gar/category.mk

configure-ruby-setup:
	cd $(WORKSRC) && ruby setup.rb config
	@$(MAKECOOKIE)

build-ruby-setup:
	cd $(WORKSRC) && ruby setup.rb setup
	@$(MAKECOOKIE)

PGCONFIG-sparc = pg_config32
PGCONFIG-i386 = pg_config

install-ruby-setup: GEM_BUILD_FLAGS=--with-pg-config=/opt/csw/postgresql/bin/$(PGCONFIG-$(GARCH))
install-ruby-setup:
	# cd $(WORKSRC) && ruby setup.rb install \
	#	--prefix=$(DESTDIR)
	cd $(WORKSRC) && rake gem
	#cd $(WORKSRC) && DESTDIR=$(DESTDIR) rake install -- --with-pg-config=/opt/csw/postgresql/bin/pg_config32
	LD_OPTIONS="$(LD_OPTIONS)" gem install \
		--ignore-dependencies \
		--local \
		--no-test \
		--install-dir $(DESTDIR)$(GEMDIR) \
		$(EXTRA_GEM_INSTALL_ARGS) \
		$(WORKSRC)/pkg/$(GEMFILE) \
		$(if $(GEM_BUILD_FLAGS),-- --build-flags $(GEM_BUILD_FLAGS))
	@$(MAKECOOKIE)

