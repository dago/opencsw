# $Id$

NAME = autoconf
VERSION = 2.13
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = GNU auto-configuration tool
define BLURB
  Autoconf is an extensible package of m4 macros that produce shell scripts to
  automatically configure software source code packages. These scripts can adapt
  the package to many kinds of UNIX-like systems without manual user
  intervention.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

# PATCHFILES = 0001-Prefer-CSW-tools.patch
PATCHFILES += 0002-Use-DESTDIR.patch

PACKAGES += CSWautoconf2-13
ARCHALL_CSWautoconf2-13 = 1

BUILD_DEP_PKGS = CSWhelp2man

# We need the Fortran runtime libs or the Fortran tests with fail
BUILD_DEP_PKGS += CSWss12f95rt

RUNTIME_DEP_PKGS = CSWgawk CSWgm4 CSWperl

VENDOR_URL = http://www.gnu.org/software/autoconf/

datadir = $(prefix)/share/autoconf-$(VERSION)
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-suffix="-$(VERSION)"

# Tests take a loooooonnng time.
# TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = $(infodir)/standards.info
EXTRA_MERGE_EXCLUDE_FILES += $(infodir)/autoconf.info

CHECKPKG_OVERRIDES_CSWautoconf2-13 += missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES_CSWautoconf2-13 += surplus-dependency|CSWgm4
CHECKPKG_OVERRIDES_CSWautoconf2-13 += surplus-dependency|CSWgawk
CHECKPKG_OVERRIDES_CSWautoconf2-13 += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWautoconf2-13 += file-with-bad-content

include gar/category.mk

# Package has two bad string which should be ignored:
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autoconf-mode.el
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autotest-mode.el
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/emacs/site-lisp

post-install-modulated:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(prefix)/share/info/standards.info
