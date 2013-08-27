NAME = gpgme
VERSION = 1.4.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = GPGME - GnuPG Made Easy
define BLURB
  GPGME (GnuPG Made Easy) is a C language library that allows to add support
  for cryptography to a program. It is designed to make access to public key
  crypto engines like GnuPG or GpgSM easier for applications. GPGME provides
  a high-level crypto API for encryption, decryption, signing, signature
  verification and key management.
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gpgme/
DISTFILES  = $(NAME)-$mfiles,CSWgpgme,)

SPKG_SOURCEURL = http://www.gnupg.org/related_software/libraries.eGARCOMPILER = GCC4

PATCHFILES += 0001_need_posix_shell.patch

BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibpth-dev
BUILD_DEP_PKGS += CSWgnupg2

RUNTIME_DEP_PKGS = CSWgpgerr CSWpth

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gpg-version=2
CONFIGURE_ARGS += --with-gpgsm-version=2
CONFIGURE_ARGS += --with-gpgconf-version=2
CONFIGURE_ARGS += --with-gpgconf=$(prefix)/bin
CONFIGURE_ARGS += --with-gpg=$(prefix)/bin
CONFIGURE_ARGS += --with-gpgsm=$(prefix)/bin

include gar/category.mk
