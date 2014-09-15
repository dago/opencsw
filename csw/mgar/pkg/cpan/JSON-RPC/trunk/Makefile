NAME = JSON-RPC
VERSION = 1.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DMAKI

DESCRIPTION = JSON RPC 2.0 Server Implementation
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-plack

PACKAGES += CSWpm-json-rpc
CATALOGNAME_CSWpm-json-rpc = pm_json_rpc
SPKG_DESC_CSWpm-json-rpc = JSON RPC 2.0 Server Implementation
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-json-rpc = 1
RUNTIME_DEP_PKGS_CSWpm-json-rpc += CSWpm-json
RUNTIME_DEP_PKGS_CSWpm-json-rpc += CSWpm-libwww-perl
RUNTIME_DEP_PKGS_CSWpm-json-rpc += CSWpm-class-accessor-lite
RUNTIME_DEP_PKGS_CSWpm-json-rpc += CSWpm-plack
RUNTIME_DEP_PKGS_CSWpm-json-rpc += CSWpm-http-message
RUNTIME_DEP_PKGS_CSWpm-json-rpc += CSWpm-router-simple

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
