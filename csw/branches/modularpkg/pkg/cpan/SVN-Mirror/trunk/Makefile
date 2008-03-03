GARNAME = SVN-Mirror
GARVERSION = 0.72
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = mirror remote repository to local Subversion repository
define BLURB
  SVN::Mirror allows you to mirror remote repository to your local subversion
  repository.
endef

DISTFILES = $(call admfiles,CSWpmsvnmirror,depend)

DEPENDS += utils/subversion
DEPENDS += cpan/TermReadKey
DEPENDS += cpan/SVN-Simple
DEPENDS += cpan/URI
DEPENDS += cpan/Class-Accessor
DEPENDS += cpan/File-chdir

# VCP Support (disabled for now)
#DEPENDS += cpan/VCP
#DEPENDS += cpan/Data-UUID
PATCHFILES += novcp.diff

# Test suite takes >20m, 0.67/SPARC
TEST_SCRIPTS =

include gar/category.mk
