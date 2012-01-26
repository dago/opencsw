NAME = HTML-Tree
VERSION = 4.1
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PETEK

DESCRIPTION = Modules for making parse trees from HTML source
define BLURB
  HTML-Tree is a suite of Perl modules for making parse trees out of HTML
  source.  It consists of mainly two modules, whose documentation you should
  refer to: HTML::TreeBuilder and HTML::Element.
endef

DISTFILES = COPYING

PACKAGES = CSWpmhtmltree
CATALOGNAME = pm_htmltree

RUNTIME_DEP_PKGS_CSWpmhtmltree += CSWpmhtmlparser
RUNTIME_DEP_PKGS_CSWpmhtmltree += CSWpmhtmltagset

ARCHALL = 1

include gar/category.mk
