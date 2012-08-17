NAME = Text-Template
VERSION = 1.45
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MJD

DESCRIPTION = Expand template text with embedded Perl
define BLURB
  This is a library for generating form letters, building HTML pages, or
  filling in templates generally. A `template' is a piece of text that has
  little Perl programs embedded in it here and there. When you `fill in' a
  template, you evaluate the little programs and replace them with their
  values.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
PACKAGES = CSWpm-text-template
CATALOGNAME = pm_text_template
ARCHALL = 1

# name change handling
SPKG_DESC_CSWpm-text-template = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-text-template = CSWpmtexttemplate
CATALOGNAME_CSWpmtexttemplate = pm_texttemplate_stub

include gar/category.mk
