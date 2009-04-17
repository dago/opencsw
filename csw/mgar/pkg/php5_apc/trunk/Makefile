GARNAME = APC
GARVERSION = 3.0.19
CATEGORIES = lang

DESCRIPTION = APC Extention for PHP
define BLURB
	The Alternative PHP Cache (APC) is a free and open opcode cache for PHP.
	It was conceived of to provide a free, open, and robust framework 
	for caching and optimizing PHP intermediate code. 
endef

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)
PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin

PATCHFILES = apc_pool.diff
PACKAGES = CSWphp5apc

SPKG_SOURCEURL = http://us.php.net/apc/
MASTER_SITES = http://pecl.php.net/package/apc/
UFILES_REGEX = (\d+(?:\.\d+)*).tgz

DISTFILES = $(DISTNAME).tgz

CATALOGNAME_CSWphp5apc = php5_apc
SPKG_DESC_CSWphp5apc = APC Extention for PHP5
REQUIRED_PKGS_CSWphp5apc = CSWphp5

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(PHP_BIN)/php-config
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs

post-extract-modulated:
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	$(DONADA)

TEST_SCRIPTS = manual

test-manual:
	@( TEST_PHP_EXECUTABLE=$(PHP_BIN)/php ; export TEST_PHP_EXECUTABLE ; \
		cd $(WORKSRC); $(PHP_BIN)/php ./run-tests.php -q )
	$(DONADA)

include gar/category.mk
