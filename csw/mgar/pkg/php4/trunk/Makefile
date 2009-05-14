GARNAME    = php4
GARVERSION = 4.4.9
CATEGORIES = lang
SF_PROJ = $(shell echo $(GARNAME) | sed -e 's/[0-9]//g')

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
DISTFILES      = $(SF_PROJ)-$(GARVERSION).tar.bz2

INSTALL_ENV   += INSTALL_ROOT=$(DESTDIR)
PHP4ROOT       = $(DESTDIR)$(prefix)/php4
STRIP_DIRS    += $(PHP4ROOT)/lib/php/extensions/*/
STRIP_DIRS    += $(PHP4ROOT)/bin

PATCHFILES  = pgsql.diff
EXTRA_LIB += $(prefix)/bdb44/lib
EXTRA_INC += $(prefix)/bdb44/include
EXTRA_CFLAGS = -I$(prefix)/include/ncursesw

CONFIGURE_ARGS += --prefix=$(prefix)/php4
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/php4/bin
CONFIGURE_ARGS += --enable-bcmath=shared
CONFIGURE_ARGS += --enable-calendar=shared
CONFIGURE_ARGS += --enable-cgi
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --with-curlwrappers
CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --enable-exif
CONFIGURE_ARGS += --enable-fastcgi
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-mbregex=shared
CONFIGURE_ARGS += --enable-mbstring=shared
CONFIGURE_ARGS += --enable-sockets
CONFIGURE_ARGS += --with-bz2=shared,$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb44
CONFIGURE_ARGS += --with-dom-exslt=$(prefix)
CONFIGURE_ARGS += --with-dom-xslt=$(prefix)
CONFIGURE_ARGS += --with-dom=shared,$(prefix)
CONFIGURE_ARGS += --with-expat-dir=$(prefix)
CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-gettext=shared,$(prefix)
CONFIGURE_ARGS += --with-gmp=shared,$(prefix)
CONFIGURE_ARGS += --with-iconv=shared
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)
CONFIGURE_ARGS += --with-imap=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)
CONFIGURE_ARGS += --with-mcal=shared,$(prefix)
CONFIGURE_ARGS += --with-mssql=shared,$(prefix)
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)
CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)
CONFIGURE_ARGS += --with-openssl=shared,$(prefix)
CONFIGURE_ARGS += --with-pgsql=shared,$(prefix)/postgresql
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)
CONFIGURE_ARGS += --with-xmlrpc=shared,$(prefix)
CONFIGURE_ARGS += --with-zlib=shared

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
ENABLE_CHECK = 0

PI_SCRIPTS  = install-extra
PI_SCRIPTS += install-ap2modphp4
PI_SCRIPTS += install-modphp4
PI_SCRIPTS += install-cleanup

post-install-modulated: $(PI_SCRIPTS)
	@$(MAKECOOKIE)

install-ap2modphp4:
	@echo "  ==> Now Building ap2_modphp4 <=="
	@if [ -f $(WORKSRC)/Makefile ]; then \
		$(BUILD_ENV) gmake -C $(WORKSRC) distclean; fi
	@cd $(WORKSRC) && $(BUILD_ENV) \
		./configure $(CONFIGURE_ARGS) --with-apxs2=$(prefix)/apache2/sbin/apxs
	@$(GARBIN)/fixlibtool $(WORKSRC)
	@$(BUILD_ENV) $(INSTALL_ENV) gmake -C $(WORKSRC) install-sapi
	@strip $(DESTDIR)$(prefix)/apache2/libexec/libphp4.so
	@$(MAKECOOKIE)

install-modphp4:
	@echo "  ==> Now Building modphp4 <=="
	@if [ -f $(WORKSRC)/Makefile ]; then \
		$(BUILD_ENV) gmake -C $(WORKSRC) distclean; fi
	@cd $(WORKSRC) && $(BUILD_ENV) \
		./configure $(CONFIGURE_ARGS) --with-apxs=$(prefix)/apache/bin/apxs
	@$(GARBIN)/fixlibtool $(WORKSRC)
	@$(BUILD_ENV) $(INSTALL_ENV) gmake -C $(WORKSRC) install-sapi
	@strip $(DESTDIR)$(prefix)/apache/libexec/libphp4.so
	@$(MAKECOOKIE)

install-extra:
	@gmv $(DESTDIR)$(prefix)/php4/etc/pear.conf \
		$(DESTDIR)$(prefix)/php4/etc/pear.conf.CSW
	@gsed -i -e s,PHPEXTDIR,$(shell $(PHP4ROOT)/bin/php-config --extension-dir),\
			$(WORKDIR)/php.ini.CSW
	@ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	@ginstall -d $(DESTDIR)$(prefix)/apache/conf
	@ginstall -d $(DESTDIR)$(prefix)/php4/lib
	@ginstall -m 0644 $(WORKDIR)/README-mod_php4_core $(DESTDIR)$(prefix)/php4
	@ginstall -m 0644 $(WORKDIR)/README-mod_php $(DESTDIR)$(prefix)/php4
	@ginstall -m 0644 $(WORKDIR)/php.ini.CSW $(DESTDIR)$(prefix)/php4/lib
	@ginstall -m 0644 $(WORKDIR)/php.ini.CSW $(DESTDIR)$(prefix)/php4/lib
	@ginstall -m 0644 $(WORKDIR)/httpd-php4.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc/extra
	@gcp $(DOWNLOADDIR)/dummy-httpd.conf $(DESTDIR)$(prefix)/apache2/etc/httpd.conf
	@gcp $(DOWNLOADDIR)/dummy-httpd.conf $(DESTDIR)$(prefix)/apache/conf/httpd.conf
	@$(MAKECOOKIE)

install-cleanup:
	@grm -fr $(DESTDIR)/.[a-z]*
	@gfind $(DESTDIR) -name \*.a -exec grm -f {} \;
	@gfind $(DESTDIR)$(prefix)/apache*  \
		-mindepth 1 -type d | egrep -v "etc|libexec" | xargs grm -fr
	@grm $(DESTDIR)$(prefix)/apache2/etc/httpd.conf*
	@$(MAKECOOKIE)

include files/pkgdef.mk
include files/pkgfiles.mk
include files/admfiles.mk
include gar/category.mk
