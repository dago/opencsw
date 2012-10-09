# $Id$

NAME = ffmpeg
VERSION = current
CATEGORIES = lang
GARTYPE = v2

# to match php5
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

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
MASTER_SITES = http://www.wilbury.sk/private/files/
DISTNAME = $(NAME)-$(VERSION)

DISTFILES = $(DISTNAME).tar.bz2
WORKSRC = $(WORKDIR)/ffmpeg-php

GARCOMPILER = GCC4

PACKAGES = CSWphp5-ffmpeg
OBSOLETED_BY_CSWphp5-ffmpeg = CSWphp5ffmpeg
CATALOG_NAME_CSWphp5ffmpeg = php5_ffmpeg_stub
SPKG_DESC_CSWphp5-ffmpeg = APC Extention for PHP5
RUNTIME_DEP_PKGS_CSWphp5-ffmpeg = CSWphp5
RUNTIME_DEP_PKGS_CSWphp5-ffmpeg += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWphp5-ffmpeg += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWphp5-ffmpeg += CSWlibavcodec54
RUNTIME_DEP_PKGS_CSWphp5-ffmpeg += CSWlibavformat54
BUILD_DEPS = CSWapache2 CSWphp5-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(bindir)/php-config
CONFIGURE_ARGS += --with-ffmpeg=shared,$(prefix)

LICENSE_TEXT = License

# These should stop the test suite from asking to send results by
# mail.
NO_INTERACTION = 1
EXTRA_TEST_EXPORTS = NO_INTERACTION

# this thing doesn't use destdir.  export install_root with the same
# value
INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

TEST_TARGET = 

CHECKPKG_OVERRIDES_CSWphp5-ffmpeg += surplus-dependency|CSWphp5

include gar/category.mk

post-extract-isa-$(ISA_DEFAULT_$(GARCH)):
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	@$(MAKECOOKIE)
