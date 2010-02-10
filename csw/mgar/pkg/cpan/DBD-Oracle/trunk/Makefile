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
EXTRA_CONFIGURE_EXPORTS = ORACLE_HOME

NOISALIST = 1
# EXTRA_LIB = /opt/csw/oracle/product/10.2.0/client/lib
# EXTRA_INC = $(includedir)/oracle/10.2

include gar/category.mk
