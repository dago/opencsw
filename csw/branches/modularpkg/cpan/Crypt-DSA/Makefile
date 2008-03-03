GARNAME = Crypt-DSA
GARVERSION = 0.14
CATEGORIES = cpan
AUTHOR = BTROTT

DESCRIPTION = DSA signatures and key generation
define BLURB
  Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
  signature verification system. The implementation itself is pure Perl,
  although the heavy-duty mathematics underneath are provided by the
  Math::Pari library.
endef

DISTFILES += CSWpmcryptdsa.gspec CSWpmcryptdsa.depend

DEPENDS += cpan/Crypt-Random cpan/Digest-SHA1
DEPENDS += cpan/Convert-PEM cpan/Data-Buffer

include ../category.mk
