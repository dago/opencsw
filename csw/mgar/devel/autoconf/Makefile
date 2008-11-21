GARNAME = autoconf
GARVERSION = 2.63
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

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = use-csw-tools.patch

PREREQUISITE_PKGS = CSWhelp2man

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Tests take a loooooonnng time.
TEST_SCRIPTS =

include ../category.mk

# Package has two bad string which should be ignored:
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autoconf-mode.el
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autotest-mode.el
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/emacs/site-lisp

post-install:
	@echo " ==> Fixing install anomalies"

	@rm -f $(DESTDIR)$(prefix)/share/info/dir
	@rm -f $(DESTDIR)$(prefix)/share/info/standards.info
