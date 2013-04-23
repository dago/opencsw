NAME = XML-SAX-Expat
VERSION = 0.40
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BJOERN

DESCRIPTION = SAX Driver for Expat
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

DISTFILES += CSWpm-xml-sax-expat.postinstall
DISTFILES += CSWpm-xml-sax-expat.preremove

PACKAGES += CSWpm-xml-sax-expat
CATALOGNAME_CSWpm-xml-sax-expat = pm_xml_sax_expat
SPKG_DESC_CSWpm-xml-sax-expat = SAX Driver for Expat
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-xml-sax-expat = 1
RUNTIME_DEP_PKGS_CSWpm-xml-sax-expat += CSWpm-xml-sax
RUNTIME_DEP_PKGS_CSWpm-xml-sax-expat += CSWpm-xml-namespacesupport
RUNTIME_DEP_PKGS_CSWpm-xml-sax-expat += CSWpm-xml-sax-base
RUNTIME_DEP_PKGS_CSWpm-xml-sax-expat += CSWpm-xml-parser

EXTRA_CONFIGURE_EXPORTS += SKIP_SAX_INSTALL
CONFIGURE_ENV_SKIP_SAX_INSTALL = 1

include gar/category.mk
