NAME = APC
VERSION = 3.1.9
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = APC Extention for PHP
define BLURB
	The Alternative PHP Cache (APC) is a free and open opcode cache for PHP.
	It was conceived of to provide a free, open, and robust framework 
	for caching and optimizing PHP intermediate code. 
endef

PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5_EXT = 1

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin

SPKG_SOURCEURL = http://us.php.net/apc/
MASTER_SITES = http://pecl.php.net/package/apc/
UFILES_REGEX = (\d+(?:\.\d+)*).tgz

DISTFILES = $(DISTNAME).tgz

PACKAGES = CSWphp5-apc
OBSOLETED_BY_CSWphp5-apc = CSWphp5apc
CATALOG_NAME_CSWphp5apc = php5_apc_stub
SPKG_DESC_CSWphp5-apc = APC Extention for PHP5
RUNTIME_DEP_PKGS_CSWphp5-apc = CSWphp5
BUILD_DEPS = CSWapache2 CSWphp5-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(bindir)/php-config
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs

LICENSE = LICENSE

# These should stop the test suite from asking to send results by
# mail.
NO_INTERACTION = 1
EXTRA_TEST_EXPORTS = NO_INTERACTION

# this thing doesn't use destdir.  export install_root with the same
# value
INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

TEST_TARGET = test

CHECKPKG_OVERRIDES_CSWphp5-apc += surplus-dependency|CSWphp5

include gar/category.mk

# these are after the include so GARCH is set.
# attempting to get a usable build on sparc:
# https://bugs.php.net/bug.php?id=59100
ifeq ($(GARCH),sparc)
EXTRA_CFLAGS = -xmemalign=1i
endif


post-extract-isa-$(ISA_DEFAULT_$(GARCH)):
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	@$(MAKECOOKIE)
