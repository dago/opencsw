GARNAME = MIME-Base64
GARVERSION = 3.07
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = Encoding and decoding of base64 strings
define BLURB
  Encoding and decoding of base64 strings
endef

DISTFILES += COPYING

CATALOGNAME = pm_mimebase64
PACKAGES = CSWpmmimebase64

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod .*\/man\/.*

CONFIGURE_ARGS = 

include gar/category.mk
