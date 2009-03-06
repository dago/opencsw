PHP5EXT_NAME = iconv

PACKAGES += CSWphp5iconv

CATALOGNAME_CSWphp5iconv = php5_iconv
SPKG_DESC_CSWphp5iconv = iconv Extention for PHP5
REQUIRED_PKGS_CSWphp5iconv = CSWphp5 CSWiconv

CONFIGURE_ARGS += --with-iconv=shared
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)

EXTRA_CFLAGS   += -I/opt/csw/include
EXTRA_LDFLAGS += -L$(libdir) -R$(libdir)
LIBS = -lrt -lintl 

#PATCHFILES += iconv.diff

PKGFILES_CSWphp5iconv = .*/lib/php/extensions/.*/iconv.*
PKGFILES_CSWphp5iconv += .*/include/php/ext/iconv/.*
