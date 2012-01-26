NAME = DBD-Sybase
VERSION = 1.11
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MEWP

DESCRIPTION = Sybase database driver for the DBI module
define BLURB
endef

DISTFILES = COPYING
PATCHFILES = 0001-Use-CS_UNITEXT_TYPE-only-when-available.patch

EXTRA_MODULATORS = DBDRIVER
MODULATIONS_DBDRIVER = ocs freetds

# I just don't have Sybase x86 OCS in 32 bit
SKIP_MODULATIONS = isa-i386-dbdriver-ocs

PACKAGES = CSWpm-dbd-sybase-ocs CSWpm-dbd-sybase-freetds

CATALOGNAME_CSWpm-dbd-sybase-ocs     = pm_dbd_sybase_ocs
CATALOGNAME_CSWpm-dbd-sybase-freetds = pm_dbd_sybase_freetds

SPKG_DESC_CSWpm-dbd-sybase-ocs     = $(DESCRIPTION) (Linked against Sybase OCS)
SPKG_DESC_CSWpm-dbd-sybase-freetds = $(DESCRIPTION) (Linked against FreeTDS)

# The "standard" is to link against Sybase OCS as it does not have additional
# dependencies. If you don't have that you can *additionally* install
# the version linked against FreeTDS pulling in all additional dependencies.
RUNTIME_DEP_PKGS_CSWpm-dbd-sybase-freetds += CSWfreetds
RUNTIME_DEP_PKGS_CSWpm-dbd-sybase-freetds += CSWggettextrt
RUNTIME_DEP_PKGS_CSWpm-dbd-sybase-ocs     += CSWpm-dbd-sybase-freetds

SYBASE_ocs = /opt/csw/sybase/OCS-12_5
SYBASE_freetds = /opt/csw
SYBASE = $(SYBASE_$(DBDRIVER))

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

DBDSYBASEDIR = $(libdir)/perl/site_perl/auto/DBD/Sybase

MERGE_SCRIPTS_isa-default-dbdriver-ocs = copy-all
MERGE_SCRIPTS_isa-default-dbdriver-freetds = copy-only
MERGE_DIRS_isa-default-dbdriver-freetds = $(DBDSYBASEDIR)

EXTRA_PAX_ARGS  = -s ",/Sybase\.bs$$,/Sybase-$(DBDRIVER).bs,p"
EXTRA_PAX_ARGS += -s ",/Sybase\.so$$,/Sybase-$(DBDRIVER).so,p"

PKGFILES_CSWpm-dbd-sybase-ocs = $(DBDSYBASEDIR)/.*-ocs\..*

ALTERNATIVES_CSWpm-dbd-sybase-ocs = ocs
ALTERNATIVES_CSWpm-dbd-sybase-freetds = freetds
ALTERNATIVE_ocs  = $(DBDSYBASEDIR)/Sybase.so so $(DBDSYBASEDIR)/Sybase-ocs.so 200
ALTERNATIVE_ocs += $(DBDSYBASEDIR)/Sybase.bs bs $(DBDSYBASEDIR)/Sybase-ocs.bs
ALTERNATIVE_freetds  = $(DBDSYBASEDIR)/Sybase.so so $(DBDSYBASEDIR)/Sybase-freetds.so 100
ALTERNATIVE_freetds += $(DBDSYBASEDIR)/Sybase.bs bs $(DBDSYBASEDIR)/Sybase-freetds.bs

# These are provided by the Sybase OCS libraries
CHECKPKG_OVERRIDES_CSWpm-dbd-sybase-ocs += soname-not-found|libcs.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWpm-dbd-sybase-ocs += soname-not-found|libcomn.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWpm-dbd-sybase-ocs += soname-not-found|libtcl.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWpm-dbd-sybase-ocs += soname-not-found|libct.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so

include gar/category.mk
