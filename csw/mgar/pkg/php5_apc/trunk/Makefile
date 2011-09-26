NAME = APC
VERSION = 3.1.9
CATEGORIES = lang

DESCRIPTION = APC Extention for PHP
define BLURB
	The Alternative PHP Cache (APC) is a free and open opcode cache for PHP.
	It was conceived of to provide a free, open, and robust framework 
	for caching and optimizing PHP intermediate code. 
endef

PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin

SPKG_SOURCEURL = http://us.php.net/apc/
MASTER_SITES = http://pecl.php.net/package/apc/
UFILES_REGEX = (\d+(?:\.\d+)*).tgz

DISTFILES = $(DISTNAME).tgz

PACKAGES = CSWphp5-apc
OBSOLETED_BY_CSWphp5-apc = CSWphp5apc
SPKG_DESC_CSWphp5-apc = APC Extention for PHP5
RUNTIME_DEP_PKGS_CSWphp5-apc = CSWphp5
BUILD_DEPS = CSWapache2 CSWphp5-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(bindir)/php-config
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs

# These should stop the test suite from asking to send results by
# mail.
NO_INTERACTION = 1
EXTRA_TEST_EXPORTS = NO_INTERACTION

# this thing doesn't use destdir.  export install_root with the same
# value
INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

TEST_TARGET = test

post-extract-modulated:
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	$(DONADA)

include gar/category.mk
