NAME = URI
VERSION = 1.59
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GAAS

DESCRIPTION =  Uniform Resource Identifiers (absolute and relative)
define BLURB
  This module implements the URI class. Objects of this class represent
  "Uniform Resource Identifier references" as specified in RFC 2396 (and
  updated by RFC 2732).
endef

DISTFILES += COPYING

PACKAGES               = CSWpm-uri
SPKG_DESC_CSWpm-uri    = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-uri = CSWpmuri
CATALOGNAME_CSWpmuri   = pm_uri_stub

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-mime-base64

include gar/category.mk
