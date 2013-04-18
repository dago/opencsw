# $Id$
#
NAME = memcache
VERSION = 2.2.7
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-i386

# to match php5

DESCRIPTION = Extention memcache for PHP5
define BLURB
   This extension allows you to work with memcached through handy OO and procedural interfaces.
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
SPKG_DESC_CSWphp5-memcache =  Extention memcache for PHP5
RUNTIME_DEP_PKGS_CSWphp5-memcache = CSWphp5
BUILD_DEPS_CSWphp5-memcache = CSWapache2 CSWphp5-dev
RUNTIME_DEP_PKGS_CSWphp5-memcache += CSWlibgcc-s1
ARCH_CSWphp5-memcache = all

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(bindir)/php-config
CONFIGURE_ARGS += --enable-memcache=shared,/opt/csw

LICENSE = CREDITS

# These should stop the test suite from asking to send results by
# mail.
NO_INTERACTION = 1
EXTRA_TEST_EXPORTS = NO_INTERACTION

# this thing doesn't use destdir.  export install_root with the same
# value
INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

TEST_TARGET = test

include gar/category.mk

post-extract-isa-$(ISA_DEFAULT_$(GARCH)):
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	@$(MAKECOOKIE)

