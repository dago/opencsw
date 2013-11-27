NAME = MARC-XML
VERSION = 1.0.1
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GMCHARLT

DESCRIPTION = MAchine Readable Catalog / XML Extension
define BLURB
endef

# This is due to our old version of MakeMaker
PATCHFILES += 0001-Only-one-author-allowed.patch

CATALOG_RELEASE = unstable

BUILD_DEP_PKGS += CSWpm-marc-charset
BUILD_DEP_PKGS += CSWpm-marc-record

PACKAGES += CSWpm-marc-xml
CATALOGNAME_CSWpm-marc-xml = pm_marc_xml
SPKG_DESC_CSWpm-marc-xml = MAchine Readable Catalog / XML Extension
ARCHALL_CSWpm-marc-xml = 1
RUNTIME_DEP_PKGS_CSWpm-marc-xml += CSWpm-marc-charset
RUNTIME_DEP_PKGS_CSWpm-marc-xml += CSWpm-marc-record
OBSOLETED_BY_CSWpm-marc-xml += CSWpmmarcxml
CATALOGNAME_CSWpmmarcxml = pm_marcxml_stub

include gar/category.mk
