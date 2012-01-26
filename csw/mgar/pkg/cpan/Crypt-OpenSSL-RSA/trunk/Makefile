NAME = Crypt-OpenSSL-RSA
VERSION = 0.25
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = IROBERTS

DESCRIPTION = RSA encoding and decoding, using the openSSL libraries
define BLURB
  Crypt::OpenSSL::RSA provides the ability to RSA encrypt strings which are
  somewhat shorter than the block size of a key. It also allows for
  decryption, signatures and signature verification.
endef

PACKAGES = CSWpmcryptosslrsa
CATALOGNAME = pm_osslrsa

RUNTIME_DEP_PKGS = CSWpmcryptosslrandom
BUILD_DEP_PKGS = CSWpmcryptosslrandom

include gar/category.mk
