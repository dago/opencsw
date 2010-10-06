GARNAME = Params-Check
GARVERSION = 0.26
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = A generic input parsing/checking mechanism.
define BLURB
  Params::Check is a generic input parsing/checking mechanism.  It allows you
  to validate input via a template. The only requirement is that the arguments
  must be named.
endef

DISTFILES += COPYING

PACKAGES = CSWpmprmscheck 
CATALOGNAME = pm_prmscheck 
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmlclemktxtsimple

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
