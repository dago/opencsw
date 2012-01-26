NAME = HTML-TableExtract
VERSION = 2.10
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MSISK

DESCRIPTION = module for extracting the contents of tables within an HTML document.
define BLURB
  HTML::TableExtract is a subclass of HTML::Parser that serves to extract the 
  information from tables of interest contained within an HTML document. The 
  information from each extracted table is stored in table objects. Tables 
  can be extracted as text, HTML, or HTML::ElementTable structures (for 
  in-place editing or manipulation).
endef

PACKAGES = CSWpmhtmltableextract
CATALOGNAME = pm_htmltableextract

DEPENDS += cpan/HTML-Parser cpan/HTML-Tagset cpan/HTML-Element-Extended cpan/HTML-Tree cpan/Test-Exception cpan/Sub-Uplevel

ARCHALL = 1

LICENSE = files/COPYING

include gar/category.mk
