GARNAME = WWW-Mechanize
GARVERSION = 1.22
CATEGORIES = cpan
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

DISTFILES += $(call admfiles,CSWpmwwwmechanize,depend)

DEPENDS   += cpan/libwww-perl
DEPENDS   += cpan/HTML-Parser

BUILDDEPS += cpan/Test-LongString
BUILDDEPS += cpan/Test-Warn
BUILDDEPS += cpan/Test-Pod
BUILDDEPS += cpan/Test-Memory-Cycle

CONFIGURE_ARGS = -n

include ../category.mk
