GARNAME = Crypt-RSA
GARVERSION = 1.58
CATEGORIES = cpan
AUTHOR = VIPUL

DESCRIPTION = RSA public-key cryptosystem.
define BLURB
  Crypt::RSA is a pure-perl, cleanroom implementation of the RSA public-key
  cryptosystem. It uses Math::Pari(3), a perl interface to the blazingly fast
  PARI library, for big integer arithmetic and number theoretic computations.
endef

DISTFILES += CSWpmcryptrsa.gspec CSWpmcryptrsa.depend

DEPENDS += cpan/Crypt-Primes cpan/Tie-EncryptedHash
DEPENDS += cpan/Convert-ASCII-Armour cpan/Sort-Versions
DEPENDS += cpan/Digest-SHA1 cpan/Digest-MD2
DEPENDS += cpan/Data-Buffer

include ../category.mk
