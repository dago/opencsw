GARNAME = Object-Accessor
GARVERSION = 0.34
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = An interface to create per object accessors
define BLURB
  Object::Accessor provides an interface to create per object accessors (as
  opposed to per Class accessors, as, for example, Class::Accessor provides).
endef

CATALOGNAME = pm_objaccessor
PACKAGES    = CSWpmobjaccessor

ARCHALL_CSWpmobjaccessor = 1

REQUIRED_PKGS_CSWpmobjaccessor += CSWpmprmscheck

LICENSE = README

include gar/category.mk

post-extract:
	@chmod o+r $(WORKSRC)/README
	@$(MAKECOOKIE)
