NAME = Params-Check
VERSION = 0.28
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BINGOS

DESCRIPTION = A generic input parsing/checking mechanism.
define BLURB
  Params::Check is a generic input parsing/checking mechanism.  It allows you
  to validate input via a template. The only requirement is that the arguments
  must be named.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-params-check 
CATALOGNAME = pm_params_check 
SPKG_DESC_CSWpm-params-check = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-params-check = CSWpmprmscheck
CATALOGNAME_CSWpmprmscheck = pm_prmscheck

ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmlclemktxtsimple

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
