NAME       = ruby-augeas
VERSION    = 0.3.0
CATEGORIES = lang

DESCRIPTION = Augeas Ruby Bindings
define BLURB
endef

MASTER_SITES = http://augeas.net/download/ruby/
DISTFILES    = $(NAME)-$(VERSION).tgz
VENDOR_URL   = http://augeas.net

PACKAGES    = CSWrubyaugeas
CATALOGNAME = ruby_augeas

RUNTIME_DEP_PKGS_CSWrubyaugeas += CSWruby18
RUNTIME_DEP_PKGS_CSWrubyaugeas += CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWrubyaugeas += CSWaugeas
CHECKPKG_OVERRIDES_CSWrubyaugeas += catalogname-does-not-match-pkgname|pkgname=CSWrubyaugeas|catalogname=ruby_augeas|expected-catalogname=rubyaugeas
CHECKPKG_OVERRIDES_CSWrubyaugeas += missing-dependency|CSWruby

BUILD_DEP_PKGS    = CSWrake
BUILD_DEP_PKGS    += CSWruby18
BUILD_SCRIPTS     =
CONFIGURE_SCRIPTS =
TEST_SCRIPTS      = 
INSTALL_SCRIPTS   = ruby-augeas

sitelibdir = $(shell ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
sitearchdir = $(shell ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")

include gar/category.mk

install-ruby-augeas:
	ginstall -m 755 -d $(DESTDIR)
	ginstall -m 755 -d $(DESTDIR)$(sitearchdir)
	ginstall -m 755 -d $(DESTDIR)$(sitelibdir)
	cd $(WORKSRC) && rake build
	ginstall -m 755 $(WORKSRC)/lib/augeas.rb $(DESTDIR)$(sitelibdir)
	ginstall -m 755 $(WORKSRC)/ext/augeas/_augeas.so $(DESTDIR)$(sitearchdir)
	@$(MAKECOOKIE)
