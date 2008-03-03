GARNAME = XML-SAX
GARVERSION = 0.14
CATEGORIES = cpan
AUTHOR = MSERGEANT

DESCRIPTION = Simple API for XML
define BLURB
  XML::SAX is a SAX parser access API for Perl. It includes classes and APIs
  required for implementing SAX drivers, along with a factory class for
  returning any SAX parser installed on the user's system.
endef

DISTFILES += $(call admfiles,CSWpmxmlsax,depend prototype)

DEPENDS += cpan/XML-NamespaceSupport

# Enable modification of ParserDetails.ini
PATCHFILES = parser.diff

include ../category.mk
