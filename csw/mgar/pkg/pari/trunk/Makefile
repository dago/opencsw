NAME = pari
VERSION = 2.3.5
CATEGORIES = lib

DESCRIPTION = efficient computations in number theory
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = http://pari.math.u-bordeaux.fr/pub/pari/unix/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWparigp,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS    = --prefix=$(prefix)
# CONFIGURE_ARGS   += --miscdir=$(docdir)/pari
BUILD_ARGS        = gp

TEST_SCRIPTS =

include gar/category.mk

configure-custom:
	@echo " ==> Running Configure"
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)
