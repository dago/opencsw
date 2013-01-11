# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = php5_ibm_db2
DISTNAME = ibm_db2-$(VERSION)
VERSION = 1.9.5
GARTYPE = v2

DESCRIPTION = IBM DB2 Extension for PHP

MASTER_SITES = http://pecl.php.net/get/
DISTFILES  = $(DISTNAME).tgz

VENDOR_URL = http://pecl.php.net/package/ibm_db2

LICENSE_TEXT = This software is licensed under the Apache 2.0 license

PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5_EXT = 1

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin

PACKAGES = CSWphp5-ibm-db2
SPKG_DESC_CSWphp5-ibm-db2 = IBM DB2 Extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-ibm-db2 = CSWphp5
BUILD_DEP_PKGS += CSWapache2
BUILD_DEP_PKGS += CSWphp5-dev
CHECKPKG_OVERRIDES_CSWphp5-ibm-db2 += surplus-dependency|CSWphp5

# Sorry, we are not allowed to ship that
CHECKPKG_OVERRIDES_CSWphp5-ibm-db2 += bad-rpath-entry|/opt/IBM/db2/V8.1/lib/|opt/csw/php5/lib/php/extensions/no-debug-non-zts-20090626/ibm_db2.so
CHECKPKG_OVERRIDES_CSWphp5-ibm-db2 += soname-not-found|libdb2.so.1|is|needed|by|opt/csw/php5/lib/php/extensions/no-debug-non-zts-20090626/ibm_db2.so

EXTRA_CONFIGURE_EXPORTS += IBM_DB_HOME
CONFIGURE_ENV_IBM_DB_HOME = /opt/IBM/db2/V8.1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(bindir)/php-config
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs

TEST_TARGET = test

# The tests require a running database
SKIPTEST ?= 1

# This thing doesn't use destdir. Export install_root with the same value
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT
INSTALL_ENV_INSTALL_ROOT = $(DESTDIR)

include gar/category.mk

post-extract:
	( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	@$(MAKECOOKIE)

