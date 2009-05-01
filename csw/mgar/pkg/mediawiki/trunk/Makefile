GARNAME = mediawiki
GARVERSION = 1.14.0
CATEGORIES = apps
RELVER = $(shell echo $(GARVERSION) |gsed 's/\(^[0-9].*\)\.[0-9]*/\1/')
DESCRIPTION = A free software wiki package written in PHP
define BLURB
	MediaWiki is a free software wiki package written in PHP, 
	originally for use on Wikipedia. It is now used by several 
	other projects of the non-profit Wikimedia Foundation and 
	by many other wikis, including this website, the home of MediaWiki. 
endef

MASTER_SITES = http://download.wikimedia.org/mediawiki/$(RELVER)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWmediawiki-math.postinstall
DISTFILES += CSWmediawiki.postinstall
DISTFILES += CSWmediawiki.preremove


PACKAGES = CSWmediawiki CSWmediawiki-math
CATALOGNAME_CSWmediawiki = mediawiki
SPKG_DESC_CSWmediawiki = $(DESCRIPTION)
CATALOGNAME_CSWmediawiki-math = mediawiki_math
SPKG_DESC_CSWmediawiki-math = LaTeX compatable Math plugin for MediaWiki

REQUIRED_PKGS_CSWmediawiki  = CSWphp5
REQUIRED_PKGS_CSWmediawiki-math  = CSWphp5 CSWmediawiki CSWtetex

PKGFILES_CSWmediawiki-math = .*/mediawiki/math.*

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU
ARCHALL_CSWmediawiki = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = math
INSTALL_SCRIPTS = custom
TEST_SCRIPTS = skip

build-math:
	cd $(WORKSRC)/math; $(BUILD_ENV) gmake
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(INSTALLISADIR)$(prefix)/mediawiki
	@(cd $(WORKSRC); /usr/bin/pax -rw -v ./ $(abspath $(INSTALLISADIR)$(prefix)/mediawiki))

test-skip:
	@$(MAKECOOKIE)

include gar/category.mk

