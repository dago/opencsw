NAME = SVN-Mirror
VERSION = 0.75
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CLKAO

DESCRIPTION = Mirror remote repository to local Subversion repository
define BLURB
  SVN::Mirror allows you to mirror remote repository to your local subversion
  repository.
endef

DISTFILES += COPYING

PACKAGES = CSWpmsvnmirror
CATALOGNAME = pm_svnmirror
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmdatauuid CSWpmsvn CSWsvn
RUNTIME_DEP_PKGS += CSWpmsvnsimple CSWpmtermreadkey CSWpmuri

# VCP Support (disabled for now)
PATCHFILES += novcp.diff

# Test suite takes >20m, 0.67/SPARC
TEST_SCRIPTS =

include gar/category.mk
