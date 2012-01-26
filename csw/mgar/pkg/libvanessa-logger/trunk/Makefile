NAME = libvanessa-logger
VERSION = 0.0.8
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Generic logging library
define BLURB
  Provides a generic logging layer that may be used to log to one or more
  of syslog, an open file handle or a file name. Though due to to
  limitations in the implementation of syslog opening multiple syslog
  loggers doesn't makes sense. Includes the ability to limit which
  messages will be logged based on priorities. 
endef

VENDOR_URL   = http://www.vergenet.net/linux/vanessa/
MASTER_SITES = $(VENDOR_URL)/download/vanessa_logger/$(VERSION)/
DISTFILES    = vanessa_logger-$(VERSION).tar.gz
DISTNAME     = vanessa_logger-$(VERSION)
UFILES_REGEX = (\d+(?:\.\d+)*)
UPSTREAM_MASTER_SITES = $(VENDOR_URL)/download/vanessa_logger/

PACKAGES = CSWlibvanessa-logger
CATALOGNAME = libvanessa_logger

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk


post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)

install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
