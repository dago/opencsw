NAME = HTML-Format
VERSION = 2.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SBURKE

DESCRIPTION = Format HTML as plaintext
define BLURB
  The HTML::FormatText is a formatter that outputs plain latin1 text. All
  character attributes (bold/italic/underline) are ignored. Formatting of HTML
  tables and forms is not implemented.
endef

DISTFILES = COPYING

PACKAGES = CSWpmhtmlformat
CATALOGNAME_CSWpmhtmlformat = pm_htmlformat

# Legacy package
PACKAGES += CSWpmhtmlfmt
CATALOGNAME_CSWpmhtmlfmt = pm_htmlfmt

SPKG_DESC_CSWpmhtmlformat = $(DESCRIPTION)
SPKG_DESC_CSWpmhtmlfmt = Deprecated, empty stub to CSWpmhtmlformat

DEP_PKGS_CSWpmhtmlformat = CSWpmfontafm CSWpmhtmltree
RUNTIME_DEP_PKGS_CSWpmhtmlfmt = CSWpmhtmlformat

ARCHALL = 1

PKGFILES_CSWpmhtmlfmt = NOFILES

include gar/category.mk
