NAME = SHARYANTO-Utils
VERSION = 0.53
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = SHARYANTO's temporary namespace for various routines
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-file-chdir
BUILD_DEP_PKGS += CSWpm-test-exception
BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-sharyanto-proc-util
CATALOGNAME_CSWpm-sharyanto-proc-util = pm_sharyanto_proc_util
SPKG_DESC_CSWpm-sharyanto-proc-util = SHARYANTO's temporary namespace for various routines
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-sharyanto-proc-util = 1
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-rinci
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-template-tiny
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-uri
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-log-any
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-parse-netstat
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-locale-maketext-lexicon
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-file-which
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-yaml-syck
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-moo
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-data-clone
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-experimental
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-data-structure-util
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-html-parser
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-file-slurp
RUNTIME_DEP_PKGS_CSWpm-sharyanto-proc-util += CSWpm-perinci-object

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
