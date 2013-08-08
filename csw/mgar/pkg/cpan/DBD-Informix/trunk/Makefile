NAME = DBD-Informix
VERSION = 2013.0521
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JOHNL

DESCRIPTION = IBM Informix Database Driver for Perl DBI
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

BUILD_DEP_PKGS += CSWpm-dbi

PACKAGES += CSWpm-dbd-informix
CATALOGNAME_CSWpm-dbd-informix = pm_dbd_informix
SPKG_DESC_CSWpm-dbd-informix = IBM Informix Database Driver for Perl DBI
RUNTIME_DEP_PKGS_CSWpm-dbd-informix += CSWpm-dbi

# This is the location of the client library which we are not allowed to distribute
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += bad-rpath-entry|/opt/IBM/informix/lib|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += bad-rpath-entry|/opt/IBM/informix/lib|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += bad-rpath-entry|/opt/IBM/informix/lib/esql|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += soname-not-found|/opt/IBM/informix/lib/esql/libifgen.so|is|needed|by|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += soname-not-found|/opt/IBM/informix/lib/esql/libifglx.so|is|needed|by|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += soname-not-found|/opt/IBM/informix/lib/esql/libifos.so|is|needed|by|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += soname-not-found|/opt/IBM/informix/lib/esql/libifgls.so|is|needed|by|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += soname-not-found|/opt/IBM/informix/lib/libifasf.so|is|needed|by|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += soname-not-found|/opt/IBM/informix/lib/esql/libifsql.so|is|needed|by|opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += no-direct-binding|/opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so|is|not|directly|bound|to|soname|/opt/IBM/informix/lib/esql/libifglx.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += no-direct-binding|/opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so|is|not|directly|bound|to|soname|/opt/IBM/informix/lib/esql/libifgls.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += no-direct-binding|/opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so|is|not|directly|bound|to|soname|/opt/IBM/informix/lib/libifasf.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += no-direct-binding|/opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so|is|not|directly|bound|to|soname|/opt/IBM/informix/lib/esql/libifsql.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += no-direct-binding|/opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so|is|not|directly|bound|to|soname|/opt/IBM/informix/lib/esql/libifos.so
CHECKPKG_OVERRIDES_CSWpm-dbd-informix += no-direct-binding|/opt/csw/lib/perl/csw/auto/DBD/Informix/Informix.so|is|not|directly|bound|to|soname|/opt/IBM/informix/lib/esql/libifgen.so

NOISALIST = 1

INFORMIXDIR = /opt/IBM/informix

EXTRA_CONFIGURE_EXPORTS += INFORMIXDIR
CONFIGURE_ENV_INFORMIXDIR = $(INFORMIXDIR)
EXTRA_CONFIGURE_EXPORTS += INFORMIXSERVER
CONFIGURE_ENV_INFORMIXSERVER = localhost
EXTRA_CONFIGURE_EXPORTS += DBD_INFORMIX_NO_ESQLTEST
CONFIGURE_ENV_DBD_INFORMIX_NO_ESQLTEST=yes

CONFIGURE_ENV_PATH = $(INFORMIXDIR)/bin:$(PATH)

EXTRA_BUILD_EXPORTS += INFORMIXDIR
BUILD_ENV_INFORMIXDIR = $(INFORMIXDIR)

BUILD_ENV_PATH = $(INFORMIXDIR)/bin:$(PATH)

EXTRA_LIB += $(INFORMIXDIR)/lib
EXTRA_LIB += $(INFORMIXDIR)/lib/esql

SKIPTEST ?= 1

include gar/category.mk
