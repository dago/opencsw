NAME = Object-Accessor
VERSION = 0.42
CATEGORIES = cpan
AUTHOR = BINGOS

DESCRIPTION = An interface to create per object accessors
define BLURB
  Object::Accessor provides an interface to create per object accessors (as
  opposed to per Class accessors, as, for example, Class::Accessor provides).
endef

CATALOGNAME = pm_objaccessor
PACKAGES    = CSWpmobjaccessor

ARCHALL_CSWpmobjaccessor = 1

RUNTIME_DEP_PKGS_CSWpmobjaccessor += CSWpmprmscheck

LICENSE = README

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3\/.* .*\/man\/man1\/.*

include gar/category.mk

post-extract:
	@chmod o+r $(WORKSRC)/README
	@$(MAKECOOKIE)
