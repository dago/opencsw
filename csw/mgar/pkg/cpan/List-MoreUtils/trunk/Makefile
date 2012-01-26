NAME = List-MoreUtils
VERSION = 0.22
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = VPARSEVAL

DESCRIPTION = Provide the stuff missing in List::Util
define BLURB
  List::MoreUtils provides some trivial but commonly needed functionality on
  lists which is not going to go into List::Util.
endef

PACKAGES = CSWpmlistmoreutils
CATALOGNAME = pm_listmoreutils

# This is the old package with the broken name
INCOMPATIBLE_PKGS = CSWpmlistmoreut

include gar/category.mk

pre-merge-modulated:
	@cd $(WORKSRC) && sed -n '/^Copyright/,$$p' README > COPYING
	@$(MAKECOOKIE)
