GARNAME = Text-Reform
SPKG_VERSION = 1.12.2
GARVERSION = v$(SPKG_VERSION)
CATEGORIES = cpan
AUTHOR = DCONWAY

DESCRIPTION = manual text wrapping and reformatting
define BLURB
endef

DISTFILES += CSWpmtxtreform.gspec
DISTFILES += $(call admfiles,CSWpmtxtreform,prototype)

include gar/category.mk

post-install:
	@echo " ==> Copying demo files"
	@cp $(WORKDIR)/$(GARNAME)-$(GARVERSION)/demo/* $(DESTDIR)/$(sharedstatedir)/perl/csw/Text/
	@$(MAKECOOKIE)
