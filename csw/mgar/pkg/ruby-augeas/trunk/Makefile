NAME       = ruby-augeas
VERSION    = 0.5.0
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Augeas Ruby Bindings
define BLURB
endef

MASTdownload.augeas.netugeas.net/download/ruby/
DISTFILES    = $(NAME)-$(VERSION).tgz
VENDOR_URL   = http://augeas.net

PACKAGES    = CSWrubyaugeas
CATALOGNAME = ruby_augeas

RUNTIME_DEP_PKGS_CSWrub20 += CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWrubyaugeas += CSWaugeas
CHECKPKG_OVERRIDES_CSWrubyaugeas += catalogname-does-not-match-pkgname|pkgname=CSWrubyaugeas|catalogname=ruby_augeas|expected-catalogname=rubyaugeas
# covered by CSWaugeas - and agreed not to split
CHECKPKG_OVERRIDES_CSWrubyaugeas += soname-not-found|libaugeas.so.0|is|needed|by|opt/csw/lib/ruby/site_ruby/1.8/sparc-solarPATCHFILES = 0001-use-gnu-make-for-building-_augeas.so.patch
PATCHFILES += 0002-modify-LDFLAGS-to-add-opt-csw-lib-to-the-runtime-lin.patch

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWrubyaugeas)
BUILD_DEP_PKGS += CSWruby20-dev
GS    += CSWruby18
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
	cd 2.0$(WORKSRC) && rake build
	ginstall -m 755 $(WORKSRC)/lib/augeas.rb $(DESTDIR)$(sitelibdir)
	ginstall -m 755 $(WORKSRC)/ext/augeas/_augeas.so $(DESTDIR)$(sitearchdir