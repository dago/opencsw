# $Id$

NAME = autoconf
VERSION = 2.69
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

PATCHFILES = 0001-Prefer-CSW-tools.patch

VENDOR_URL = http://www.gnu.org/software/autoconf/

BUILD_DEP_PKGS += CSWhelp2man

# We need the Fortran runtime libs or the Fortran tests with fail
BUILD_DEP_PKGS += CSWss12f95rt

PACKAGES += CSWautoconf
SPKG_DESC_CSWautoconf = GNU auto-configuration tool
# PKGFILES is catchall
ARCHALL_CSWautoconf = 1
RUNTIME_DEP_PKGS_CSWautoconf += CSWperl
RUNTIME_DEP_PKGS_CSWautoconf += CSWgawk
RUNTIME_DEP_PKGS_CSWautoconf += CSWgm4
# checkpkg cannot track these
CHECKPKG_OVERRIDES_CSWautoconf += surplus-dependency|CSWgm4
CHECKPKG_OVERRIDES_CSWautoconf += surplus-dependency|CSWgawk

# This is just for the emacs style
CHECKPKG_OVERRIDES_CSWautoconf += missing-dependency|CSWemacscommon

# These are just docs
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/local|root/opt/csw/share/autoconf/INSTALL
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/local|root/opt/csw/share/info/autoconf.info
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/share|root/opt/csw/share/info/autoconf.info

# The search pathes also include /usr/local among others
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/local|root/opt/csw/share/autoconf/autoconf/autoconf.m4f
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/local|root/opt/csw/share/autoconf/autoconf/functions.m4
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/local|root/opt/csw/share/autoconf/autoconf/general.m4
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/local|root/opt/csw/share/autoconf/autoconf/fortran.m4
CHECKPKG_OVERRIDES_CSWautoconf += file-with-bad-content|/usr/local|root/opt/csw/share/autoconf/autoconf/libs.m4

EXTRA_MERGE_EXCLUDE_FILES = $(infodir)/standards.info

include gar/category.mk

# Package has two bad string which should be ignored:
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autoconf-mode.el
#   ;;; from file /export/medusa/dam/build/csw/devel/autoconf/work/dam-ra.d/autoconf-2.61/lib/emacs/elc.15767/autotest-mode.el
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/emacs/site-lisp

post-install-modulated:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(prefix)/share/info/standards.info
