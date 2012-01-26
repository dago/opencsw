NAME = Parse-RecDescent
VERSION = 1.963
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DCONWAY

DESCRIPTION = Generate recursive-descent parsers
define BLURB
  Parse::RecDescent incrementally generates top-down recursive-descent text
  parsers from simple yacc-like grammar specifications.
endef

PACKAGES = CSWpmparserecdescent
CATALOGNAME = pm_parserecdescent

ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmversion

LICENSE = README

include gar/category.mk

post-extract:
	@chmod o+r $(WORKSRC)/README
	@$(MAKECOOKIE)
