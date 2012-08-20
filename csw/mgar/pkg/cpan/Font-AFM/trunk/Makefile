NAME = Font-AFM
VERSION = 1.20
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GAAS

DESCRIPTION = Interface to Adobe Font Metrics files
define BLURB
  This module implements the Font::AFM class. Objects of this class are
  initialised from an AFM-file and allows you to obtain information about the
  font and the metrics of the various glyphs in the font.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-font-afm
CATALOGNAME = pm_font_afm
SPKG_DESC_CSWpm-font-afm = $(DESCRIPTION)

# Name change
OBSOLETED_BY_CSWpm-font-afm = CSWpmfontafm
CATALOGNAME_CSWpmfontafm = pm_fontafm_stub

ARCHALL = 1

PATCHFILES += 0001-add-csw-font-paths.patch

# Harmless
CHECKPKG_OVERRIDES_CSWpm-font-afm += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Font/AFM.pm
CHECKPKG_OVERRIDES_CSWpm-font-afm += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Font::AFM.3perl

include gar/category.mk
