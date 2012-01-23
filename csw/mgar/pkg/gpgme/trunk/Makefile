NAME = gpgme
VERSION = 1.1.8
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgpgme,)

SPKG_SOURCEURL = http://www.gnupg.org/related_software/libraries.en.html#lib-GPGME

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWgpgerr CSWpth

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
