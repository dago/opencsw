NAME = XML-LibXSLT
VERSION = 1.80
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHLOMIF

DESCRIPTION = interface to the gnome libxslt library
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-xml-libxslt
CATALOGNAME = pm_xml_libxslt
SPKG_DESC_CSWpm-xml-libxslt = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-xml-libxslt = CSWpmxmllibxslt
CATALOGNAME_CSWpmxmllibxslt = pm_xmllibxslt

RUNTIME_DEP_PKGS_CSWpm-xml-libxslt += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWpm-xml-libxslt += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpm-xml-libxslt += CSWlibexslt0
RUNTIME_DEP_PKGS += CSWpm-xml-libxml

SKIPTEST = 1

CHECKPKG_OVERRIDES_CSWpm-xml-libxslt += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/auto/XML/LibXSLT/LibXSLT.so

include gar/category.mk
