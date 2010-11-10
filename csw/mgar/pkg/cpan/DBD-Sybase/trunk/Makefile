GARNAME = DBD-Sybase
GARVERSION = 1.11
CATEGORIES = cpan
AUTHOR = MEWP

DESCRIPTION = Sybase database driver for the DBI module
define BLURB
endef

DISTFILES = COPYING
PATCHFILES = 0001-Use-CS_UNITEXT_TYPE-only-when-available.patch

EXTRA_MODULATORS = DBDRIVER
MODULATIONS_DBDRIVER = ocs freetds

PACKAGES = CSWpmdbdsybase CSWpmdbdsybaseftds

CATALOGNAME_CSWpmdbdsybase = pm_dbdsybase
CATALOGNAME_CSWpmdbdsybaseftds = pm_dbdsybaseftds

SPKG_DESC_CSWpmdbdsybase = $(DESCRIPTION) (Linked against Sybase OCS)
SPKG_DESC_CSWpmdbdsybaseftds = $(DESCRIPTION) (Linked against FreeTDS)

# The "standard" is to link against Sybase OCS as it does not have additional
# dependencies. If you don't have that you can *additionally* install
# the version linked against FreeTDS pulling in all additional dependencies.
RUNTIME_DEP_PKGS_CSWpmdbdsybaseftds += CSWpmdbdsybase
RUNTIME_DEP_PKGS_CSWpmdbdsybaseftds += CSWfreetds
RUNTIME_DEP_PKGS_CSWpmdbdsybaseftds += CSWggettextrt

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

PKGFILES_CSWpmdbdsybaseftds = $(DBDSYBASEDIR)/.*-freetds\..*

ALTERNATIVES_CSWpmdbdsybase = ocs
ALTERNATIVES_CSWpmdbdsybaseftds = freetds
ALTERNATIVE_ocs  = $(DBDSYBASEDIR)/Sybase.so so $(DBDSYBASEDIR)/Sybase-ocs.so 200
ALTERNATIVE_ocs += $(DBDSYBASEDIR)/Sybase.bs bs $(DBDSYBASEDIR)/Sybase-ocs.bs
ALTERNATIVE_freetds  = $(DBDSYBASEDIR)/Sybase.so so $(DBDSYBASEDIR)/Sybase-freetds.so 100
ALTERNATIVE_freetds += $(DBDSYBASEDIR)/Sybase.bs bs $(DBDSYBASEDIR)/Sybase-freetds.bs

# These are provided by the Sybase OCS libraries
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libcs.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libcomn.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libtcl.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWpmdbdsybase += soname-not-found|libct.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so

include gar/category.mk
