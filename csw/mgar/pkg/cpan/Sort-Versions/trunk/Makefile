NAME = Sort-Versions
VERSION = 1.5
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = EDAVIS

DESCRIPTION = A module for sorting of revision-like numbers
define BLURB
  Sort::Versions allows easy sorting of mixed non-numeric and numeric strings,
  like the 'version numbers' that many shared library systems and revision
  control packages use. This is quite useful if you are trying to deal with
  shared libraries. It can also be applied to applications that intersperse
  variable-width numeric fields within text. Other applications can
  undoubtedly be found.
endef

DISTFILES = COPYING

PACKAGES = CSWpmsortversions CSWpmsortver

CATALOGNAME_CSWpmsortversions = pm_sortversions
CATALOGNAME_CSWpmsortver = pm_sortver

SPKG_DESC_CSWpmsortversions = $(DESCRIPTION)
SPKG_DESC_CSWpmsortver = Empty stub as contents has been moved to CSWpmsortversions

RUNTIME_DEP_PKGS_ONLY_CSWpmsortver = CSWpmsortversions

ARCHALL = 1

PKGFILES_CSWpmsortver = NOFILES

include gar/category.mk
