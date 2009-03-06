PHP5EXT_NAME = pdomysql

PACKAGES += CSWphp5pdomysql

CATALOGNAME_CSWphp5pdomysql = php5_pdomysql
SPKG_DESC_CSWphp5pdomysql = pdomysql Extention for PHP5
REQUIRED_PKGS_CSWphp5pdomysql = CSWphp5 CSWmysql5rt CSWzlib

CONFIGURE_ARGS += --with-pdo-mysql=shared,$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

PKGFILES_CSWphp5pdomysql = .*/lib/php/extensions/.*/pdo_mysql.*
