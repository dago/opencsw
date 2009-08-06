GARNAME = Module-Pluggable
GARVERSION = 3.9
CATEGORIES = cpan
AUTHOR = SIMONW

DESCRIPTION = Automatically give your module the ability to have plugins
define BLURB
  Provides a simple but, hopefully, extensible way of having 'plugins' for
  your module. Obviously this isn't going to be the be all and end all of
  solutions but it works for me.  Essentially all it does is export a method
  into your namespace that looks through a search path for .pm files and turn
  those into class names.  Optionally it instantiates those classes for you.
endef

PACKAGES = CSWpmmoduleplug
CATALOGNAME = pm_moduleplug

ARCHALL = 1

include gar/category.mk
