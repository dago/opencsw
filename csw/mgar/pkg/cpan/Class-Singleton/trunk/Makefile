GARNAME = Class-Singleton
GARVERSION = 1.4
CATEGORIES = cpan
AUTHOR = ABW

DESCRIPTION = Implementation of a "Singleton" class
define BLURB
  This is the Class::Singleton module. A Singleton describes an object
  class that can have only one instance in any system. An example of a
  Singleton might be a print spooler or system registry. This module
  implements a Singleton class from which other classes can be derived. By
  itself, the Class::Singleton module does very little other than manage
  the instantiation of a single object. In deriving a class from
  Class::Singleton, your module will inherit the Singleton instantiation
  method and can implement whatever specific functionality is
  required.
endef

PACKAGES = CSWpmclasssingleton
CATALOGNAME = pm_classsingleton

ARCHALL = 1

include gar/category.mk

pre-merge-modulated:
	@cd $(WORKSRC) && sed -n '/^Copyright/,$$p' README > COPYING
	@$(MAKECOOKIE)
