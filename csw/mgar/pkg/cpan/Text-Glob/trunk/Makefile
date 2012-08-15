NAME = Text-Glob
VERSION = 0.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCLAMP

DESCRIPTION = Match globbing patterns against text
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

PACKAGES += CSWpm-text-glob
CATALOGNAME_CSWpm-text-glob = pm_text_glob
SPKG_DESC_CSWpm-text-glob = Match globbing patterns against text
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-text-glob = 1
OBSOLETED_BY_CSWpm-text-glob += CSWpmtextglob
CATALOGNAME_CSWpmtextglob = pm_textglob_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
