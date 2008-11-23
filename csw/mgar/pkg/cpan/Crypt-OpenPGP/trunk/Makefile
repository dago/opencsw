GARNAME = Crypt-OpenPGP
GARVERSION = 1.03
CATEGORIES = cpan
AUTHOR = BTROTT

DESCRIPTION = pure-Perl OpenPGP implementation
define BLURB
  Crypt::OpenPGP is a pure-Perl implementation of the OpenPGP standard[1]. In
  addition to support for the standard itself, Crypt::OpenPGP claims
  compatibility with many other PGP implementations, both those that support
  the standard and those that preceded it.
endef

DISTFILES += CSWpmcryptopenpgp.gspec CSWpmcryptopenpgp.depend

DEPENDS += cpan/libwww-perl
DEPENDS += cpan/Crypt-IDEA
DEPENDS += cpan/Crypt-Rijndael
DEPENDS += cpan/Crypt-CAST5_PP
DEPENDS += cpan/Crypt-Twofish
DEPENDS += cpan/Crypt-RIPEMD160
DEPENDS += cpan/Crypt-RSA
DEPENDS += cpan/Crypt-DSA

CONFIGURE_ARGS = --defaultdeps

include gar/category.mk
