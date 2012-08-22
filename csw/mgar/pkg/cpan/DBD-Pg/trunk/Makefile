NAME = DBD-Pg
VERSION = 2.17.2
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TURNSTEP

DESCRIPTION = PostgreSQL database driver for the DBI module
define BLURB
  DBD::Pg is a Perl module which works with the DBI module to provide access
  to PostgreSQL databases.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DISTFILES += changelog.CSW

PATCHFILES = 0001-Dont-return-value-in-dequote_bytea.patch

PACKAGES = CSWpm-dbd-pg
SPKG_DESC_$(PACKAGES) = $(DESCRIPTION)

OBSOLETED_BY_$(PACKAGES) = CSWpmdbdpg 
CATALOGNAME_CSWpmdbdpg = pm_dbdpg_stub
RUNTIME_DEP_PKGS_$(PACKAGES) += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_$(PACKAGES) += CSWlibpq5
RUNTIME_DEP_PKGS_$(PACKAGES) += CSWpm-dbi

CHECKPKG_OVERRIDES_CSWpm-dbd-pg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pm_dbd_pg/license
CHECKPKG_OVERRIDES_CSWpmdbdpg += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pm_dbdpg_stub/license

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS_$(PACKAGES))
BUILD_DEP_PKGS += CSWpostgresql-dev

LICENSE = README

PERL_CONFIGURE_ARGS += cc="$(CC)"
PERL_CONFIGURE_ARGS += ld="$(CC)"

include gar/category.mk

# set postgres home and lib
CONFIGURE_ENV += POSTGRES_HOME="$(prefix)"
CONFIGURE_ENV += POSTGRES_LIB="$(libdir) -lssl"
