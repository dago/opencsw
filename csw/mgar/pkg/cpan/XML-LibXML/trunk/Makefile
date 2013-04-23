NAME = XML-LibXML
VERSION = 2.0016
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHLOMIF

DESCRIPTION = Interface to Gnome libxml2 xml parsing and DOM library
define BLURB
endef

DISTFILES += CSWpm-xml-libxml.postinstall
DISTFILES += CSWpm-xml-libxml.preremove

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-devel-checklib

PACKAGES += CSWpm-xml-libxml
CATALOGNAME_CSWpm-xml-libxml = pm_xml_libxml
SPKG_DESC_CSWpm-xml-libxml = Interface to Gnome libxml2 xml parsing and DOM library
RUNTIME_DEP_PKGS_CSWpm-xml-libxml += CSWpm-xml-sax
RUNTIME_DEP_PKGS_CSWpm-xml-libxml += CSWpm-xml-namespacesupport
RUNTIME_DEP_PKGS_CSWpm-xml-libxml += CSWlibxml2-2
OBSOLETED_BY_CSWpm-xml-libxml += CSWpmxmllibxml
CATALOGNAME_CSWpmxmllibxml = pm_xmllibxml_stub

CONFIGURE_ENV += SKIP_SAX_INSTALL=1
CONFIGURE_ENV += XMLPREFIX="$(prefix)"
CONFIGURE_ENV += LD_OPTIONS="$(LD_OPTIONS)"

# This crappy check_lib bails out on -R
CONFIGURE_ARGS += LIBS="$(filter-out -R%,$(shell $(bindir)/xml2-config --libs))"
CONFIGURE_ARGS += INC="$(shell $(bindir)/xml2-config --cflags)"

include gar/category.mk
