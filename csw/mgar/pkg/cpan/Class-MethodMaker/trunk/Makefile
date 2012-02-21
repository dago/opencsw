NAME = Class-MethodMaker
VERSION = 2.18
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SCHWIGON

DESCRIPTION = A module for creating generic methods
define BLURB
endef

CATALOG_RELEASE = unstable

PACKAGES += CSWpm-class-methodmaker
CATALOGNAME_CSWpm-class-methodmaker = pm_class_methodmaker
SPKG_DESC_CSWpm-class-methodmaker = A module for creating generic methods

# These is really no license file in the package
CHECKPKG_OVERRIDES_CSWpm-class-methodmaker += license-missing|/opt/csw/share/doc/pm_class_methodmaker/license

# Too many args confuse MakeMaker
CONFIGURE_ARGS =

include gar/category.mk
