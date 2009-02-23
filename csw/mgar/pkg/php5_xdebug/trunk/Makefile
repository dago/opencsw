GARNAME = xdebug
GARVERSION = 2.0.4
CATEGORIES = lang

DESCRIPTION = Xdebug Extention for PHP
define BLURB
The Xdebug extension helps you debugging your script by providing a lot of valuable debug information. The debug information that Xdebug can provide includes the following:

    * stack traces and function traces in error messages with:
          o full parameter display for user defined functions
          o function name, file name and line indications
          o support for member functions
    * memory allocation
    * protection for infinite recursions
endef


INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)
PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin


PACKAGES = CSWphp5xdebug

MASTER_SITES = http://www.xdebug.org/
SPKG_SOURCEURL = http://www.xdebug.org/files/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

DISTFILES = $(DISTNAME).tgz

CATALOGNAME_CSWphp5xdebug = php5_xdebug
SPKG_DESC_CSWphp5xdebug = Xdebug Extention for PHP5
REQUIRED_PKGS_CSWphp5xdebug = CSWphp5

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(PHP_BIN)/php-config

post-extract-modulated:
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	$(DONADA)

# There are no test scripts
TEST_SCRIPTS =

include gar/category.mk
