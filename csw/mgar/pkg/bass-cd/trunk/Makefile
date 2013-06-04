# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME    = bass-cd
VERSION = 1.2
GARTYPE = v2

DESCRIPTION = Beneath a Steel Sky, Freeware CD Version
define BLURB
  Robert Foster is an innocent outsider stranded in a vast city where oppressed civilians live and work in soaring tower blocks... while the corrupt, covetous and rich lie underground, shielded from all pollution. Alone, save for a robot circuit board, Foster must fight for survival... and discover the sinister truth behind his abduction...
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT   = scummvm
DISTFILES    = $(DISTNAME).zip

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

BUILD_DEP_PKGS += CSWscummvm

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@echo worksrc: $(WORKSRC)
	@ginstall -m 755 -d $(DESTDIR)$(datadir)/scummvm/$(DISTNAME)
	@ginstall  -m 644 -p $(WORKSRC)/* $(DESTDIR)$(datadir)/scummvm/$(DISTNAME)
	@$(MAKECOOKIE)

