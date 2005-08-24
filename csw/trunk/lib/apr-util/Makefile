GARNAME = apr-util
GARVERSION = 1.0.0
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime Utilities
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES = http://apache.gnusoft.net/apr/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

#DEPENDS += lib/apr lib/openldap lib/bdb4
DEPENDS += lib/apr

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(DESTDIR)$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-ldap-include=$(includedir)
CONFIGURE_ARGS += --with-ldap-lib=$(libdir)
CONFIGURE_ARGS += --with-dbm=db4
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb4
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)

include ../category.mk

post-install:
	@( cd $(DESTDIR)$(bindir) ; ln -s apu-1-config apu-config )
	@$(MAKECOOKIE)
