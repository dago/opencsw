NAME = Term-ReadLine-Gnu
VERSION = 1.19
CATEGORIES = cpan
AUTHOR = HAYASHI

DESCRIPTION = Perl extension for the GNU Readline/History Library
define BLURB
  This is an implementation of Term::ReadLine using the GNU Readline/History
  Library.
endef

PACKAGES = CSWpmtermreadlineg
CATALOGNAME = pm_termreadlineg

RUNTIME_DEP_PKGS = CSWreadline

# readline.h (CSWreadline) is inconsistent and breaks our test, therefor we
# will patch that test for the time beeing
PATCHFILES = patch-readline.t

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
