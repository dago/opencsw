NAME = Class-Container
VERSION = 0.12
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KWILLIAMS

DESCRIPTION = Glues object frameworks together transparently
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-class-container
CATALOGNAME_CSWpm-class-container = pm_class_container
SPKG_DESC_CSWpm-class-container = Glues object frameworks together transparently
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-class-container = 1
RUNTIME_DEP_PKGS_CSWpm-class-container += CSWpm-params-validate
OBSOLETED_BY_CSWpm-class-container += CSWpmclscontainer
CATALOGNAME_CSWpmclscontainer = pm_clscontainer_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
