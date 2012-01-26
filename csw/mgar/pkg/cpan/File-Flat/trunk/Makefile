NAME = File-Flat
VERSION = 1.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Implements a flat filesystem
define BLURB
endef

PACKAGES = CSWpmfileflat
CATALOGNAME = pm_fileflat

RUNTIME_DEP_PKGS = CSWpmprefork CSWpmfileslurp CSWpmfileremove CSWpmfilecpyrecurs
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWpmtestclassapi

LICENSE = LICENSE

ARCHALL = 1

include gar/category.mk
