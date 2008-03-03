GARNAME = Attribute-Handlers
GARVERSION = 0.78
CATEGORIES = cpan
AUTHOR = ABERGMAN

DESCRIPTION = simpler definition of attribute handlers
define BLURB
  This module, when inherited by a package, allows that package's class to set
  up attribute handler subroutines for specific attributes. Variables and
  subroutines subsequently defined in that package, or in packages derived
  from that package may be given attributes with the same names as the
  attribute handler subroutines, which will then be called in one of the
  compilation phases (i.e. in a BEGIN, CHECK, INIT, or END block).
endef

DISTFILES += CSWpmattrhnd.gspec

include gar/category.mk
