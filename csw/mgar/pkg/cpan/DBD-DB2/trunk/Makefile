NAME = DBD-DB2
VERSION = 1.84
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = IBMTORDB2

DESCRIPTION = DB2 Driver for DBI
define BLURB
endef

CATALOG_RELEASE = unstable

# libdb2.so.1 requires libm.so.2 only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = LICENSE

PACKAGES += CSWpm-dbd-db2
SPKG_DESC_CSWpm-dbd-db2 = DB2 Driver for DBI

# These are just docs
CHECKPKG_OVERRIDES_CSWpm-dbd-db2 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/DBD::DB2.3perl
CHECKPKG_OVERRIDES_CSWpm-dbd-db2 += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/DBD/DB2.pod

# This is the default install location of the client
CHECKPKG_OVERRIDES_CSWpm-dbd-db2 += bad-rpath-entry|/opt/IBM/db2/V8.1/lib|opt/csw/lib/perl/csw/auto/DBD/DB2/Constants/Constants.so
CHECKPKG_OVERRIDES_CSWpm-dbd-db2 += bad-rpath-entry|/opt/IBM/db2/V8.1/lib|opt/csw/lib/perl/csw/auto/DBD/DB2/DB2.so

# The library is installed manually and not shipped via OpenCSW
CHECKPKG_OVERRIDES_CSWpm-dbd-db2 += soname-not-found|libdb2.so.1|is|needed|by|opt/csw/lib/perl/csw/auto/DBD/DB2/DB2.so

NOISALIST = 1

DB2_HOME = /opt/IBM/db2/V8.1
DB2_LIB = $(DB2_HOME)/lib

EXTRA_LIB += $(DB2_LIB)

EXTRA_CONFIGURE_ENV += DB2_HOME=$(DB2_HOME)
EXTRA_CONFIGURE_ENV += DB2LIB=$(DB2_LIB)

include gar/category.mk
