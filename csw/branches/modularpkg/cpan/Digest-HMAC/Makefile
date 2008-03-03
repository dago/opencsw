GARNAME = Digest-HMAC
GARVERSION = 1.01
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = keyed-hashing for message authentication
define BLURB
  HMAC is used for message integrity checks between two parties that share a
  secret key, and works in combination with some other Digest algorithm,
  usually MD5 or SHA-1. The HMAC mechanism is described in RFC 2104.
endef

DISTFILES += CSWpmdigesthmac.gspec CSWpmdigesthmac.depend

DEPENDS += cpan/Digest-SHA1

include ../category.mk
