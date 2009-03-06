PHP5EXT_NAME = xml

PACKAGES += CSWphp5xml

CATALOGNAME_CSWphp5xml = php5_xml
SPKG_DESC_CSWphp5xml = xml Extention for PHP5
REQUIRED_PKGS_CSWphp5xml = CSWphp5 CSWexpat

CONFIGURE_ARGS += --enable-xml=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)

PKGFILES_CSWphp5xml  = .*/lib/php/extensions/.*/xml.so
PKGFILES_CSWphp5xml += .*/lib/php/extensions/.*/xml.a
PKGFILES_CSWphp5xml += .*/include/php/ext/xml/.*
PKGFILES_CSWphp5xml += .*/include/php/ext/libxml/.*
