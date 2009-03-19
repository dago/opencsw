GARNAME = kbproto
GARVERSION = 1.0.3

CATEGORIES = x11

DESCRIPTION = KB extension headers from X.org
define BLURB
This provides the KB extension headers from modular X.org X11 project.
endef

MASTER_SITES  = $(X11_PROTO_MASTER_SITE)
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES    += $(call admfiles,CSWkbproto)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

pre-install:
	@ginstall -d $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME) 
	@gcp -fp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(DISTNAME)/COPYING $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))$(datadir)/doc/$(GARNAME)/License.txt 

include gar/category.mk

