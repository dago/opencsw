NAME = Parse-Netstat
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Parse the output of Unix "netstat" command
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-parse-netstat
CATALOGNAME_CSWpm-parse-netstat = pm_parse_netstat
SPKG_DESC_CSWpm-parse-netstat = Parse the output of Unix "netstat" command
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-parse-netstat = 1
RUNTIME_DEP_PKGS_CSWpm-parse-netstat += CSWpm-rinci
RUNTIME_DEP_PKGS_CSWpm-parse-netstat += CSWpm-exporter-lite

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
