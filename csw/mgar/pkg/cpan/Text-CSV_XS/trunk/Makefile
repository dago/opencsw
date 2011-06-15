NAME = Text-CSV_XS
VERSION = 0.81
CATEGORIES = cpan
AUTHOR = HMBRAND

DESCRIPTION = Comma-separated values manipulation routines
define BLURB
  Text::CSV_XS provides facilities for the composition and decomposition of
  comma-separated values. An instance of the Text::CSV_XS class can combine
  fields into a CSV string and parse a CSV string into fields.
endef

# This module uses .tgz instead of .tar.gz :-(
MODDIST = $(NAME)-$(VERSION).tgz

PACKAGES = CSWpm-text-csv-xs
CATALOGNAME = pm_text_csv_xs
SPKG_DESC_CSWpm-text-csv-xs = Comma-separated values manipulation routines
OBSOLETED_BY_CSWpm-text-csv-xs = CSWpmtextcsvxs
RUNTIME_DEP_PKGS_CSWpm-text-csv-xs = CSWpm-text-csv

# This was the previous name. Note the typo!
INCOMPATIBLE_PKGS = CSWpmttextcsvxs


include gar/category.mk
