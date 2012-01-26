NAME = prefork
VERSION = 1.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Optimized module loading for forking or non-forking processes
define BLURB
endef

PACKAGES = CSWpmprefork
CATALOGNAME = pm_prefork

LICENSE = LICENSE

ARCHALL = 1

# Yes, the module names violates the Perl standard
CHECKPKG_OVERRIDES_CSWpmprefork += pkginfo-description-not-starting-with-uppercase

include gar/category.mk
