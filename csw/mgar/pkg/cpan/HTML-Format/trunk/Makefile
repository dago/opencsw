NAME = HTML-Format
VERSION = 2.10
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = NIGELM

DESCRIPTION = Base class for HTML formatters
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpmfileslurp
BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-html-formatter
CATALOGNAME_CSWpm-html-formatter = pm_html_formatter
SPKG_DESC_CSWpm-html-formatter = Base class for HTML formatters
ARCHALL_CSWpm-html-formatter = 1
RUNTIME_DEP_PKGS_CSWpm-html-formatter += CSWpm-font-afm
RUNTIME_DEP_PKGS_CSWpm-html-formatter += CSWpm-html-tree
OBSOLETED_BY_CSWpm-html-formatter += CSWpmhtmlformat
CATALOGNAME_CSWpmhtmlformat = pm_htmlformat_stub
OBSOLETED_BY_CSWpm-html-format += CSWpmhtmlfmt
CATALOGNAME_CSWpmhtmlfmt = pm_htmlfmt_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
