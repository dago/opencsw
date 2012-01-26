NAME = sol-inst
VERSION = 0.90a
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHRISJ

DESCRIPTION = access basic Solaris installation information
define BLURB
  sol-inst is a collection of Perl modules to access basic installation
  information on a Solaris system.
endef

UFILES_REGEX ?= $(NAME)-((\d+(?:\.\d+)*)(a)?).tar.gz

WORKSRC = $(WORKDIR)/Solaris

DISTFILES += CSWpmsolinst.gspec

include gar/category.mk
