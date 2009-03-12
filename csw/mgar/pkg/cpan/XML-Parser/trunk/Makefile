GARNAME = XML-Parser
GARVERSION = 2.36
CATEGORIES = cpan
AUTHOR = MSERGEANT

DESCRIPTION = a module for parsing XML documents
define BLURB
  This module provides ways to parse XML documents. It is built on top of
  XML::Parser::Expat, which is a lower level interface to James Clarks expat
  library. Each call to one of the parsing methods creates a new instance of
  XML::Parser::Expat which is then used to parse the document. Expat options
  may be provided when the XML::Parser object is created. These options are
  then passed on to the Expat object on each parse call. They can also be
  given as extra arguments to the parse methods, in which case they override
  options given at XML::Parser creation time.
endef


DISTFILES = $(call admfiles,CSWpmxmlparser,)

REQUIRED_PKGS += CSWexpat

DEPENDS += lib/expat

CONFIGURE_ARGS  = EXPATINCPATH=$(includedir)
CONFIGURE_ARGS += EXPATLIBPATH=$(libdir)

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
