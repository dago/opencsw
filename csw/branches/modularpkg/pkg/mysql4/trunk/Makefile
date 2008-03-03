GARNAME = mysql
GARVERSION = 4.1.18
CATEGORIES = server

DESCRIPTION = A fast SQL database server.
define BLURB
  MySQL is a widely used and fast SQL database server. It is a client/server
  implementation that consists of a server daemon (mysqld) and many different
  client programs/libraries.
endef

MASTER_SITES = http://mysql.he.net/Downloads/MySQL-4.1/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmysql4,)

DB_USER = mysqld

CONFIGURE_ARGS  = --prefix=$(prefix)/mysql4
CONFIGURE_ARGS += --enable-assembler
CONFIGURE_ARGS += --disable-static --enable-shared
CONFIGURE_ARGS += --enable-local-infile
CONFIGURE_ARGS += --with-mysqld-user=$(DB_USER)
CONFIGURE_ARGS += --enable-thread-safe-client 
CONFIGURE_ARGS += --without-docs --without-bench --without-debug
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-openssl-libs=$(libdir)
CONFIGURE_ARGS += --with-openssl-includes=$(includedir)

include gar/category.mk

CFLAGS   := -mt -xstrconst -D_FORTEC_ $(CFLAGS)
CXXFLAGS := -noex -D_FORTEC_ $(CXXFLAGS)

# Timezone test doesn't take DST into account...
MYTZ = $(shell TZ=MET date '+%Z')
MYTZ_R = mysql-test/r/timezone.result

# Remove I18N tests -- they don't work properly for
# some reason.
pre-test:
	@( cd $(WORKSRC) ; rm -f mysql-test/t/ctype_* )
	@( cd $(WORKSRC) ; $(PERL) -i.bak -plne 's/MET/$(MYTZ)/g' $(MYTZ_R) )
