NAME = HTML-Parser
VERSION = 3.64
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = HTML parser class
define BLURB
  Objects of the HTML::Parser class will recognize markup and separate it from
  plain text (alias data content) in HTML documents. As different kinds of
  markup and text are recognized, the corresponding event handlers are
  invoked.
endef

DISTFILES += COPYING

PACKAGES = CSWpmhtmlparser
CATALOGNAME = pm_htmlparser

RUNTIME_DEP_PKGS = CSWpmhtmltagset

CONFIGURE_ARGS = -n

include gar/category.mk
