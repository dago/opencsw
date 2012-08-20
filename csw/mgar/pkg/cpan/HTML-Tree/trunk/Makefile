NAME = HTML-Tree
VERSION = 5.02
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CJM

DESCRIPTION = Work with HTML in a DOM-like tree structure
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-html-tree
CATALOGNAME_CSWpm-html-tree = pm_html_tree
SPKG_DESC_CSWpm-html-tree = Work with HTML in a DOM-like tree structure
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-html-tree = 1
RUNTIME_DEP_PKGS_CSWpm-html-tree += CSWpm-html-parser
RUNTIME_DEP_PKGS_CSWpm-html-tree += CSWpm-html-tagset
OBSOLETED_BY_CSWpm-html-tree += CSWpmhtmltree
CATALOGNAME_CSWpmhtmltree = pm_htmltree_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
