# $Id$
NAME = pgpool
VERSION = 3.0.1
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = A middleware that works between PostgreSQL servers and a PostgreSQL database client
define BLURB
  pgpool-II talks PostgreSQL's backend and frontend protocol, and relays a connection between them.
  Therefore, a database application (frontend) thinks that pgpool-II is the actual PostgreSQL server,
  and the server (backend) sees pgpool-II as one of its clients. Because pgpool-II is transparent
  to both the server and the client, an existing database application can be used with pgpool-II
  almost without a change to its sources.
endef

DISTNAME = pgpool-II-$(VERSION)
MASTER_SITES = http://pgfoundry.org/frs/download.php/2841/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpgpool
CATALOGNAME_CSWpgpool = pgpool
SPKG_DESC_CSWpgpool = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWpgpool += CSWlibpq
RUNTIME_DEP_PKGS_CSWpgpool += CSWlibgnugetopt
RUNTIME_DEP_PKGS_CSWpgpool += CSWlibpcp0

PACKAGES += CSWlibpcp0
CATALOGNAME_CSWlibpcp0 = libpcp0
SPKG_DESC_CSWlibpcp0 = Library for PostgreSQL pgpool providing libpcp.so.0
PKGFILES_CSWlibpcp0 = $(call baseisadirs,$(libdir),libpcp\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibpcp0 += CSWlibgnugetopt

PACKAGES += CSWpgpool-dev
CATALOGNAME_CSWpgpool-dev = pgpool_dev
SPKG_DESC_CSWpgpool-dev = Development Files for pgpool
PKGFILES_CSWpgpool-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWpgpool-dev += CSWpgpool
RUNTIME_DEP_PKGS_CSWpgpool-dev += CSWlibpcp0

# It looks like compiler != gcc means Windows :-(
EXTRA_CFLAGS = -DPGDLLIMPORT=

EXTRA_LINKER_FLAGS = -lgnugetopt

BUILD_DEP_PKGS = CSWlibgnugetopt

sysconfdir = /etc/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-pgsql=$(prefix)/postgresql
# Adding OpenSSL breaks detection of libpq, disable for now
#CONFIGURE_ARGS += --with-openssl
# We must use gegrep insread if egrep as certain arguments are needed
CONFIGURE_ARGS += ac_cv_prog_egrep=$(bindir)/gegrep

EXTRA_PAX_ARGS = -s ",\.sample$$,.CSW,p"

PRESERVECONF += $(sysconfdir)/pcp.conf
PRESERVECONF += $(sysconfdir)/pgpool.conf
PRESERVECONF += $(sysconfdir)/pool_hba.conf

include gar/category.mk
