NAME = Tree-Simple
VERSION = 1.23
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RSAVAGE

DESCRIPTION = A simple tree object
define BLURB
endef

MODDIST = Tree-Simple-1.23.tgz

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details https://www.gnu.org/licenses/license-list.html#PerlLicense

BUILD_DEP_PKGS += CSWpm-test-version
BUILD_DEP_PKGS += CSWpm-test-exception

PACKAGES += CSWpm-tree-simple
CATALOGNAME_CSWpm-tree-simple = pm_tree_simple
SPKG_DESC_CSWpm-tree-simple = A simple tree object
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-tree-simple = 1
OBSOLETED_BY_CSWpm-tree-simple += CSWpmtreesimple
CATALOGNAME_CSWpmtreesimple = pm_treesimple_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
