PHP5EXT_NAME = pdopgsql

PACKAGES += CSWphp5pdopgsql

CATALOGNAME_CSWphp5pdopgsql = php5_pdopgsql
SPKG_DESC_CSWphp5pdopgsql = pdopgsql Extention for PHP5
REQUIRED_PKGS_CSWphp5pdopgsql = CSWphp5 CSWlibpq

PATCHFILES += pdopgsql.diff

CONFIGURE_ARGS += --with-pdo-pgsql=shared,$(prefix)/postgresql

PKGFILES_CSWphp5pdopgsql = .*/lib/php/extensions/.*/pdo_pgsql.*
