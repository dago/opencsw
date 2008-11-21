GARNAME = Crypt-OpenSSL-RSA
GARVERSION = 0.24
CATEGORIES = cpan
AUTHOR = IROBERTS

DESCRIPTION = RSA encoding and decoding, using the openSSL libraries
define BLURB
  Crypt::OpenSSL::RSA provides the ability to RSA encrypt strings which are
  somewhat shorter than the block size of a key. It also allows for
  decryption, signatures and signature verification.
endef

DISTFILES += CSWpmcryptosslrsa.gspec CSWpmcryptosslrsa.depend

DEPENDS += lib/openssl
DEPENDS += cpan/Crypt-OpenSSL-Random

include ../category.mk
