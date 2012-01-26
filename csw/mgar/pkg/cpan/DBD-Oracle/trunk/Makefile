NAME = DBD-Oracle
VERSION = 1.23
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PYTHIAN

DESCRIPTION = Oracle database driver for the DBI module
define BLURB
endef

DISTFILES = COPYING

PACKAGES = CSWpmdbdoracle CSWpmdbdoraexplain
CATALOGNAME_CSWpmdbdoracle     = pm_dbdoracle
CATALOGNAME_CSWpmdbdoraexplain = pm_dbdoraexplain

SPKG_DESC_CSWpmdbdoracle = $(DESCRIPTION)
SPKG_DESC_CSWpmdbdoraexplain = Tk application ora_explain for DBD::Oracle

RUNTIME_DEP_PKGS_CSWpmdbdoraexplain = CSWpmdbdoracle CSWpmtk

ORACLE_HOME = /opt/csw/instantclient_10_2/$(MM_LIBDIR)
LD_LIBRARY_PATH=$(ORACLE_HOME)
EXTRA_CONFIGURE_EXPORTS = ORACLE_HOME LD_LIBRARY_PATH
EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

NOISALIST = 1
EXTRA_LIB = /opt/csw/instantclient_10_2

# Testing requires a running Oracle database which may not be present.
# Just clean if you have one at hand.
SKIPTEST ?= 1

PKGFILES_CSWpmdbdoraexplain = .*ora_explain.*

# The oracle client is not shipped.
CHECKPKG_OVERRIDES_CSWpmdbdoracle = symbol-not-found|Oracle.so

# This is an internal-only sourcepackage. Users are expected to
# install the Oracle client manually and set LD_LIBRARY_PATH on
# their own according to Oracle policies.
CHECKPKG_OVERRIDES_CSWpmdbdoracle += missing-dependency|CSWorainstclient102

include gar/category.mk
