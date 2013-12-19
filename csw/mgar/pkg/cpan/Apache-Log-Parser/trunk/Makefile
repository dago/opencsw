NAME = Apache-Log-Parser
VERSION = 0.02
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TAGOMORIS

DESCRIPTION = Parser for Apache Log
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-exception
BUILD_DEP_PKGS += CSWpm-test-deep

PACKAGES += CSWpm-apache-log-parser
CATALOGNAME_CSWpm-apache-log-parser = pm_apache_log_parser
SPKG_DESC_CSWpm-apache-log-parser = Parser for Apache Log (common, combined, and any other custom styles by LogFormat)
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-apache-log-parser = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
