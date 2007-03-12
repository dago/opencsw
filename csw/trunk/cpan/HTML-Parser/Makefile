GARNAME = HTML-Parser
GARVERSION = 3.56
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = HTML parser class
define BLURB
  Objects of the HTML::Parser class will recognize markup and separate it from
  plain text (alias data content) in HTML documents. As different kinds of
  markup and text are recognized, the corresponding event handlers are
  invoked.
endef

DISTFILES = $(call admfiles,CSWpmhtmlparser,depend prototype)

DEPENDS += cpan/HTML-Tagset

CONFIGURE_ARGS = -n

include ../category.mk
