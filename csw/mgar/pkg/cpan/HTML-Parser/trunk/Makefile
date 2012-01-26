NAME = HTML-Parser
VERSION = 3.68
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GAAS

DESCRIPTION = HTML parser class
define BLURB
  Objects of the HTML::Parser class will recognize markup and separate it from
  plain text (alias data content) in HTML documents. As different kinds of
  markup and text are recognized, the corresponding event handlers are
  invoked.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-html-parser
CATALOGNAME = pm_html_parser
SPKG_DESC_CSWpm-html-parser = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-html-parser = CSWpmhtmlparser
CATALOGNAME_CSWpmhtmlparser = pm_htmlparser

RUNTIME_DEP_PKGS = CSWpm-html-tagset

CHECKPKG_OVERRIDES_CSWpm-html-parser += unidentified-dependency|CSWpm-html-tagset

CONFIGURE_ARGS = -n

include gar/category.mk
