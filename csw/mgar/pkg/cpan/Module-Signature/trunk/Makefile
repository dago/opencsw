NAME = Module-Signature
VERSION = 0.63
CATEGORIES = cpan
AUTHOR = FLORA

DESCRIPTION = Module signature file manipulation
define BLURB
  Module::Signature adds cryptographic authentications to CPAN distributions,
  via the special SIGNATURE file.
endef

DISTFILES += COPYING

PACKAGES = CSWpmmodulesign
CATALOGNAME = pm_modulesign
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWgnupg
RUNTIME_DEP_PKGS += CSWpmpardist
RUNTIME_DEP_PKGS += CSWpmtextdiff

CHECKPKG_OVERRIDES_CSWpmmodulesign += surplus-dependency|CSWpmpardist
CHECKPKG_OVERRIDES_CSWpmmodulesign += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWpmmodulesign += surplus-dependency|CSWpmtextdiff

include gar/category.mk
