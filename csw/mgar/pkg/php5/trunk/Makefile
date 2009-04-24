GARNAME    = php
GARVERSION = 5.2.9
CATEGORIES = lang

DESCRIPTION = A high-level scripting language.
define BLURB
	PHP is a widely-used Open Source general-purpose scripting language that is
	especially suited for Web development and can be embedded into HTML. Its
	syntax draws upon C, Java, and Perl, and is easy to learn. PHP runs on many
	different platforms and can be used as a standalone executable or as a
	module under a variety of Web servers. It has excellent support for
	databases, XML, LDAP, IMAP, Java, various Internet protocols, and general
	data manipulation, and is extensible via its powerful API. It is actively
	developed and supported by a talented and energetic international team.
	Numerous Open Source and commercial PHP-based application packages are
	available.
endef

php5_root = $(DESTDIR)$(prefix)/php5
php5_bin  = $(php5_root)/bin
php5_lib  = $(php5_root)/lib

MASTER_SITES   = http://us.php.net/distributions/
SPKG_SOURCEURL = http://www.php.net/downloads.php
DISTFILES     += $(GARNAME)-$(GARVERSION).tar.bz2

INSTALL_ENV   += INSTALL_ROOT=$(DESTDIR)
PHP5ROOT       = $(DESTDIR)$(prefix)/php5

STRIP_DIRS    += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS    += $(PHP5ROOT)/bin

# Auxilliary files
DISTFILES += php.ini.CSW phpext pear.conf.CSW
DISTFILES += CSWphp5_ext_enable.sh CSWphp5_ext_disable.sh

PACKAGES = CSWphp5 CSWphp5devel

CATALOGNAME_CSWphp5        = php5
SPKG_DESC_CSWphp5          = A High-Level Scripting Languages
DISTFILES                 += CSWphp5.postinstall
CATALOGNAME_CSWphp5devel   = php5_devel
SPKG_DESC_CSWphp5devel     = Development files for php5
REQUIRED_PKGS_CSWphp5      = CSWexpat CSWggettextrt CSWiconv 
REQUIRED_PKGS_CSWphp5     += CSWlibxml2 CSWzlib CSWmysql5rt
REQUIRED_PKGS_CSWphp5devel = CSWphp5

PKGFILES_CSWphp5devel  = $(prefix)/php5/bin/php-config
PKGFILES_CSWphp5devel += $(prefix)/php5/bin/phpize
PKGFILES_CSWphp5devel += $(prefix)/php5/bin/peardev
PKGFILES_CSWphp5devel += $(prefix)/php5/include.*
PKGFILES_CSWphp5devel += $(prefix)/php5/lib/php/build/.*
PKGFILES_CSWphp5devel += $(prefix)/php5/man/.*

PATCHFILES += configure.diff
PATCHFILES += php-bug-45557-fix.diff

# PHP Extensions
EXTDIRLIST = $(shell ls -d extensions/*)
include $(foreach X,$(EXTDIRLIST),$(X)/Makefile)

# BerkeleyDB
EXTRA_LIB += $(prefix)/bdb44/lib
EXTRA_INC += $(prefix)/bdb44/include
EXTRA_CFLAGS = -I$(prefix)/include/ncursesw

NOISALIST = 1
DISTFILES += fixme.sh

CONFIGURE_ARGS += --prefix=$(prefix)/php5
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/php5/bin
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --enable-fastcgi
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-pcntl=shared
CONFIGURE_ARGS += --enable-pdo=shared
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --enable-magic-quotes
CONFIGURE_ARGS += --enable-spl=shared
CONFIGURE_ARGS += --with-pcre-regex
CONFIGURE_ARGS += --with-pear=shared

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
ENABLE_CHECK = 0

# SAPI Specific Rules
STRIP_DIRS += $(DESTDIR)$(prefix)/apache2/libexec

# Rebuild Configure Args to build mod_php5
NEW_CONFIGURE_ARGS = $(shell echo $(CONFIGURE_ARGS) |sed -e 's/apxs2/apxs/' \
		-e 's/apache2\/sbin\/apxs/apache\/bin\/apxs/')

# Copy over template config files and utility scripts

post-install-modulated:
	ginstall -m 0755 \
		$(WORKDIR)/phpext \
		$(DESTDIR)$(prefix)/php5/bin
	gsed -i -e s,PHPEXTDIR,$(shell $(DESTDIR)$(prefix)/php5/bin/php-config --extension-dir), $(WORKDIR)/php.ini.CSW
	ginstall -m 0644 \
		$(WORKDIR)/php.ini.CSW \
		$(DESTDIR)$(prefix)/php5/lib
	ginstall -m 0644 \
		$(WORKDIR)/pear.conf.CSW \
		$(DESTDIR)$(prefix)/php5/etc
	@(grm -fr $(DESTDIR)/.[a-z]*)
	@(gfind $(PHP5ROOT)/lib -name "*.a" -exec grm {} \;)
	@( echo "  ==> Now Building mod_php5 <==" )
	@( if [ -f $(WORKSRC)/Makefile ]; then \
		$(BUILD_ENV) gmake -C $(WORKSRC) distclean; fi)
	cd $(WORKSRC) && $(BUILD_ENV) ./configure $(NEW_CONFIGURE_ARGS)
	@( $(BUILD_ENV) $(INSTALL_ENV) gmake -C $(WORKSRC) install-sapi )
	@( strip $(DESTDIR)$(prefix)/apache/libexec/libphp5.so )
	@( gfind $(DESTDIR)$(prefix)/apache*  \
			-mindepth 1 -type d | grep -v libexec | xargs grm -fr )
	@$(MAKECOOKIE)

post-configure-modulated:
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)

EXTFILES = $(shell find extensions/*/files/* -prune -type f)
pre-fetch:
	$(foreach F,$(EXTFILES),$(shell cp $(F) $(DOWNLOADDIR)))

# System Rules/Configuration
include gar/category.mk
