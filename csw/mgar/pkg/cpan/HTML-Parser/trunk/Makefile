GARNAME = HTML-Parser
GARVERSION = 3.61
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = HTML parser class
define BLURB
  Objects of the HTML::Parser class will recognize markup and separate it from
  plain text (alias data content) in HTML documents. As different kinds of
  markup and text are recognized, the corresponding event handlers are
  invoked.
endef

DISTFILES = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpmhtmlparser
CATALOGNAME = pm_htmlparser

REQUIRED_PKGS = CSWpmhtmltagset

CONFIGURE_ARGS = -n

include gar/category.mk
