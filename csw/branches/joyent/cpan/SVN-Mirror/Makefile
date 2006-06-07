GARNAME = SVN-Mirror
GARVERSION = 0.68
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = mirror remote repository to local Subversion repository
define BLURB
  SVN::Mirror allows you to mirror remote repository to your local subversion
  repository. 
endef

DISTFILES = $(call admfiles,CSWpmsvnmirror,depend)

DEPENDS += utils/subversion
DEPENDS += cpan/TermReadKey cpan/SVN-Simple cpan/URI
DEPENDS += cpan/Class-Accessor cpan/File-chdir

# VCP Support (disabled for now)
#DEPENDS += cpan/VCP cpan/Data-UUID
PATCHFILES += novcp.diff

# Test suite takes >20m, 0.67/SPARC
ENABLE_TEST = 0

include ../category.mk
