GARNAME     = php5
GARVERSION  = 5.2.9
CATEGORIES  = lang
SF_PROJ     = $(shell echo $(GARNAME) | sed -e 's/[0-9]//g')
DISTNAME    = $(SF_PROJ)-$(GARVERSION)

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

MASTER_SITES   = http://us.php.net/distributions/
SPKG_SOURCEURL = http://www.php.net/downloads.php
INSTALL_ENV   += INSTALL_ROOT=$(DESTDIR)
STRIP_DIRS    += $(DESTDIR)$(prefix)/lib/php/extensions/*/

DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += php.ini.CSW phpext pear.conf.CSW
DISTFILES += CSWphp5_ext_enable.sh CSWphp5_ext_disable.sh
DISTFILES += CSWphp5.postinstall

PACKAGES = CSWphp5 CSWphp5devel
CATALOGNAME_CSWphp5        = php5
SPKG_DESC_CSWphp5          = A High-Level Scripting Languages
CATALOGNAME_CSWphp5devel   = php5_devel
SPKG_DESC_CSWphp5devel     = Development files for php5
REQUIRED_PKGS_CSWphp5      = CSWexpat CSWggettextrt CSWiconv 
REQUIRED_PKGS_CSWphp5     += CSWlibxml2 CSWzlib CSWmysql5rt
REQUIRED_PKGS_CSWphp5devel = CSWphp5

PKGFILES_CSWphp5devel  = $(bindir)/php-config
PKGFILES_CSWphp5devel += $(bindir)/phpize
PKGFILES_CSWphp5devel += $(bindir)/peardev
PKGFILES_CSWphp5devel += $(includedir)/.*
PKGFILES_CSWphp5devel += $(libdir)/php/build/.*
PKGFILES_CSWphp5devel += $(mandir)/.*

PATCHFILES += configure.diff
PATCHFILES += php-bug-45557-fix.diff

# PHP Extensions
EXTDIRLIST = $(shell ls -d extensions/*)
include $(foreach X,$(EXTDIRLIST),$(X)/Makefile)

EXTRA_LIB += $(prefix)/bdb44/lib
EXTRA_INC += $(prefix)/bdb44/include
EXTRA_CFLAGS = -I$(prefix)/include/ncursesw

NOISALIST = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/bin
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --enable-fastcgi
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --enable-magic-quotes
CONFIGURE_ARGS += --enable-spl=shared
CONFIGURE_ARGS += --with-pcre-regex
CONFIGURE_ARGS += --with-pear=shared

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
ENABLE_CHECK = 0

PI_SCRIPTS  = install-extras
PI_SCRIPTS += install-ap2modphp5
PI_SCRIPTS += install-modphp5
PI_SCRIPTS += install-cleanup

post-install-modulated: $(PI_SCRIPTS)
	@$(MAKECOOKIE)

install-extras:
	ginstall -m 0755 $(WORKDIR)/phpext $(DESTDIR)$(bindir)
	gsed -i -e s,PHPEXTDIR,$(shell $(DESTDIR)$(bindir)/php-config --extension-dir),\
		$(WORKDIR)/php.ini.CSW
	ginstall -m 0644 $(WORKDIR)/php.ini.CSW $(DESTDIR)$(libdir)
	ginstall -m 0644 $(WORKDIR)/pear.conf.CSW $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 $(WORKDIR)/httpd-php5.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc/extra
	@$(MAKECOOKIE)

install-ap2modphp5:
	@echo "  ==> Now Building ap2_modphp5 <=="
	@if [ -f $(WORKSRC)/Makefile ]; then \
		$(BUILD_ENV) gmake -C $(WORKSRC) distclean; fi
	cd $(WORKSRC) && $(BUILD_ENV) \
		./configure $(CONFIGURE_ARGS) --with-apxs2=$(prefix)/apache2/sbin/apxs
	@$(GARBIN)/fixlibtool $(WORKSRC)
	@$(BUILD_ENV) $(INSTALL_ENV) gmake -C $(WORKSRC) install-sapi
	@strip $(DESTDIR)$(prefix)/apache2/libexec/libphp5.so
	@$(MAKECOOKIE)

install-modphp5:
	@echo "  ==> Now Building mod_php5 <=="
	@if [ -f $(WORKSRC)/Makefile ]; then \
		$(BUILD_ENV) gmake -C $(WORKSRC) distclean; fi
	cd $(WORKSRC) && $(BUILD_ENV) \
		./configure $(CONFIGURE_ARGS) --with-apxs=$(prefix)/apache/bin/apxs
	@$(GARBIN)/fixlibtool $(WORKSRC)
	@$(BUILD_ENV) $(INSTALL_ENV) gmake -C $(WORKSRC) install-sapi
	@strip $(DESTDIR)$(prefix)/apache/libexec/libphp5.so
	@$(MAKECOOKIE)

install-cleanup:
	@gfind $(DESTDIR) -name \.[a-z]\* -exec grm -fr {} \;
	@gfind $(DESTDIR)/$(libdir) -name "*.a" -exec grm -f {} \;
	@grm -f $(DESTDIR)$(sysconfdir)/pear.conf
	@gfind $(DESTDIR)$(prefix)/apache*  \
		-mindepth 1 -type d | egrep -v "etc|libexec" | xargs grm -fr
	@$(MAKECOOKIE)

EXTFILES = $(shell find extensions/*/files/* -prune -type f)
pre-fetch:
	$(foreach F,$(EXTFILES),$(shell cp $(F) $(DOWNLOADDIR)))

post-merge-modulated:
	@echo "[====> Fixing Admin Scripts <====]"
	PHP_INI_FILE=`$(PKGROOT)$(bindir)/php -i | grep "Configuration File .* Path" | awk '{print $$NF}'`; \
	perl -i -pne "s|_PHPINIFILE_|$${PHP_INI_FILE}/php.ini|" `gfind $(DOWNLOADDIR) -type f -print`
	perl -i -pne "s|_PHPLIBDIR_|$(libdir)|" `gfind $(DOWNLOADDIR) -type f -print`
	perl -i -pne "s|_PHPBINDIR_|$(bindir)|" `gfind $(DOWNLOADDIR) -type f -print`
	#@$(MAKECOOKIE)
	
# System Rules/Configuration
include gar/category.mk
