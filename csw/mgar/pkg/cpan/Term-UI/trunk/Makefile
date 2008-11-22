GARNAME = Term-UI
GARVERSION = 0.14
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Term::ReadLine UI made easy
define BLURB
  Term::UI is a transparent way of eliminating the overhead of having to
  format a question and then validate the reply, informing the user if the
  answer was not proper and re-issuing the question.
endef

DISTFILES = $(call admfiles,CSWpmtermui,depend prototype)

DEPENDS += cpan/Params-Check
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/Log-Message-Simple

include ../category.mk
