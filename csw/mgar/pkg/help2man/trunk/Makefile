NAME = help2man
VERSION = 1.40.5
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = A tool for automatically generating simple manual pages from program output
define BLURB
  help2man is a tool for automatically generating simple manual pages from program output.
  It is intended to provide an easy way for software authors to include a manual page
  in their distribution without having to maintain that document.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWhelp2man
SPKG_DESC_CSWhelp2man = A tool for automatically generating simple manual pages from program output
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWhelp2man += CSWpm-locale-gettext
# Perl module dependency cannot be tracked by checkpkg
CHECKPKG_OVERRIDES_CSWhelp2man += surplus-dependency|CSWpm-locale-gettext

REINPLACE_USRSHARE += help2man.info

REINPLACEMENTS += usrlib
REINPLACE_MATCH_usrlib = /usr/lib
REINPLACE_WITH_usrlib = $(libdir)
REINPLACE_FILES_usrlib += help2man.info

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk
