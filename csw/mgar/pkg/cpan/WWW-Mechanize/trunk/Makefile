NAME = WWW-Mechanize
VERSION = 1.66
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PETDANCE

DESCRIPTION = Handy web browsing in a Perl object
define BLURB
  WWW::Mechanize, or Mech for short, helps you automate interaction with a
  website. It supports performing a sequence of page fetches including
  following links and submitting forms. Each fetched page is parsed and its
  links and forms are extracted. A link or a form can be selected, form fields
  can be filled and the next page can be fetched. Mech also stores a history
  of the URLs you've visited, which can be queried and revisited.
endef

DISTFILES += COPYING

PACKAGES = CSWpmwwwmechanize
CATALOGNAME = pm_wwwmechanize
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmhtmlparser
RUNTIME_DEP_PKGS += CSWpmhttpsvrsimp
RUNTIME_DEP_PKGS += CSWpmlibwww
RUNTIME_DEP_PKGS += CSWpmuri

CONFIGURE_ARGS = -nolive -nolocal

include gar/category.mk
