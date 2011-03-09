NAME = GSSAPI
VERSION = 0.28
CATEGORIES = cpan
AUTHOR = AGROLMS

DESCRIPTION = Providing access to the GSSAPIv2 library
define BLURB
  Providing access to the GSSAPIv2 library.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-gssapi
CATALOGNAME = pm_gssapi
SPKG_DESC_CSWpm-gssapi = $(DESCRIPTION)
OBSOLETES_CSWpm-gssapi = CSWpmgssapi
CATALOGNAME_CSWpmgssapi = pm_gssapi_stub

RUNTIME_DEP_PKGS = CSWkrb5lib

# Dago: "You can safely override it and make a comment
#       that after krb5-config fixing it should go away"
CHECKPKG_OVERRIDES_CSWpm-gssapi += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/perl/csw/auto/GSSAPI/GSSAPI.so

include gar/category.mk
