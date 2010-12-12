NAME    = gnupg
VERSION = 1.4.11
CATEGORIES = apps

DESCRIPTION = GnuPG is a complete and free replacement for PGP.
define BLURB
    RFC 2440 compliant tool for secure communication and data storage
endef

PACKAGES    = CSWgnupg
CATALOGNAME = gnupg
SPKG_DESC   = GnuPG is a complete and free replacement for PGP.

SPKG_SOURCEURL = http://www.gnupg.org/
MASTER_SITES   = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES      = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

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

PROTOTYPE_MODIFIERS = suid
PROTOTYPE_FILES_suid = .*/gpg
PROTOTYPE_PERMS_suid = 4755

RUNTIME_DEP_PKGS_CSWgnupg  = CSWbzip2 CSWcurlrt CSWggettextrt CSWiconv
RUNTIME_DEP_PKGS_CSWgnupg += CSWoldaprt CSWreadline CSWzlib

TEST_TARGET = check

include gar/category.mk
