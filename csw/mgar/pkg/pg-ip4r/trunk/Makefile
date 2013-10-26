# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pg-ip4r
VERSION = 1.05
GARTYPE = v2
GARCOMPILER = SOS12U3

DESCRIPTION = Advanced cidr type for PostgreSQL
define BLURB
   ip4 and ip4r are types that contain a single IPv4 address and a range of
   IPv4 addresses respectively. They can be used as a more flexible, indexable
   version of the cidr type.
endef

# We do not donwload ip4r from pgfoundry.org, since they use fusionforge:
# the fusionforge download script requires an id for getting a file, e.g.
#
#  http://pgfoundry.org/frs/download.php/3380/ip4r-2.0.tgz
#
# now the id is 3380. Everything after that id is ignored
#
#  http://pgfoundry.org/frs/download.php/3380/foobar.tgz
#
# downloads the same file as the first example.
#
# If mgar tries to download ip4r-1.05.tar.gz and 
#
#  http://pgfoundry.org/frs/download.php/3380
#
# is in master sites, it will succeed and download the wrong file.
#
# Therefore, ip4r-XY has to be downloaded manually and placed in the
# proper place.
MASTER_SITES  = http://ftp.postgresql.org/pub/source/v8.3.23/
MASTER_SITES += http://ftp.postgresql.org/pub/source/v8.4.18/
MASTER_SITES += http://ftp.postgresql.org/pub/source/v9.0.14/
MASTER_SITES += http://ftp.postgresql.org/pub/source/v9.1.10/
MASTER_SITES += http://ftp.postgresql.org/pub/source/v9.2.5/
MASTER_SITES += http://ftp.postgresql.org/pub/source/v9.3.1/
DISTFILES  = README.CSW
DISTFILES += postgresql-8.3.23.tar.gz
DISTFILES += postgresql-8.4.18.tar.gz
DISTFILES += postgresql-9.0.14.tar.gz
DISTFILES += postgresql-9.1.10.tar.gz
DISTFILES += postgresql-9.2.5.tar.gz
DISTFILES += postgresql-9.3.1.tar.gz
# This is only required for Postgres 8.3, since version 2.0 source
# references to numeric_div_trun() which is not available in 8.3
DISTFILES += ip4r-1.05.tar.gz
# This is used for Postgres 8.4-9.0, which do not feature extension
# packaging mechanism
DISTFILES += ip4r-2.0.tgz
# This is used for Postgres 9.1+, which feature extension packaging
# mechanism
DISTFILES += ip4r-extension-2.0.tgz

EXTRA_MODULATORS	= PGVERSION
MODULATIONS_PGVERSION	= 83 84 90 91 92 93

# Variables for PGVERSION modulations
PG_SOURCE_NAME_83		= postgresql-8.3.23
PG_BASEVERSION_DOT_83		= 8.3
IP4R_SOURCE_NAME_83		= ip4r-1.05
CONFIGURE_ARGS_83		= --with-docdir=$(docdir)/postgresql/$(PGVERSION)

PG_SOURCE_NAME_84		= postgresql-8.4.18
PG_BASEVERSION_DOT_84		= 8.4
IP4R_SOURCE_NAME_84		= ip4r-2.0
CONFIGURE_ARGS_84		= --docdir=$(docdir)/postgresql/$(PGVERSION)

PG_SOURCE_NAME_90		= postgresql-9.0.14
PG_BASEVERSION_DOT_90		= 9.0
IP4R_SOURCE_NAME_90		= ip4r-2.0
CONFIGURE_ARGS_90		= --docdir=$(docdir)/postgresql/$(PGVERSION)

PG_SOURCE_NAME_91		= postgresql-9.1.10
PG_BASEVERSION_DOT_91		= 9.1
IP4R_SOURCE_NAME_91		= ip4r-extension-2.0
CONFIGURE_ARGS_91		= --docdir=$(docdir)/postgresql/$(PGVERSION)

PG_SOURCE_NAME_92		= postgresql-9.2.5
PG_BASEVERSION_DOT_92		= 9.2
IP4R_SOURCE_NAME_92		= ip4r-extension-2.0
CONFIGURE_ARGS_92		= --docdir=$(docdir)/postgresql/$(PGVERSION)

PG_SOURCE_NAME_93		= postgresql-9.3.1
PG_BASEVERSION_DOT_93		= 9.3
IP4R_SOURCE_NAME_93		= ip4r-extension-2.0
CONFIGURE_ARGS_93		= --docdir=$(docdir)/postgresql/$(PGVERSION)

MERGE_SCRIPTS_$(MODULATION)	= copy-relocate


PACKAGES  =  $(foreach v,$(MODULATIONS_PGVERSION),CSWpg$(v)-ip4r)
$(foreach v,$(MODULATIONS_PGVERSION),\
	$(eval SPKG_DESC_CSWpg$(v)-ip4r = Indexable version of the cidr type for PostgreSQL $(PG_BASEVERSION_DOT_$(v)))\
	$(eval PKGFILES_CSWpg$(v)-ip4r = .*/postgresql/$(v)/.*)\
)

BUILD64 = 1

# We define NO_PGXS=1 so that pg_config is not called. This is the main reason we do it the hard way.
BUILD_ARGS = NO_PGXS=1
INSTALL_ARGS = NO_PGXS=1

CONFIGURE_SCRIPTS = ip4r
BUILD_SCRIPTS = ip4r
INSTALL_SCRIPTS = ip4r
# Deliberately no check
TEST_SCRIPTS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --datadir=$(datadir)/postgresql/$(PGVERSION)
CONFIGURE_ARGS += --with-gssapi
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-libxml
CONFIGURE_ARGS += --with-libxslt
CONFIGURE_ARGS += --without-krb5
CONFIGURE_ARGS += --without-bonjour
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(PGVERSION))

include gar/category.mk

pre-configure-modulated:
	cp -R $(WORKDIR)/$(IP4R_SOURCE_NAME_$(PGVERSION)) $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/contrib/ip4r
# Copy errcodes.h into src/include/utils/. Used to make builds for 9.1+ work
	-cp $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/src/backend/utils/errcodes.h $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/src/include/utils/
	@echo " ===> Adjusting pkglibdir in $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/src/Makefile.global.in"
	@if [ -r $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/src/Makefile.global.in ] ; then \
		gsed -i -r -e 's|^(pkglibdir[[:space:]]*=[[:space:]]*)\$$\(libdir\).*$$|\1$$(libdir)/postgresql/$(PGVERSION)|' $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/src/Makefile.global.in ; \
	else \
		echo "$(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/src/Makefile.global.in not found. Aborting" ; \
		exit 1 ; \
	fi
	@$(MAKECOOKIE)

configure-ip4r:
	cd $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/ && env $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-ip4r:
	cd $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/contrib/ip4r && env $(BUILD_ENV) gmake $(BUILD_ARGS)
	@$(MAKECOOKIE)

install-ip4r:
	cd $(WORKDIR)/$(PG_SOURCE_NAME_$(PGVERSION))/contrib/ip4r && env $(INSTALL_ENV) gmake install $(INSTALL_ARGS)
	@$(MAKECOOKIE)
