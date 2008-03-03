GARNAME = pari
GARVERSION = 2.1.7
CATEGORIES = lib

DESCRIPTION = efficient computations in number theory
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = http://pari.math.u-bordeaux.fr/pub/pari/unix/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWparigp,)

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS    = --prefix=$(prefix)
CONFIGURE_ARGS   += --miscdir=$(docdir)/pari
BUILD_ARGS        = gp

include gar/category.mk

configure-custom:
	@echo " ==> Running Configure"
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)
