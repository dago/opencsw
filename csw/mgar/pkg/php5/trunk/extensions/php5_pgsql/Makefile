PHP5EXT_NAME = pgsql

PACKAGES += CSWphp5pgsql

CATALOGNAME_CSWphp5pgsql = php5_pgsql
SPKG_DESC_CSWphp5pgsql = pgsql Extention for PHP5
REQUIRED_PKGS_CSWphp5pgsql = CSWphp5 CSWlibpq

PATCHFILES += pgsql.diff

CONFIGURE_ARGS += --with-pgsql=shared,$(prefix)/postgresql

PKGFILES_CSWphp5pgsql = .*/lib/php/extensions/.*/pgsql.*
