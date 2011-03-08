NAME = Term-UI
VERSION = 0.26
CATEGORIES = cpan
AUTHOR = BINGOS

DESCRIPTION = Term::ReadLine UI made easy
define BLURB
  Term::UI is a transparent way of eliminating the overhead of having to
  format a question and then validate the reply, informing the user if the
  answer was not proper and re-issuing the question.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-term-ui
CATALOGNAME = pm_term_ui
SPKG_DESC_CSWpm-term-ui = $(DESCRIPTION)
OBSOLETES_CSWpm-term-ui = CSWpmtermui
CATALOGNAME_CSWpmtermui = pm_termui

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmlclemktxtsimple
RUNTIME_DEP_PKGS += CSWpm-log-message-simple
RUNTIME_DEP_PKGS += CSWpm-params-check

# Not yet released/renamed packages
CHECKPKG_OVERRIDES_CSWpm-term-ui += unidentified-dependency|CSWpm-params-check
CHECKPKG_OVERRIDES_CSWpm-term-ui += unidentified-dependency|CSWpm-log-message-simple

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
