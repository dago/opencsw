GARNAME = XML-LibXML
GARVERSION = 1.70
CATEGORIES = cpan
AUTHOR = PAJAS

DESCRIPTION = binding for libxml2
define BLURB
  This module is an interface to the gnome libxml2 DOM and SAX parser and the
  DOM tree. It also provides an XML::XPath-like findnodes() interface,
  providing access to the XPath API in libxml2. The module is split into
  several packages which are not described in this section.
endef

PACKAGES  = CSWpmxmllibxml CSWpmxmllibxmlcom
CATALOGNAME_CSWpmxmllibxml = pm_xmllibxml
SPKG_DESC_CSWpmxmllibxml = Binding for libxml2
# PKGFILES_CSWpmxmllibxml = 
CATALOGNAME_CSWpmxmllibxmlcom = pm_xmllibxmlcom
SPKG_DESC_CSWpmxmllibxmlcom = Constants and Character Encoding Routines
PKGFILES_CSWpmxmllibxmlcom = this-is-just-an-empty-stub

PREREQUISITE_PKGS = CSWpmxmlnssupp CSWpmxmlsax CSWlibxml2
REQUIRED_PKGS = CSWpmxmlnssupp CSWpmxmlsax CSWlibxml2

CONFIGURE_ENV += SKIP_SAX_INSTALL=1

include gar/category.mk
