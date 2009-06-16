GARNAME = Parse-RecDescent
GARVERSION = 1.96.0
CATEGORIES = cpan
AUTHOR = DCONWAY

DESCRIPTION = generate recursive-descent parsers
define BLURB
  Parse::RecDescent incrementally generates top-down recursive-descent text
  parsers from simple yacc-like grammar specifications.
endef

CATALOGNAME = pm_parserecdescent
PACKAGES    = CSWpmparserecdescent

ARCHALL_CSWpmparserecdescent = 1

REQUIRED_PKGS_CSWpmparserecdescent = CSWpmversion

LICENSE = README

include gar/category.mk

post-extract:
	@chmod o+r $(WORKSRC)/README
	@$(MAKECOOKIE)
