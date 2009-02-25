GARNAME = xcb-proto
GARVERSION = 1.4

CATEGORIES = x11

DESCRIPTION = xcb-proto
define BLURB
xcb-proto
endef

MASTER_SITES = $(XCB_MASTER_SITES)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWxcb-proto)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

pre-install:
	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME) 
	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(DISTNAME)/COPYING $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)/License.txt 

include gar/category.mk


