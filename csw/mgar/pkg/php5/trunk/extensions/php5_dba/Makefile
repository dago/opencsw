PHP5EXT_NAME = dba

PACKAGES += CSWphp5dba

CATALOGNAME_CSWphp5dba = php5_dba
SPKG_DESC_CSWphp5dba = dba Extention for PHP5
REQUIRED_PKGS_CSWphp5dba = CSWphp5 CSWbdb44 CSWgdbm

CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --with-ndbm
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb44


PKGFILES_CSWphp5dba = .*/lib/php/extensions/.*/dba\.so
