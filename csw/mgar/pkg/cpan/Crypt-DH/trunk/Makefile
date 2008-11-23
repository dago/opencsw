GARNAME = Crypt-DH
GARVERSION = 0.06
CATEGORIES = cpan
AUTHOR = BTROTT

DESCRIPTION = Diffie-Hellman key exchange system
define BLURB
  Crypt::DH is a Perl implementation of the Diffie-Hellman key exchange
  system.  Diffie-Hellman is an algorithm by which two parties can agree on a
  shared secret key, known only to them. The secret is negotiated over an
  insecure network without the two parties ever passing the actual shared
  secret, or their private keys, between them.
endef

DISTFILES += CSWpmcryptdh.gspec CSWpmcryptdh.depend

DEPENDS += cpan/Math-Pari cpan/Crypt-Random

include gar/category.mk
