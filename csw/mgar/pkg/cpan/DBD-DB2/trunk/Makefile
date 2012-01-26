NAME = DBD-DB2
VERSION = 1.78
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = IBMTORDB2

DESCRIPTION = DataBase Driver for DB2 UDB
define BLURB
  DBD::DB2 is a Perl5 module which when used in conjunction with DBI 
  allows Perl5 to communicate with IBM's DB2 Universal Database.
  In the generic sense, most of the functionality provided by any of the 
  available DBDs is accessed indirectly through the DBI.
endef

CATALOGNAME = pm_dbddb2
PACKAGES    = CSWpmdbddb2

DB2_HOME    = /opt/IBM/db2/V9
EXTRA_LIB   = $(DB2_HOME)/lib32
LICENSE     = LICENSE

include gar/category.mk

CONFIGURE_ENV += DB2_HOME=$(DB2_HOME)
CONFIGURE_ENV += DB2LIB=$(DB2_HOME)/lib32
