NAME = MouseX-Traits
VERSION = 0.1102
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GFUJI

DESCRIPTION = Automatically apply roles at object creation time
define BLURB
endef

CATALOG_RELEASE = unstable

BUILD_DEP_PKGS += CSWpm-ok
BUILD_DEP_PKGS += CSWpm-test-exception

# Really no license
CHECKPKG_OVERRIDES_CSWpm-mousex-traits += license-missing|/opt/csw/share/doc/pm_mousex_traits/license

PACKAGES += CSWpm-mousex-traits
CATALOGNAME_CSWpm-mousex-traits = pm_mousex_traits
SPKG_DESC_CSWpm-mousex-traits = Automatically apply roles at object creation time
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-mousex-traits = 1
RUNTIME_DEP_PKGS_CSWpm-mousex-traits += CSWpm-mouse

include gar/category.mk
