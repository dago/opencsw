GARNAME    = gnupg
GARVERSION = 2.0.10
CATEGORIES = apps

DESCRIPTION = GnuPG is a complete and free replacement for PGP.
define BLURB
    RFC 2440 compliant tool for secure communication and data storage
endef

PACKAGES    = CSWgnupg2
CATALOGNAME = gnupg2
SPKG_DESC   = GnuPG is a complete and free replacement for PGP.

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

BUILD64    = 1
NO_ISAEXEC = 0

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

ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpg-agent
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpg-connect-agent
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpg2
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpgconf
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpgkey2ssh
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpgparsemail
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpgsm
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpgsm-gencert.sh
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/gpgv2
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/kbxutil
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/scdaemon
ISAEXEC_EXCLUDE_FILES += /opt/csw/bin/watchgnupg

MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpg-agent
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpg-connect-agent
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpg2
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpgconf
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpgkey2ssh
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpgparsemail
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpgsm
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpgsm-gencert.sh
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/gpgv2
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/kbxutil
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/scdaemon
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/watchgnupg

REQUIRED_PKGS  = CSWlibksba CSWgpgerr CSWgcrypt CSWlibassuan
REQUIRED_PKGS += CSWcurlrt CSWoldaprt CSWzlib CSWpth CSWlibidn 
REQUIRED_PKGS += CSWbzip2 CSWreadline CSWggettextrt CSWiconv CSWosslrt

TEST_TARGET = check

include gar/category.mk
