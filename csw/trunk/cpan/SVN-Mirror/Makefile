GARNAME = SVN-Mirror
GARVERSION = 0.67
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = mirror remote repository to local Subversion repository
define BLURB
  SVN::Mirror allows you to mirror remote repository to your local subversion
  repository. 
endef

DISTFILES = $(call admfiles,CSWpmsvnmirror,depend)

DEPENDS += utils/subversion
DEPENDS += cpan/TermReadKey cpan/SVN-Simple cpan/URI cpan/VCP
DEPENDS += cpan/Data-UUID cpan/Class-Accessor

include ../category.mk
