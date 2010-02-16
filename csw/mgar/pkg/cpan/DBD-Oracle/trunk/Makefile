GARNAME = DBD-Oracle
GARVERSION = 1.23
CATEGORIES = cpan
AUTHOR = PYTHIAN

DESCRIPTION = Oracle database driver for the DBI module
define BLURB
endef

PACKAGES = CSWpmdbdoracle
CATALOGNAME = pm_dbdoracle

ORACLE_HOME = /opt/csw/instantclient_10_2/$(MM_LIBDIR)
LD_LIBRARY_PATH=$(ORACLE_HOME)
EXTRA_CONFIGURE_EXPORTS = ORACLE_HOME LD_LIBRARY_PATH
EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

NOISALIST = 1
EXTRA_LIB = /opt/csw/instantclient_10_2
# EXTRA_INC = $(includedir)/oracle/10.2

include gar/category.mk
