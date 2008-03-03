GARNAME = PodToHTML
GARVERSION = 0.05
CATEGORIES = cpan
AUTHOR = NI-S

DESCRIPTION = Convert POD to trees of HTML::Element
define BLURB
  Pod::HTML_Elements is subclass of Pod::Parser. As the pod is parsed a tree
  of HTML::Element objects is built to represent HTML for the pod.
endef

DISTFILES = $(call admfiles,CSWpmpodtohtml,depend prototype)

DEPENDS += cpan/HTML-Format cpan/HTML-Parser cpan/HTML-Tree

include gar/category.mk
