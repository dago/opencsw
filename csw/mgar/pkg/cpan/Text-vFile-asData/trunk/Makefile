NAME = Text-vFile-asData
VERSION = 0.07
CATEGORIES = cpan
AUTHOR = RCLAMP

DESCRIPTION = Parse vFile formatted files into data structures
define BLURB
  Parse vFile formatted files into data structures
endef

DISTFILES += COPYING

PACKAGES = CSWpm-text-vfile-asdata
CATALOGNAME = pm_text_vfile_asdata
SPKG_DESC_CSWpm-text-vfile-asdata = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-text-vfile-asdata = CSWpmtextvfileasdata
CATALOGNAME_CSWpmtextvfileasdata = pm_textvfileasdata

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-class-accessor-chained

CHECKPKG_OVERRIDES_CSWpm-text-vfile-asdata += unidentified-dependency|CSWpm-class-accessor-chained

include gar/category.mk
