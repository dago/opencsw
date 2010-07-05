GARNAME = autoconf
GARVERSION = 2.66
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

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = 0001-Prefer-CSW-tools.patch

BUILD_DEP_PKGS = CSWhelp2man
RUNTIME_DEP_PKGS = CSWgawk CSWgm4 CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Tests take a loooooonnng time.
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = $(infodir)/standards.info

CHECKPKG_OVERRIDES_CSWautoconf += missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES_CSWautoconf += surplus-dependency|CSWgm4
CHECKPKG_OVERRIDES_CSWautoconf += surplus-dependency|CSWgawk

include gar/category.mk

# Package has two bad string which should be ignored:
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autoconf-mode.el
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autotest-mode.el
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/emacs/site-lisp

post-install-modulated:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(prefix)/share/info/standards.info
