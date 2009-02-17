GARNAME = php5
GARVERSION = 5.2.6
CATEGORIES = lang
PHP5EXT_NAME = mbstring

DESCRIPTION = mbstring Extention for PHP
define BLURB
   mbstring Extention for PHP
endef

WORKSRC = $(WORKSRC)/ext/$(PHP5EXT_NAME)

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)
PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin


PACKAGES = CSWphp5mbstring

MASTER_SITES = http://www.php.net/releases/
SPKG_SOURCEURL = http://www.php.net/get/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

DISTFILES = $(DISTNAME).tar.bz2

CATALOGNAME_CSWphp5xdebug = php5_mbstring
SPKG_DESC_CSWphp5xdebug = mbstring Extention for PHP5
REQUIRED_PKGS_CSWphp5xdebug = CSWphp5

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(PHP_BIN)/php-config

post-extract-modulated:
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	$(DONADA)

# There are no test scripts
TEST_SCRIPTS =

include gar/category.mk
