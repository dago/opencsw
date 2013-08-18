NAME = File-Type
VERSION = 0.22
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PMISON

DESCRIPTION = 
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-file-type
CATALOGNAME_CSWpm-file-type = pm_file_type
SPKG_DESC_CSWpm-file-type = Determine file type using magic
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-file-type = 1
OBSOLETED_BY_CSWpm-file-type += CSWpmfiletype
CATALOGNAME_CSWpmfiletype = pm_filetype_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
