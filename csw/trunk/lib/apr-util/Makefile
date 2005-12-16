GARNAME = apr-util
GARVERSION = 1.2.2
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime Utilities
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES  = http://apache.mirrored.ca/apr/
MASTER_SITES += http://apache.webthing.com/database/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += apr_dbd_mysql.c
DISTFILES += $(call admfiles,CSWaprutil,depend prototype)
DISTFILES += $(call admfiles,CSWaprutil-devel,depend prototype)
DISTFILES += config.layout

# Force use of GNU iconv
PATCHFILES += iconv.diff

# Trying to fix mysql support
PATCHFILES += dbd-mysql.diff

# What version of bdb should we use?
BDB_VERSION = 43

# Allow use with bdb44
ifeq ($(BDB_VERSION),44)
PATCHFILES += bdb44.diff
DEPENDS    += lib/bdb44
else
DEPENDS    += lib/bdb43
endif

DEPENDS += lib/apr
#DEPENDS += lib/expat
#DEPENDS += lib/iconv
#DEPENDS += server/mysql
#DEPENDS += server/pgsql
#DEPENDS += lib/openldap

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-config
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-dbm=db$(BDB_VERSION)
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb$(BDB_VERSION)
CONFIGURE_ARGS += --with-pgsql=$(prefix)/postgresql
CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql4
CONFIGURE_ARGS += --with-sqlite2=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)

# Extra libpath
EXTRA_LIB = $(prefix)/bdb43/lib $(prefix)/mysql4/lib/mysql
EXTRA_INC = $(prefix)/bdb43/include $(prefix)/mysql4/include/mysql

include ../category.mk

# bdb requires -lnsl
LIBS += -lnsl
export LIBS

pre-configure: copy-layout copy-mysql-dbm autogen
	$(DONADA)
	@$(MAKECOOKIE)

copy-layout:
	@sed -e s,INSTALL_PREFIX,$(prefix),g \
		$(WORKDIR)/config.layout > $(WORKSRC)/config.layout
	@$(MAKECOOKIE)

copy-mysql-dbm:
	@( cd $(WORKSRC) ; cp ../apr_dbd_mysql.c dbd )

autogen:
	@( cd $(WORKSRC) ; autoconf )
	@$(MAKECOOKIE)

post-install:
	@( cd $(DESTDIR)$(bindir) ; ln -s apu-1-config apu-config )
	@$(MAKECOOKIE)

