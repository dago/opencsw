NAME = Error
VERSION = 0.17018
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHLOMIF

DESCRIPTION = Error/exception handling in an OO-ish way
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

PACKAGES += CSWpm-error
CATALOGNAME_CSWpm-error = pm_error
SPKG_DESC_CSWpm-error = Error/exception handling in an OO-ish way
ARCHALL_CSWpm-error = 1
OBSOLETED_BY_CSWpm-error += CSWpmerror
CATALOGNAME_CSWpmerror = pm_error_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
