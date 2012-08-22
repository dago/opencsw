NAME = XML-SemanticDiff
VERSION = 1.0000
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHLOMIF

DESCRIPTION = Perl extension for comparing XML documents
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-xml-semanticdiff
CATALOGNAME_CSWpm-xml-semanticdiff = pm_xml_semanticdiff
SPKG_DESC_CSWpm-xml-semanticdiff = Perl extension for comparing XML documents
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-xml-semanticdiff = 1
RUNTIME_DEP_PKGS_CSWpm-xml-semanticdiff += CSWpm-xml-parser
OBSOLETED_BY_CSWpm-xml-semanticdiff += CSWpmxmlsemdiff
CATALOGNAME_CSWpmxmlsemdiff = pm_xmlsemdiff_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
