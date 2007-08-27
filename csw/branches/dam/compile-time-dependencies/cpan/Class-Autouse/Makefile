GARNAME = Class-Autouse
GARVERSION = 1.27
CATEGORIES = cpan
AUTHOR = ADAMK

DESCRIPTION = Run-time class loading on first method call
define BLURB
  Class::Autouse allows you to specify a class the will only load when a
  method of that class is called. For large classes that might not be used
  during the running of a program, such as Date::Manip, this can save you
  large amounts of memory, and decrease the script load time a great deal.
endef

DISTFILES = $(call admfiles,CSWpmclsautouse,depend prototype)

include ../category.mk
