GARNAME = postgresql
BASE_VERSION = 8.4
PATCHLEVEL = 1
GARVERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = apps

DESCRIPTION = An advanced open source database
define BLURB
endef

bindir_install = $(prefix)/bin/$(GARNAME)/$(BASE_VERSION)
datadir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)
docdir=$(prefix)/share/doc/$(GARNAME)/$(BASE_VERSION)
includedir=$(prefix)/include/$(GARNAME)/$(BASE_VERSION)
infodir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)/info
libdir_install =$(prefix)/lib/$(GARNAME)/$(BASE_VERSION)
libexecdir_install =$(prefix)/libexec/$(GARNAME)/$(BASE_VERSION)
lispdir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)/emacs/site-lisp
localstatedir = /var/opt/csw/$(GARNAME)/$(BASE_VERSION)
mandir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)/man
sbindir_install = $(prefix)/sbin/$(GARNAME)/$(BASE_VERSION)
sharedstatedir=$(prefix)/share/$(GARNAME)/$(BASE_VERSION)
sourcedir=$(prefix)/src/$(GARNAME)/$(BASE_VERSION)
sysconfdir = /etc/opt/csw/$(GARNAME)/$(BASE_VERSION)

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

# prefix = $(BUILD_PREFIX)/postgresql
# docdir = $(BUILD_PREFIX)/share/doc

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
INITSMF = /etc/opt/csw/init\.d/cswpostgres-$(BASE_VERSION)

# -> TODO: Migrate /opt/csw/var/pgdata to /var/opt/csw/postgresql/pgdata
USERGROUP = /etc/opt/csw/pkg/postgresql-$(BASE_VERSION)

# -> TODO: Migrate /opt/csw/etc/postgresql.conf to /etc/opt/csw/postgresql.conf
PRESERVECONF = /opt/csw/etc/postgresql\.conf

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

post-merge:
	ginstall -d $(PKGROOT)/etc/opt/csw/init.d
	ginstall \
		$(WORKDIR)/cswpostgres \
		$(PKGROOT)/etc/opt/csw/init.d/cswpostgres-$(BASE_VERSION)
	ginstall -d $(PKGROOT)/etc/opt/csw/pkg/$(GARNAME)
	ginstall $(WORKDIR)/cswusergroup \
		$(PKGROOT)/etc/opt/csw/pkg/postgresql/$(GARNAME)-$(BASE_VERSION)
	ginstall -d $(PKGROOT)/etc/opt/csw/$(GARNAME)-$(BASE_VERSION)
	ginstall $(WORKDIR)/postgresql.conf \
		$(PKGROOT)/etc/opt/csw/$(GARNAME)-$(BASE_VERSION)
	ginstall -d $(PKGROOT)$(docdir)/$(GARNAME)
	ginstall $(WORKDIR)/README-CSW.txt $(PKGROOT)$(docdir)/$(GARNAME)/
	@$(MAKECOOKIE)
