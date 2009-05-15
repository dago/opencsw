GARNAME = Time-Format
GARVERSION = 1.09
CATEGORIES = cpan
AUTHOR = ROODE

DESCRIPTION = Easy-to-use date/time formatting
define BLURB
  Time::Format provides a very easy way to format dates and times. The
  formatting functions are tied to hash variables, so they can be used inside
  strings as well as in ordinary expressions. The formatting codes used are
  meant to be easy to remember, use, and read.
endef

PACKAGES = CSWpmtimeformat
CATALOGNAME = pm_timeformat
ARCHALL = 1

include gar/category.mk

pre-merge-modulated:
	@cd $(WORKSRC) && sed -n '/^Copyright/,/^$$/p' README > COPYING
	@$(MAKECOOKIE)
