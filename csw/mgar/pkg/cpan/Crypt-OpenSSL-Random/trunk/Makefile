NAME = Crypt-OpenSSL-Random
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = IROBERTS

DESCRIPTION = Perl Crypt::OpenSSL::Random module
define BLURB
  Crypt::OpenSSL::Random provides the ability to seed and query the OpenSSL
  library's pseudo-random number generator
endef

LICENSE = LICENSE

PACKAGES = CSWpm-crypt-openssl-random
CATALOGNAME = pm_crypt_openssl_random
SPKG_DESC_CSWpm-crypt-openssl-random = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-crypt-openssl-random = CSWpmcryptosslrandom
CATALOGNAME_CSWpmcryptosslrandom = pm_osslrandom_stub

RUNTIME_DEP_PKGS_CSWpm-crypt-openssl-random += CSWlibssl1-0-0

include gar/category.mk
