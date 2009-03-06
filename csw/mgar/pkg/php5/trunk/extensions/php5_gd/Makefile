PHP5EXT_NAME = gd

PACKAGES += CSWphp5gd

CATALOGNAME_CSWphp5gd = php5_gd
SPKG_DESC_CSWphp5gd = gd Extention for PHP5
REQUIRED_PKGS_CSWphp5gd  = CSWphp5 CSWftype2 CSWgd CSWjpeg
REQUIRED_PKGS_CSWphp5gd += CSWpng CSWt1lib CSWxpm CSWzlib


CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-xpm-dir=$(prefix)
CONFIGURE_ARGS += --with-ttf=$(prefix)
CONFIGURE_ARGS += --with-freetype-dir=$(prefix)
CONFIGURE_ARGS += --with-t1lib=$(prefix)
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-gd-jis-conv

PKGFILES_CSWphp5gd  = .*/lib/php/extensions/.*/gd.*
PKGFILES_CSWphp5gd += .*/include/php/ext/gd/.*
