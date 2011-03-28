NAME = Module-Signature
VERSION = 0.66
CATEGORIES = cpan
AUTHOR = FLORA

DESCRIPTION = Module signature file manipulation
define BLURB
  Module::Signature adds cryptographic authentications to CPAN distributions,
  via the special SIGNATURE file.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-module-signature
CATALOGNAME = pm_module_signature
SPKG_DESC_CSWpm-module-signature = $(DESCRIPTION)
ARCHALL = 1
OBSOLETED_BY_CSWpm-module-signature = CSWpmmodulesign
CATALOGNAME_CSWpmmodulesign = pm_modulesign

RUNTIME_DEP_PKGS += CSWgnupg
RUNTIME_DEP_PKGS += CSWpmpardist
RUNTIME_DEP_PKGS += CSWpmtextdiff

include gar/category.mk
