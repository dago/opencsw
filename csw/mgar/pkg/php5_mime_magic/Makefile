GARNAME = php
GARVERSION = 5.2.6
CATEGORIES = lang
PHP5EXT_NAME = mime_magic

DESCRIPTION = $(PHP5EXT_NAME) Extention for PHP
define BLURB
   $(PHP5EXT_NAME) Extention for PHP
endef

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)/ext/$(PHP5EXT_NAME)

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)
PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin


PACKAGES = CSWphp5mimemagic

MASTER_SITES = http://www.php.net/releases/
SPKG_SOURCEURL = http://www.php.net/get/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

DISTFILES = $(DISTNAME).tar.bz2

CATALOGNAME_CSWphp5mimemagic = php5_$(PHP5EXT_NAME)
SPKG_DESC_CSWphp5mimemagic = $(PHP5EXT_NAME) Extention for PHP5
REQUIRED_PKGS_CSWphp5mimemagic = CSWphp5

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(PHP_BIN)/php-config

post-extract-$(MODULATION):
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	$(DONADA)


TEST_SCRIPTS = manual

test-manual:
	@( TEST_PHP_EXECUTABLE=$(PHP_BIN)/php ; export TEST_PHP_EXECUTABLE ; \
		cd $(WORKSRC); $(PHP_BIN)/php ./run-tests.php -q )
	$(DONADA)

include gar/category.mk
