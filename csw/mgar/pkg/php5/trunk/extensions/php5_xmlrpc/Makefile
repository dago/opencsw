PHP5EXT_NAME = xmlrpc

PACKAGES += CSWphp5xmlrpc

CATALOGNAME_CSWphp5xmlrpc = php5_xmlrpc
SPKG_DESC_CSWphp5xmlrpc = xmlrpc Extention for PHP5
REQUIRED_PKGS_CSWphp5xmlrpc = CSWphp5 CSWiconv CSWlibxml2 CSWzlib CSWexpat

CONFIGURE_ARGS += --with-xmlrpc=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)

PKGFILES_CSWphp5xmlrpc = .*/lib/php/extensions/.*/xmlrpc.*
