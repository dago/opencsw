GARNAME = Text-Reform
#SPKG_VERSION = 1.12.2
#GARVERSION = v$(SPKG_VERSION)
GARVERSION = 1.20
CATEGORIES = cpan
AUTHOR = CHORNY

DESCRIPTION = Manual text wrapping and reformatting
define BLURB
	Manual text wrapping and reformatting
endef

#DISTFILES += CSWpmtxtreform.gspec
#DISTFILES += $(call admfiles,CSWpmtxtreform,prototype)
DISTFILES += COPYING

PACKAGES = CSWpmtxtreform
CATALOGNAME = pm_txtreform
ARCHALL = 1

include gar/category.mk

#post-install:
#	@echo " ==> Copying demo files"
#	@cp $(WORKDIR)/$(GARNAME)-$(GARVERSION)/demo/* $(DESTDIR)/$(sharedstatedir)/perl/csw/Text/
#	@$(MAKECOOKIE)
