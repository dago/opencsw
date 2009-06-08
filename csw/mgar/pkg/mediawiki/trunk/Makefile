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
DISTFILES += CSWmediawiki.postinstall CSWmediawiki.preremove 
DISTFILES += httpd-mediawiki.conf.CSW README.CSW

ALLOW_RELOCATE = 1
RELOCATE_PREFIX = /opt/csw/share/www

CATALOGNAME_CSWmediawiki = mediawiki
SPKG_DESC_CSWmediawiki = $(DESCRIPTION)

REQUIRED_PKGS_CSWmediawiki  = CSWphp5 CSWapache2c

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL_CSWmediawiki = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
INSTALL_SCRIPTS = custom
TEST_SCRIPTS = skip

PATH = /opt/csw/php5/bin:$(PATH)
install-custom:
	@ginstall -d $(DESTDIR)$(RELOCATE_PREFIX)/mediawiki
	@cd $(WORKSRC); \
		/usr/bin/pax -rw -v ./ $(abspath $(DESTDIR)$(RELOCATE_PREFIX)/mediawiki)
	@ginstall -D $(DOWNLOADDIR)/README.CSW \
		$(DESTDIR)$(RELOCATE_PREFIX)/mediawiki/documentation/README.CSW
	@ginstall -D $(DOWNLOADDIR)/httpd-mediawiki.conf.CSW \
		$(DESTDIR)$(RELOCATE_PREFIX)/mediawiki/contrib/httpd-mediawiki.conf.CSW
	@$(MAKECOOKIE)

test-skip:
	@$(MAKECOOKIE)

include gar/category.mk

