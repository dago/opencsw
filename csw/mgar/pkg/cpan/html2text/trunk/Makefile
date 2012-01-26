NAME = html2text
VERSION = 0.003
CATEGORIES = cpan
GARTYPE = v2
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

post-extract-modulated:
	-perl -pi -e 's,^#!.*,#!/opt/csw/bin/perl -w,' $(WORKSRC)/html2text.pl
	@$(MAKECOOKIE)
