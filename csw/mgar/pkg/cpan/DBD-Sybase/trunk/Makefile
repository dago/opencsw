GARNAME = DBD-Sybase
GARVERSION = 1.11
CATEGORIES = cpan
AUTHOR = MEWP

DESCRIPTION = Sybase database driver for the DBI module
define BLURB
endef

DISTFILES = COPYING
PATCHFILES = 0001-Use-CS_UNITEXT_TYPE-only-when-available.patch

PACKAGES = CSWpmdbdsybase
CATALOGNAME = pm_dbdsybase

SYBASE = /opt/csw/sybase/OCS-12_5
LD_LIBRARY_PATH = $(SYBASE)/lib

NOISALIST = 1
EXTRA_LIB = $(SYBASE)/lib

LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

EXTRA_CONFIGURE_EXPORTS = SYBASE LD_LIBRARY_PATH
PERL_CONFIGURE_ARGS = --accept_test_defaults --chained Y --threaded_libs N

EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

# We need a running database for this
TEST_SCRIPTS ?=

# These are provided by the Sybase OCS libraries
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libcs.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase.so
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libcomn.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase.so
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libtcl.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase.so
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libct.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase.so

include gar/category.mk
