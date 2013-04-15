# $Id$
#
NAME = memcache
VERSION = 2.2.7
GARTYPE = v2

# to match php5
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = memcache Extention for PHP
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

SPKG_SOURCEURL = http://us.php.net/memcache/
MASTER_SITES = http://pecl.php.net/get/
UFILES_REGEX = (\d+(?:\.\d+)*).tgz

DISTFILES = $(DISTNAME).tgz

GARCOMPILER = GNU

PACKAGES = CSWphp5-memcache
OBSOLETED_BY_CSWphp5-memcache = CSWphp5memcache
CATALOG_NAME_CSWphp5memcache = php5_memcache_stub
SPKG_DESC_CSWphp5-memcache = APC Extention for PHP5
RUNTIME_DEP_PKGS_CSWphp5-memcache = CSWphp5
BUILD_DEPS_CSWphp5-memcache = CSWapache2 CSWphp5-dev
RUNTIME_DEP_PKGS_CSWphp5-memcache += CSWlibgcc-s1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(bindir)/php-config
CONFIGURE_ARGS += --enable-memcache=shared,/opt/csw

LICENSE = CREDITS

# Build flags
EXTRA_CFLAGS += "-I$(predix)/include/libmemcache"

# These should stop the test suite from asking to send results by
# mail.
NO_INTERACTION = 1
EXTRA_TEST_EXPORTS = NO_INTERACTION

# this thing doesn't use destdir.  export install_root with the same
# value
INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

TEST_TARGET = test

CHECKPKG_OVERRIDES_CSWphp5-memcahcewd += surplus-dependency|CSWphp5

include gar/category.mk

post-extract-isa-$(ISA_DEFAULT_$(GARCH)):
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	@$(MAKECOOKIE)
