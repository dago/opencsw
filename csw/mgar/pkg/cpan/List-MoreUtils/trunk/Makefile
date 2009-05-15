GARNAME = List-MoreUtils
GARVERSION = 0.22
CATEGORIES = cpan
AUTHOR = VPARSEVAL

DESCRIPTION = Provide the stuff missing in List::Util
define BLURB
  List::MoreUtils provides some trivial but commonly needed functionality on
  lists which is not going to go into List::Util.
endef

PACKAGES = CSWpmlistmoreutils
CATALOGNAME = pm_listmoreutils

include gar/category.mk

pre-merge-modulated:
	@cd $(WORKSRC) && sed -n '/^Copyright/,$$p' README > COPYING
	@$(MAKECOOKIE)
