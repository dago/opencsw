NAME = XML-SAX-Writer
VERSION = 0.53
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = PERIGRIN

DESCRIPTION = SAX2 Writer
define BLURB
  SAX2 Writer
endef

DISTFILES += COPYING

PACKAGES = CSWpm-xml-sax-writer
CATALOGNAME = pm_xml_sax_writer
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-xml-sax-base
RUNTIME_DEP_PKGS += CSWpm-xml-namespacesupport
RUNTIME_DEP_PKGS += CSWpm-xml-filter-buffertext

CONFIGURE_ARGS = 

CHECKPKG_OVERRIDES_CSWpm-xml-sax-writer += unidentified-dependency|CSWpm-xml-filter-buffertext

include gar/category.mk
