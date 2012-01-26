NAME = XML-LibXML
VERSION = 1.70
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PAJAS

DESCRIPTION = binding for libxml2
define BLURB
  This module is an interface to the gnome libxml2 DOM and SAX parser and the
  DOM tree. It also provides an XML::XPath-like findnodes() interface,
  providing access to the XPath API in libxml2. The module is split into
  several packages which are not described in this section.
endef

DISTFILES += CSWpmxmllibxml.postinstall

PACKAGES  = CSWpmxmllibxml CSWpmxmllibxmlcom
CATALOGNAME_CSWpmxmllibxml = pm_xmllibxml
SPKG_DESC_CSWpmxmllibxml = Binding for libxml2
CATALOGNAME_CSWpmxmllibxmlcom = pm_xmllibxmlcom
SPKG_DESC_CSWpmxmllibxmlcom = Constants and Character Encoding Routines
PKGFILES_CSWpmxmllibxmlcom = this-is-just-an-empty-stub
ARCHALL_CSWpmxmllibxmlcom = 1

RUNTIME_DEP_PKGS_CSWpmxmllibxml += CSWiconv 
RUNTIME_DEP_PKGS_CSWpmxmllibxml += CSWzlib 
RUNTIME_DEP_PKGS_CSWpmxmllibxml += CSWpmxmlnssupp 
RUNTIME_DEP_PKGS_CSWpmxmllibxml += CSWpmxmlsax 
RUNTIME_DEP_PKGS_CSWpmxmllibxml += CSWlibxml2 
RUNTIME_DEP_PKGS_CSWpmxmllibxml += CSWlibxml2devel
BUILD_DEP_PKGS_CSWpmxmllibxml = $(RUNTIME_DEP_PKGS_CSWpmxmllibxml)
RUNTIME_DEP_PKGS_CSWpmxmllibxmlcom = CSWpmxmllibxml

CONFIGURE_ENV += SKIP_SAX_INSTALL=1

include gar/category.mk
