GARNAME = gnupg
GARVERSION = 1.4.9
CATEGORIES = apps

DESCRIPTION = RFC 2440 compliant tool for secure communication and data storage
define BLURB
  GnuPG is a complete and free replacement for PGP.
endef

MASTER_SITES = http://www.gnupg.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWgnupg, depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gnupg/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bzip2
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --enable-threads=solaris

TEST_TARGET = check

include gar/category.mk
