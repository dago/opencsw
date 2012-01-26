NAME = SVN-Simple
VERSION = 0.27
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CLKAO

DESCRIPTION = a simple interface for driving svn delta editors
define BLURB
  SVN::Simple::Edit wraps the subversion delta editor with a perl friendly
  interface and then you could easily drive it for describing changes to a
  tree.  A common usage is to wrap the commit editor, so you could make
  commits to a subversion repository easily.
endef

DISTFILES = $(call admfiles,CSWpmsvnsimple,depend prototype)

DEPENDS += utils/subversion

include gar/category.mk
