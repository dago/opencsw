GARNAME = autoconf
GARVERSION = 2.61
CATEGORIES = devel

DESCRIPTION = GNU auto-configuration tool
define BLURB
  Autoconf is an extensible package of m4 macros that produce shell scripts to
  automatically configure software source code packages. These scripts can adapt
  the package to many kinds of UNIX-like systems without manual user
  intervention.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWautoconf,depend)

DEPENDS = utils/sed utils/sh-utils

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Tests take a loooooonnng time.
TEST_SCRIPTS =

include ../category.mk

# Package has two bad string which should be ignored:
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autoconf-mode.el
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autotest-mode.el
# As we don't want the whole test to be skipped we strip the offending part from the comments
#SPKG_SKIP_COMPLIANCE_CHECK = 1

post-install:
	@echo " ==> Fixing install anomalies"

	@for f in share/emacs/site-lisp/autoconf-mode.elc share/emacs/site-lisp/autotest-mode.elc; do \
		perl -pi -e 's!/export/medusa!! if( /^;;;/ )' $(DESTDIR)$(prefix)/$$f; \
	done
	@rm -f $(DESTDIR)$(prefix)/share/info/dir
