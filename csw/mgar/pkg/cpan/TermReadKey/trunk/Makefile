GARNAME = TermReadKey
GARVERSION = 2.30
CATEGORIES = cpan
AUTHOR = JSTOWE

DESCRIPTION = module for simple terminal control
define BLURB
  Term::ReadKey is a compiled perl module dedicated to providing simple
  control over terminal driver modes (cbreak, raw, cooked, etc.,) support for
  non-blocking reads, if the architecture allows, and some generalized handy
  functions for working with terminals. One of the main goals is to have the
  functions as portable as possible, so you can just plug in "use
  Term::ReadKey" on any architecture and have a good likelyhood of it working.
endef

DISTFILES = $(call admfiles,CSWpmtermreadkey,depend prototype)

DEPENDS += lib/ncurses

include gar/category.mk
