NAME = gettext
VERSION = 1.05
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PVANDRY

DESCRIPTION = Message handling functions
define BLURB
  The gettext module permits access from perl to the gettext() family
  of functions for retrieving message strings from databases constructed
  to internationalize software.
endef

DISTFILES = COPYING

# Compatibility patches for Perl 5.10.1 from
#   https://rt.cpan.org/Public/Bug/Display.html?id=35680
PATCHFILES  = compatibility-with-POSIX-module.diff
PATCHFILES += doc-update.diff

PACKAGES = CSWpmlocalegettext
CATALOGNAME = pm_localegettext

RUNTIME_DEP_PKGS = CSWggettextrt

# The Perl module really does not start with uppercase...
CHECKPKG_OVERRIDES_CSWpmlocalegettext += pkginfo-description-not-starting-with-uppercase

include gar/category.mk

BUILD_ARGS += OTHERLDFLAGS="-lintl -R$(libdir)"
