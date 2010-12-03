GARNAME = freeradius
GARVERSION = 2.1.10
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

GARCOMPILER = GCC4

# Stripping libtool breaks the build in versions <=2.1.7
#STRIP_LIBTOOL = 1

## Some of the RLM Submodules don't seem to pick up the include paths without 
## setting CFLAGS
EXTRA_CFLAGS  = -I/opt/csw/include
#EXTRA_CFLAGS += -DIE_LIBTOOL_DIE
#CONFIGURE_ENV = CFLAGS="$(CFLAGS)"

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += CC=$(CC) CXX=$(CXX) F77=$(F77) FC=$(FC)
CONFIGURE_ARGS += CFLAGS="$(CFLAGS)" CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += CPPFLAGS="$(CPPFLAGS)" FCFLAGS="$(FCFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"
CONFIGURE_ARGS += --with-system-libtool
CONFIGURE_ARGS += --with-system-libltld
CONFIGURE_ARGS += --without-rlm_sqlippool
CONFIGURE_ARGS += --with-rlm_sql_mysql
CONFIGURE_ARGS += --without-rlm_sql_postgresql
CONFIGURE_ARGS += --without-rlm_sql_db2
CONFIGURE_ARGS += --without-rlm_sql_firebird
CONFIGURE_ARGS += --without-rlm_sql_freetds
CONFIGURE_ARGS += --without-rlm_sql_iodbc
CONFIGURE_ARGS += --without-rlm_sql_oracle
CONFIGURE_ARGS += --without-rlm_sql_sybase
CONFIGURE_ARGS += --with-rlm_sql_unixodbc
CONFIGURE_ARGS += --with-rlm-ldap
CONFIGURE_ARGS += --without-rlm_eap_ikev2
CONFIGURE_ARGS += --without-rlm_eap_sim
CONFIGURE_ARGS += --with-rlm_eap_tls
CONFIGURE_ARGS += --without-rlm_eap_peap
CONFIGURE_ARGS += --without-rlm_eap_ttls
CONFIGURE_ARGS += --without-rlm_eap_tnc
CONFIGURE_ARGS += --with-rlm_krb5
CONFIGURE_ARGS += --without-rlm_dbm
CONFIGURE_ARGS += --without-rlm_otp
CONFIGURE_ARGS += --with-rlm_pam
CONFIGURE_ARGS += --with-rlm_python
CONFIGURE_ARGS += --with-snmp
CONFIGURE_ARGS += --with-rlm_counter-include-dir=/opt/csw/include
CONFIGURE_ARGS += --with-rlm_counter-lib-dir=/opt/csw/lib/$(MM_LIBDIR)

# No tests available
TEST_TARGET =

INSTALL_ARGS += R=$(DESTDIR)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
