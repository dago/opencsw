NAME = GSSAPI
VERSION = 0.28
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = AGROLMS

DESCRIPTION = Providing access to the GSSAPIv2 library
define BLURB
endef

PACKAGES = CSWpm-gssapi
CATALOGNAME = pm_gssapi
SPKG_DESC_CSWpm-gssapi = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWpm-gssapi += CSWlibkrb5-3

CHECKPKG_OVERRIDES_CSWpm-gssapi += missing-dependency|CSWlibintl8

include gar/category.mk
