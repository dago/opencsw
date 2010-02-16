GARNAME = DBD-Oracle
GARVERSION = 1.23
CATEGORIES = cpan
AUTHOR = PYTHIAN

DESCRIPTION = Oracle database driver for the DBI module
define BLURB
endef

DISTFILES = COPYING

PACKAGES = CSWpmdbdoracle
CATALOGNAME = pm_dbdoracle

ORACLE_HOME = /opt/csw/instantclient_10_2/$(MM_LIBDIR)
LD_LIBRARY_PATH=$(ORACLE_HOME)
EXTRA_CONFIGURE_EXPORTS = ORACLE_HOME LD_LIBRARY_PATH
EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

NOISALIST = 1
EXTRA_LIB = /opt/csw/instantclient_10_2

# The oracle client is not shipped.
CHECKPKG_OVERRIDES = symbol-not-found|Oracle.so

# This is an internal-only sourcepackage. Users are expected to
# install the Oracle client manually and set LD_LIBRARY_PATH on
# their own according to Oracle policies.
CHECKPKG_OVERRIDES += missing-dependency|CSWorainstclient102

include gar/category.mk
