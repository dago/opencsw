PHP5EXT_NAME = odbc

PACKAGES += CSWphp5odbc

CATALOGNAME_CSWphp5odbc = php5_odbc
SPKG_DESC_CSWphp5odbc = odbc Extention for PHP5
REQUIRED_PKGS_CSWphp5odbc = CSWphp5 CSWunixodbc

PATCHFILES += odbc.diff

CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)

PKGFILES_CSWphp5odbc = .*/lib/php/extensions/.*/odbc.*
