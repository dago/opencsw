GARNAME = freeradius
GARVERSION = 2.1.6
CATEGORIES = server

DESCRIPTION = A free RADIUS server implementation
define BLURB
  A free RADIUS server implementation
endef

MASTER_SITES = ftp://ftp.freeradius.org:/pub/freeradius/
DISTFILES  = $(GARNAME)-server-$(GARVERSION).tar.gz
DISTNAME = $(GARNAME)-server-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

SPKG_SOURCEURL = http://freeradius.org/

GARCOMPILER = GCC3

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-system-libtool
CONFIGURE_ARGS += --without-rlm_sqlippool
CONFIGURE_ARGS += --without-rlm_sql_mysql
CONFIGURE_ARGS += --without-rlm_sql_postgresql
CONFIGURE_ARGS += --without-rlm_sql_db2
CONFIGURE_ARGS += --without-rlm_sql_firebird
CONFIGURE_ARGS += --without-rlm_sql_freetds
CONFIGURE_ARGS += --without-rlm_sql_iodbc
CONFIGURE_ARGS += --without-rlm_sql_oracle
CONFIGURE_ARGS += --without-rlm_sql_sybase
CONFIGURE_ARGS += --without-rlm_sql_unixodbc
CONFIGURE_ARGS += --without-rlm-ldap
CONFIGURE_ARGS += --without-rlm_eap_ikev2
CONFIGURE_ARGS += --without-rlm_eap_sim
CONFIGURE_ARGS += --without-rlm_eap_tls
CONFIGURE_ARGS += --without-rlm_eap_peap
CONFIGURE_ARGS += --without-rlm_eap_ttls
CONFIGURE_ARGS += --without-rlm_eap_tnc
CONFIGURE_ARGS += --without-rlm_krb5
CONFIGURE_ARGS += --without-rlm_dbm
CONFIGURE_ARGS += --without-rlm_otp
CONFIGURE_ARGS += --without-rlm_pam
CONFIGURE_ARGS += --without-rlm_python
CONFIGURE_ARGS += --without-snmp

# No tests available
TEST_TARGET =

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
