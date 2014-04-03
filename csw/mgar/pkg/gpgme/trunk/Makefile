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
BUILD_DEP_PKGS += CSWlibassuan-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWgnupg2

OBSOLETED_BY_CSWlibgpgme11 = CSWgpgme
OBSOLETED_BY_CSWlibgpgme-pthread11 = CSWgpgme

PACKAGES += CSWlibgpgme-pthread11
CATALOGNAME_CSWlibgpgme-pthread11 = libgpgme_pthread11
PKGFILES_CSWlibgpgme-pthread11 += $(call baseisadirs,$(libdir),libgpgme-pthread\.so\.11\.11\.0)
PKGFILES_CSWlibgpgme-pthread11 += $(call baseisadirs,$(libdir),libgpgme-pthread\.so\.11(\.\d+)*)
SPKG_DESC_CSWlibgpgme-pthread11 += $(DESCRIPTION), libgpgme-pthread.so.11
RUNTIME_DEP_PKGS_CSWlibgpgme-pthread11 += CSWlibassuan0
RUNTIME_DEP_PKGS_CSWlibgpgme-pthread11 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgpgme-pthread11 += CSWlibgcc-s1

PACKAGES += CSWlibgpgme11
CATALOGNAME_CSWlibgpgme11 = libgpgme11
PKGFILES_CSWlibgpgme11 += $(call baseisadirs,$(libdir),libgpgme\.so\.11\.11\.0)
PKGFILES_CSWlibgpgme11 += $(call baseisadirs,$(libdir),libgpgme\.so\.11(\.\d+)*)
SPKG_DESC_CSWlibgpgme11 += $(DESCRIPTION), libgpgme.so.11
RUNTIME_DEP_PKGS_CSWlibgpgme11 += CSWlibassuan0
RUNTIME_DEP_PKGS_CSWlibgpgme11 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgpgme11 += CSWlibgcc-s1

PACKAGES += CSWgpgme-dev
CATALOGNAME_CSWgpgme-dev = gpgme_dev
SPKG_DESC_CSWgpgme-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWgpgme-dev += CSWlibgpgme11
RUNTIME_DEP_PKGS_CSWgpgme-dev += CSWlibgpgme-pthread11

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gpg-version=2
CONFIGURE_ARGS += --with-gpgsm-version=2
CONFIGURE_ARGS += --with-gpgconf-version=2
CONFIGURE_ARGS += --with-gpgconf=$(prefix)/bin
CONFIGURE_ARGS += --with-gpg=$(prefix)/bin
CONFIGURE_ARGS += --with-gpgsm=$(prefix)/bin

include gar/category.mk
