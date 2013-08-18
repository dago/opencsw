NAME = Test-XML
VERSION = 0.08
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SEMANTICO

DESCRIPTION = Compare XML in perl tests
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-xml-semanticdiff

PACKAGES += CSWpm-test-xml
CATALOGNAME_CSWpm-test-xml = pm_test_xml
SPKG_DESC_CSWpm-test-xml = Compare XML in perl tests
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-test-xml = 1
RUNTIME_DEP_PKGS_CSWpm-test-xml += CSWpm-xml-semanticdiff
RUNTIME_DEP_PKGS_CSWpm-test-xml += CSWpm-xml-parser
OBSOLETED_BY_CSWpm-test-xml += CSWpmtestxml
CATALOGNAME_CSWpmtestxml = pm_testxml_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
