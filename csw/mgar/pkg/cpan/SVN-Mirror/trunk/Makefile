NAME = SVN-Mirror
VERSION = 0.75
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CLKAO

DESCRIPTION = Mirror remote repository to local Subversion repository
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-svn-mirror
CATALOGNAME = pm_svn_mirror
SPKG_DESC_CSWpm-svn-mirror = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-svn-mirror = CSWpmsvnmirror
CATALOGNAME_CSWpmsvnmirror = pm_svnmirror

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-class-accessor
RUNTIME_DEP_PKGS += CSWpm-timedate
RUNTIME_DEP_PKGS += CSWpmfilechdir
RUNTIME_DEP_PKGS += CSWpmsvn
RUNTIME_DEP_PKGS += CSWpm-svn-simple-edit
RUNTIME_DEP_PKGS += CSWpm-term-readkey
RUNTIME_DEP_PKGS += CSWpm-uri

# VCP Support (disabled for now)
PATCHFILES += novcp.diff

# Test suite takes >20m, 0.67/SPARC
TEST_SCRIPTS =

include gar/category.mk
