GARNAME    = gnupg
GARVERSION = 1.4.9
CATEGORIES = apps

DESCRIPTION = GnuPG without keyserver access and optional algorithms, except RSA (enable-minimal configure)
define BLURB
    RFC 2440 compliant tool for secure communication and data storage
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = (\d+(?:\.\d+)*)

PACKAGES = CSWgnupgminimal
CATALOGNAME_CSWgnupgminimal = gnupg_minimal
SPKG_DESC_CSWgnupgminimal = $(DESCRIPTION)
#PKGFILES_CSWgnupgminimal = .*/bin/.*
REQUIRED_PKGS_CSWgnupgminimal = CSWbzip2 CSWcurlrt CSWggettextrt CSWiconv
REQUIRED_PKGS_CSWgnupgminimal += CSWoldaprt CSWreadline CSWzlib

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-suffix=-minimal
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
CONFIGURE_ARGS += --enable-shared=no
CONFIGURE_ARGS += --disable-asm
CONFIGURE_ARGS += --disable-gnupg-iconv
CONFIGURE_ARGS += --disable-card-support
CONFIGURE_ARGS += --disable-agent-support
CONFIGURE_ARGS += --disable-idea
CONFIGURE_ARGS += --disable-cast5
CONFIGURE_ARGS += --disable-blowfish
CONFIGURE_ARGS += --disable-aes
CONFIGURE_ARGS += --disable-twofish
CONFIGURE_ARGS += --disable-sha256
CONFIGURE_ARGS += --disable-sha512
CONFIGURE_ARGS += --disable-bzip2
CONFIGURE_ARGS += --disable-exec
CONFIGURE_ARGS += --disable-photo-viewers
CONFIGURE_ARGS += --disable-keyserver-helpers
CONFIGURE_ARGS += --disable-ldap
CONFIGURE_ARGS += --disable-hkp
CONFIGURE_ARGS += --disable-finger
CONFIGURE_ARGS += --disable-generic
CONFIGURE_ARGS += --disable-keyserver-path
CONFIGURE_ARGS += --disable-dns-srv
CONFIGURE_ARGS += --disable-dns-pka
CONFIGURE_ARGS += --disable-dns-cert

TEST_TARGET = check

include gar/category.mk

