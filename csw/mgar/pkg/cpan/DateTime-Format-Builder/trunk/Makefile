NAME = DateTime-Format-Builder
VERSION = 0.80
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Create DateTime parser classes and objects
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = COPYING

PACKAGES += CSWpm-datetime-format-builder
CATALOGNAME_CSWpm-datetime-format-builder = pm_datetime_format_builder
SPKG_DESC_CSWpm-datetime-format-builder = Create DateTime parser classes and objects
ARCHALL_CSWpm-datetime-format-builder = 1
RUNTIME_DEP_PKGS_CSWpm-datetime-format-builder += CSWpm-datetime
RUNTIME_DEP_PKGS_CSWpm-datetime-format-builder += CSWpm-task-weaken
RUNTIME_DEP_PKGS_CSWpm-datetime-format-builder += CSWpm-params-validate
RUNTIME_DEP_PKGS_CSWpm-datetime-format-builder += CSWpm-datetime-format-strptime
RUNTIME_DEP_PKGS_CSWpm-datetime-format-builder += CSWpmclassfactutil

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
