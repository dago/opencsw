GARNAME = gnupg
GARVERSION = 2.0.10
CATEGORIES = apps

DESCRIPTION = RFC 2440 compliant tool for secure communication and data storage
define BLURB
  GnuPG is a complete and free replacement for PGP.
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgnupg,)

SPKG_SOURCEURL = http://www.gnupg.org/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

# This is somehow not correctly detected from autoconf
EXTRA_LINKER_FLAGS = -lgpg-error

# Needed for nanosleep()
EXTRA_LINKER_FLAGS += -lrt

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bzip2
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --enable-threads=solaris

TEST_TARGET = check

include gar/category.mk
