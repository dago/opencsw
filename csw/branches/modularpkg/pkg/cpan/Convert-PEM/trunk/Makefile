GARNAME = Convert-PEM
GARVERSION = 0.07
CATEGORIES = cpan
AUTHOR = BTROTT

DESCRIPTION = read/write encrypted ASN.1 PEM files
define BLURB
  Convert::PEM reads and writes PEM files containing ASN.1-encoded objects.
  The files can optionally be encrypted using a symmetric cipher algorithm,
  such as 3DES.
endef

DISTFILES += CSWpmconvertpem.gspec CSWpmconvertpem.depend

DEPENDS += cpan/Convert-ASN1 cpan/Crypt-DES_EDE3

include gar/category.mk
