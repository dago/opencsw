NAME = Unicode-Map
VERSION = 0.112
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MSCHWARTZ

DESCRIPTION = Maps charsets from and to utf16 unicode
define BLURB
  This module converts strings from and to 2-byte Unicode UCS2 format. All
  mappings happen via 2 byte UTF16 encodings, not via 1 byte UTF8 encoding. To
  transform these use Unicode::String.
endef

PACKAGES = CSWpmunicodemap
CATALOGNAME = pm_unicodemap

# This is needed for mirrorMappings:
#   http://www.opencsw.org/mantis/view.php?id=2710
RUNTIME_DEP_PKGS = CSWpmlibwww

include gar/category.mk
