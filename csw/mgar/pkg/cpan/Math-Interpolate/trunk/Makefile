NAME = Math-Interpolate
VERSION = 1.05
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BZAJAC

DESCRIPTION = Interpolate the value Y from X using a list of pairs
define BLURB
endef

CATALOG_RELEASE = unstable

PACKAGES += CSWpm-math-interpolate
CATALOGNAME_CSWpm-math-interpolate = pm_math_interpolate
SPKG_DESC_CSWpm-math-interpolate = Interpolate the value Y from X using a list of pairs
ARCHALL_CSWpm-math-interpolate = 1
OBSOLETED_BY_CSWpm-math-interpolate += CSWpmmathinterpolate
CATALOGNAME_CSWpmmathinterpolate = pm_mathinterpolate_stub

# There is really no license
CHECKPKG_OVERRIDES_CSWpm-math-interpolate += license-missing
CHECKPKG_OVERRIDES_CSWpmmathinterpolate += license-missing

# This is a problem in checkpkg, override for now
CHECKPKG_OVERRIDES_CSWpmmathinterpolate += action-class-only-in-pkginfo|none

include gar/category.mk
