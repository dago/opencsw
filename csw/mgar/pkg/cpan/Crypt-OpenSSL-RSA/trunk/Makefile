NAME = Crypt-OpenSSL-RSA
VERSION = 0.28
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PERLER

DESCRIPTION = RSA encoding and decoding, using the openSSL libraries
define BLURB
  Crypt::OpenSSL::RSA provides the ability to RSA encrypt strings which are
  somewhat shorter than the block size of a key. It also allows for
  decryption, signatures and signature verification.
endef

LICENSE = LICENSE

PACKAGES = CSWpm-crypt-openssl-rsa
CATALOGNAME = pm_crypt_openssl_rsa
SPKG_DESC_CSWpm-crypt-openssl-rsa = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-crypt-openssl-rsa = CSWpmcryptosslrsa
CATALOGNAME_CSWpmcryptosslrsa = pm_osslrsa_stub

RUNTIME_DEP_PKGS_CSWpm-crypt-openssl-rsa  = CSWpm-crypt-openssl-random
RUNTIME_DEP_PKGS_CSWpm-crypt-openssl-rsa += CSWlibssl1-0-0

# Will be released at same time as this package, remove this override next time
CHECKPKG_OVERRIDES_CSWpm-crypt-openssl-rsa += unidentified-dependency|CSWpm-crypt-openssl-random

include gar/category.mk
