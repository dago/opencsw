GARNAME = Sub-Uplevel
GARVERSION = 0.09
CATEGORIES = cpan
AUTHOR = MSCHWERN

DESCRIPTION = apparently run a function in a higher stack frame
define BLURB
  Like Tcl's uplevel() function, but not quite so dangerous. The idea is just
  to fool caller(). All the really naughty bits of Tcl's uplevel() are
  avoided.  THIS IS NOT THE SORT OF THING YOU WANT TO DO EVERYDAY
endef

DISTFILES += $(call admfiles,CSWpmsubuplevel,prototype)

include ../category.mk
