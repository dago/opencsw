GARNAME = Term-UI
GARVERSION = 0.20
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Term::ReadLine UI made easy
define BLURB
  Term::UI is a transparent way of eliminating the overhead of having to
  format a question and then validate the reply, informing the user if the
  answer was not proper and re-issuing the question.
endef

DISTFILES += COPYING

PACKAGES = CSWpmtermui
CATALOGNAME = pm_termui
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmlclemktxtsimple CSWpmlogmsgsimple CSWpmprmscheck

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
