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

PACKAGES = CSWpmfontafm
CATALOGNAME = pm_fontafm
ARCHALL = 1

PATCHFILES += 0001-add-csw-font-paths.patch

include gar/category.mk
