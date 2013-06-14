# $Id$
#
NAME    = lure
VERSION = 1.1
GARTYPE = v2

DESCRIPTION = Lure of the Temptress, Freeware version
define BLURB
  Trouble is afoot in the once peaceful land of Turnvale. Skori warriors (vicious mercenaries under the control of the mysterious Temptress) have arrived. But who is the Temptress, and more importantly, where is she?
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT   = scummvm
DISTFILES    = $(DISTNAME).zip
DISTFILES   += $(NAME)-de-$(VERSION).zip
DISTFILES   += $(NAME)-es-$(VERSION).zip
DISTFILES   += $(NAME)-fr-$(VERSION).zip
DISTFILES   += $(NAME)-it-$(VERSION).zip

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

PACKAGES  = CSWlure
PACKAGES += CSWlure-de
PACKAGES += CSWlure-es
PACKAGES += CSWlure-fr
PACKAGES += CSWlure-it

LICENSE = $(NAME)/LICENSE.txt

WORKSRC = $(WORKDIR)/$(NAME)

SPKG_DESC_CSWlure   = Lure of the Temptress, Freeware version (English)
CATALOGNAME_CSWlure = lure
PKGFILES_CSWlure    = $(datadir)/scummvm/$(NAME)[^-].*

SPKG_DESC_CSWlure-de   = Lure of the Temptress, Freeware version (German)
CATALOGNAME_CSWlure-de = lure_de
PKGFILES_CSWlure-de    = $(datadir)/scummvm/$(NAME)-de.*

SPKG_DESC_CSWlure-es   = Lure of the Temptress, Freeware version (Spanish)
CATALOGNAME_CSWlure-es = lure_es
PKGFILES_CSWlure-es    = $(datadir)/scummvm/$(NAME)-es.*

SPKG_DESC_CSWlure-fr   = Lure of the Temptress, Freeware version (French)
CATALOGNAME_CSWlure-fr = lure_fr
PKGFILES_CSWlure-fr    = $(datadir)/scummvm/$(NAME)-fr.*

SPKG_DESC_CSWlure-it   = Lure of the Temptress, Freeware version (Italian)
CATALOGNAME_CSWlure-it = lure_it
PKGFILES_CSWlure-it    = $(datadir)/scummvm/$(NAME)-it.*

RUNTIME_DEP_PKGS   += CSWscummvm
CHECKPKG_OVERRIDES += surplus-dependency|CSWscummvm

# List of languages beside English
LANGUAGES = de es fr it

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@echo worksrc: $(WORKSRC)
	@ginstall -m 755 -d $(DESTDIR)$(datadir)/scummvm/$(NAME)
	@ginstall -m 644 -p $(WORKSRC)/* $(DESTDIR)$(datadir)/scummvm/$(NAME)
	@$(foreach lang, $(LANGUAGES), \
		ginstall -m 755 -d $(DESTDIR)$(datadir)/scummvm/$(NAME)-$(lang); ginstall -m 644 -p $(WORKSRC)-$(lang)/* $(DESTDIR)$(datadir)/scummvm/$(NAME)-$(lang); )
	@$(MAKECOOKIE)

