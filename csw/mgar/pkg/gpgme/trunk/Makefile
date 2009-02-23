GARNAME = gpgme
GARVERSION = 1.1.8
CATEGORIES = apps

DESCRIPTION = GPGME - GnuPG Made Easy
define BLURB
  GPGME (GnuPG Made Easy) is a C language library that allows to add support
  for cryptography to a program. It is designed to make access to public key
  crypto engines like GnuPG or GpgSM easier for applications. GPGME provides
  a high-level crypto API for encryption, decryption, signing, signature
  verification and key management.
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gpgme/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgpgme,)

SPKG_SOURCEURL = http://www.gnupg.org/related_software/libraries.en.html#lib-GPGME

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWgpgerr CSWpth

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
