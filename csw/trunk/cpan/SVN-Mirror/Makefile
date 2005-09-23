GARNAME = SVN-Mirror
GARVERSION = 0.66
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = mirror remote repository to local Subversion repository
define BLURB
  SVN::Mirror allows you to mirror remote repository to your local subversion
  repository. 
endef

DISTFILES += CSWpmsvnmirror.gspec CSWpmsvnmirror.depend

DEPENDS += utils/subversion
DEPENDS += cpan/TermReadKey cpan/SVN-Simple cpan/URI

# Not quite ready for prime time
PATCHFILES += novcp.diff
#DEPENDS += cpan/VCP cpan/Data-UUID

include ../category.mk
