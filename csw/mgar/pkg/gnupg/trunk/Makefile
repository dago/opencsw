NAME = gnupg
VERSION = 1.4.12
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = GnuPG is a complete and free replacement for PGP
define BLURB
  RFC 2440 compliant tool for secure communication and data storage
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://www.gnupg.org/

PACKAGES += CSWgnupg
SPKG_DESC_CSWgnupg = GnuPG is a complete and free replacement for PGP
RUNTIME_DEP_PKGS_CSWgnupg += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWgnupg += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWgnupg += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnupg += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnupg += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgnupg += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnupg += CSWoldaprt

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl=$(prefix)
CONFIGURE_ARGS += --with-ldap=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-bzip2=$(prefix)
CONFIGURE_ARGS += --with-tar=$(prefix)
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-libintl-prefix=$(prefix)
CONFIGURE_ARGS += --with-included-regex
CONFIGURE_ARGS += --enable-threads=solaris
CONFIGURE_ARGS += --disable-asm

EXTRA_MERGE_EXCLUDE_FILES += .*/charset.alias
# Collision with gnupg2
EXTRA_MERGE_EXCLUDE_FILES += .*/gpg-zip.1

PROTOTYPE_MODIFIERS  = suid
PROTOTYPE_FILES_suid = .*/gpg
PROTOTYPE_PERMS_suid = 4755

CHECKPKG_OVERRIDES_CSWgnupg += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/gpg.ru.1
CHECKPKG_OVERRIDES_CSWgnupg += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/gpg.1
CHECKPKG_OVERRIDES_CSWgnupg += file-with-bad-content|/usr/local|root/opt/csw/share/info/gnupg1.info

include gar/category.mk
