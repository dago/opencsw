GARNAME = postgresql
GARVERSION = 8.4.1
CATEGORIES = apps

DESCRIPTION = An advanced open source database
define BLURB
endef

MASTER_SITES = http://wwwmaster.postgresql.org/redir/53/h/source/v$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += cswpostgres
DISTFILES += cswusergroup
DISTFILES += postgresql.conf
DISTFILES += README-CSW.txt

PACKAGES = CSWpostgresql CSWpostgresqldoc CSWpostgresqldevel CSWlibpq

CATALOGNAME_CSWpostgresql      = postgresql
CATALOGNAME_CSWpostgresqldoc   = postgresql_doc
CATALOGNAME_CSWpostgresqldevel = postgresql_devel
CATALOGNAME_CSWlibpq           = libpq

SPKG_DESC_CSWpostgresql = An advanced open source database
SPKG_DESC_CSWpostgresqldoc = PostgreSQL Documentation
SPKG_DESC_CSWpostgresqldevel = PostgreSQL Developer Files
SPKG_DESC_CSWlibpq = PostgreSQL Libraries

SPKG_SOURCEURL = http://www.postgresql.org/

REQUIRED_PKGS_CSWpostgresql = CSWreadline CSWzlib CSWlibpq
REQUIRED_PKGS_CSWpostgresqldevel = CSWpostgresql

LICENSE = COPYRIGHT

prefix = $(BUILD_PREFIX)/postgresql
docdir = $(BUILD_PREFIX)/share/doc

EXTRA_INC = $(BUILD_PREFIX)/include
EXTRA_LIB = $(BUILD_PREFIX)/lib

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_PAX_ARGS = -s ",^\./opt/csw/postgresql/share/doc,./opt/csw/share/doc/postgresql,p"

PKGFILES_CSWpostgresqldoc = $(PKGFILES_DOC)
PKGFILES_CSWpostgresqldevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibpq = $(PKGFILES_RT)

# -> TODO: start in rc3.d S10, Stop everywhere else in K90
INITSMF = /etc/init.d/cswpostgres

# -> TODO: Migrate /opt/csw/var/pgdata to /var/opt/csw/postgresql/pgdata
USERGROUP = /opt/csw/etc/pkg/postgresql

# -> TODO: Migrate /opt/csw/etc/postgresql.conf to /etc/opt/csw/postgresql.conf
PRESERVECONF = /opt/csw/etc/postgresql.conf

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

post-merge:
	ginstall -d $(PKGROOT)/etc/init.d && ginstall $(WORKDIR)/cswpostgres $(PKGROOT)/etc/init.d/
	ginstall -d $(PKGROOT)/opt/csw/etc/pkg/postgresql && ginstall $(WORKDIR)/cswusergroup $(PKGROOT)/opt/csw/etc/pkg/postgresql/
	ginstall -d $(PKGROOT)/opt/csw/etc && ginstall $(WORKDIR)/postgresql.conf $(PKGROOT)/opt/csw/etc/
	ginstall -d $(PKGROOT)$(docdir)/postgresql/ && ginstall $(WORKDIR)/README-CSW.txt $(PKGROOT)$(docdir)/postgresql/
	@$(MAKECOOKIE)
