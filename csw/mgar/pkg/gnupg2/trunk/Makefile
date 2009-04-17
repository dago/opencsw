GARNAME    = gnupg
GARVERSION = 2.0.10
CATEGORIES = apps

DESCRIPTION = GnuPG is a complete and free replacement for PGP.
define BLURB
    RFC 2440 compliant tool for secure communication and data storage
endef

PACKAGES              = CSWgnupg2
CATALOGNAME_CSWgnupg2 = gnupg2
SPKG_DESC_CSWgnupg2   = GnuPG is a complete and free replacement for PGP.

SPKG_SOURCEURL = http://www.gnupg.org/
MASTER_SITES   = ftp://ftp.gnupg.org/gcrypt/gnupg/
DISTFILES      = $(GARNAME)-$(GARVERSION).tar.bz2

# fix some missing libraries for Keyserver tools and gpgsm
# Bug ID 996 filed up stream along with patch
# Supposed to be Fixed in the 01/2009 SVN version but has not
# made it into a release at the time of this packaging
PATCHFILES = patch-keyserver_and_sm.diff

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

NOISALIST  = 1
BUILD64    = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libcurl
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bzip2
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --enable-threads=solaris

# This is somehow not correctly detected from autoconf
EXTRA_LINKER_FLAGS  = -lgpg-error
# Needed for nanosleep()
EXTRA_LINKER_FLAGS += -lrt

REQUIRED_PKGS  = CSWlibksba CSWgpgerr CSWgcrypt 
REQUIRED_PKGS += CSWcurlrt CSWoldaprt CSWzlib CSWpth CSWlibidn 
REQUIRED_PKGS += CSWbzip2 CSWreadline CSWggettextrt CSWiconv CSWosslrt

TEST_TARGET = check

include gar/category.mk
