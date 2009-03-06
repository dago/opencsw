PHP5EXT_NAME = sqlite

PACKAGES += CSWphp5sqlite

CATALOGNAME_CSWphp5sqlite = php5_sqlite
SPKG_DESC_CSWphp5sqlite = sqlite Extention for PHP5
REQUIRED_PKGS_CSWphp5sqlite = CSWphp5 CSWsqlite

CONFIGURE_ARGS += --with-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --enable-sqlite-utf8

PKGFILES_CSWphp5sqlite = .*/lib/php/extensions/.*/sqlite.*
PKGFILES_CSWphp5sqlite += .*/include/php/ext/sqlite/.*
