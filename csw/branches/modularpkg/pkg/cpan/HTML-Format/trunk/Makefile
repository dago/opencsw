GARNAME = HTML-Format
GARVERSION = 2.04
CATEGORIES = cpan
AUTHOR = SBURKE

DESCRIPTION = format HTML as plaintext
define BLURB
  The HTML::FormatText is a formatter that outputs plain latin1 text. All
  character attributes (bold/italic/underline) are ignored. Formatting of HTML
  tables and forms is not implemented.
endef

DISTFILES = $(call admfiles,CSWpmhtmlfmt,depend prototype)

DEPENDS += cpan/Font-AFM

include gar/category.mk
