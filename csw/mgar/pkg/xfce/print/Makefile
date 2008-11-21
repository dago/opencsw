GARNAME = xfprint
CATEGORIES = xfce

DESCRIPTION = Xfce Printing Helper
define BLURB
   Xfce Printing Helper 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfceprint.depend CSWxfceprint.gspec CSWxfceprint.prototype
# DISTFILES += CSWxfceprintdoc.depend CSWxfceprintdoc.gspec CSWxfceprintdoc.prototype
# DISTFILES += CSWlibxfceprint.depend CSWlibxfceprint.gspec CSWlibxfceprint.prototype
# DISTFILES += CSWlibxfceprintdev.depend CSWlibxfceprintdev.gspec CSWlibxfceprintdev.prototype

DISTFILES += $(call admfiles,CSWxfceprint, depend)

TEST_SCRIPTS = none

include ../category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS += --enable-bsdlpr --enable-cups

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

