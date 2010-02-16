GARNAME = html2text
GARVERSION = 0.003
CATEGORIES = cpan
AUTHOR = AWRIGLEY

DESCRIPTION = Script for generating formatted text from HTML
define BLURB
  html2text.pl generates simple formatted text from HTML. It uses
  HTML::Element to traverse an HTML tree built by HTML::TreeBuilder, and formats
  the output text using Text::Format. It is _very_ simple at the moment.
endef

DISTFILES = COPYING

PACKAGES = CSWpmhtml2text
CATALOGNAME = pm_html2text

DEP_PKGS = CSWpmtextformat CSWpmhtmltree

ARCHALL = 1

include gar/category.mk
