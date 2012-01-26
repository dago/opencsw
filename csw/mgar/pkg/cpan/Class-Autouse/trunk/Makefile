NAME = Class-Autouse
VERSION = 1.29
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Run-time class loading on first method call
define BLURB
  Class::Autouse allows you to specify a class the will only load when a
  method of that class is called. For large classes that might not be used
  during the running of a program, such as Date::Manip, this can save you
  large amounts of memory, and decrease the script load time a great deal.
endef

PACKAGES = CSWpmclassautouse CSWpmclsautouse

CATALOGNAME_CSWpmclassautouse = pm_classautouse
CATALOGNAME_CSWpmclsautouse = pm_clsautouse

SPKG_DESC_CSWpmclassautouse = $(DESCRIPTION)
SPKG_DESC_CSWpmclsautouse = Empty stub as contents has been moved to CSWpmclassautouse

RUNTIME_DEP_PKGS_ONLY_CSWpmclsautouse = CSWpmclassautouse

LICENSE = LICENSE

ARCHALL = 1

PKGFILES_CSWpmclsautouse = NOFILES

include gar/category.mk
