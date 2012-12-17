NAME     = php5
VERSION  = 5.3.19
GARTYPE = v2
SF_PROJECT  = $(shell echo $(NAME) | sed -e 's/[0-9]//g')
DISTNAME    = $(SF_PROJECT)-$(VERSION)

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

EXTRA_MODULATORS = SAPI
MODULATIONS_SAPI = cgi ap2
MERGE_SCRIPTS_isa-default-sapi-cgi = copy-all
MERGE_SCRIPTS_isa-default-sapi-ap2 = copy-all

# turn on the build scripts to enable/disable modules
PHP5_EXT = 1
AP2_MODS = 1
AP2_MODFILES = *libphp5.so

# at least for a decent echo used during build.
PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)

VENDOR_URL     = http://www.php.net/
MASTER_SITES   = http://us.php.net/distributions/
EXTRA_INSTALL_ENV   = INSTALL_ROOT=$(DESTDIR)

LICENSE = LICENSE

DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += phpext pear.conf.CSW CSWphp5.postinstall
DISTFILES += CSWphp5.cswreleasenotes
DISTFILES += CSWap2-modphp5.cswreleasenotes
DISTFILES += CSWap2-modphp5.postinstall
DISTFILES += CSWap2-modphp5.preremove
DISTFILES += httpd-php5.conf

PATCHFILES += 0001-Strip-usr-ucblib-references.patch

BUILD_DEP_PKGS += CSWlibgdbm-dev CSWlibidn-dev CSWlibgd-dev CSWcoreutils
BUILD_DEP_PKGS += CSWlibxml2-dev CSWlibexpat1 CSWlibz-dev CSWlibcurl-dev CSWjpeg
BUILD_DEP_PKGS += CSWlibpng-dev CSWt1lib CSWlibgdbm-dev CSWlibgmp10
BUILD_DEP_PKGS += CSWggettext-dev CSWlibssl-dev CSWlibgd2 CSWbdb42devel
BUILD_DEP_PKGS += CSWlibcares-dev CSWftype2 CSWlibiconv-dev CSWlibc-client-dev
BUILD_DEP_PKGS += CSWopenldap-dev CSWlibkrb5-dev CSWsasl CSWlibltdl7
BUILD_DEP_PKGS += CSWmcrypt-dev CSWfreetds CSWmysql-dev CSWunixodbc
BUILD_DEP_PKGS += CSWlibreadline-dev CSWlibncurses-dev CSWnetsnmp-dev
BUILD_DEP_PKGS += CSWlibsqlite3-dev CSWaspell CSWtidy-dev CSWpostgresql-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibxpm-dev
BUILD_DEP_PKGS += CSWlibsqlite3-0
BUILD_DEP_PKGS += CSWlibaspell-dev

PRESERVECONF = $(sysconfdir)/php.ini $(sysconfdir)/pear.conf
PRESERVECONF += /opt/csw/apache2/etc/extra/httpd-php5.conf
MIGRATE_FILES_CSWphp5 = "php.ini"
MIGRATE_SOURCE_DIR_CSWphp5 = /opt/csw/php5/lib
MIGRATE_DEST_DIR = $(sysconfdir)

define php5_subpackage
PACKAGES += CSWphp5-$(1)
CATALOGNAME_CSWphp5-$(1) ?= php5_$(1)
SPKG_DESC_CSWphp5-$(1) ?= The $(1) extention for PHP5
RUNTIME_DEP_PKGS_CSWphp5-$(1) ?= CSWphp5 $(2)
OBSOLETED_BY_CSWphp5-$(1) ?= CSWphp5$(1)
PKGFILES_CSWphp5-$(1) ?= .*lib/php/extensions/.*/$(1).so .*php5/extensions/$(1)
CHECKPKG_OVERRIDES_CSWphp5-$(1) += surplus-dependency|CSWphp5
endef

PACKAGES = CSWphp5
CATALOGNAME_CSWphp5        = php5
SPKG_DESC_CSWphp5          = A High-Level Scripting Language
RUNTIME_DEP_PKGS_CSWphp5 += CSWlibxml2-2 CSWlibexpat1 CSWlibz1
RUNTIME_DEP_PKGS_CSWphp5 += CSWlibicui18n49
RUNTIME_DEP_PKGS_CSWphp5 += CSWlibicuuc49
INCOMPATIBLE_PKGS_CSWphp5 = CSWphp5mimemagic CSWphp5mhash CSWphp5dbase
INCOMPATIBLE_PKGS_CSWphp5 += CSWphp5ncurses CSWmodphp5
# embeded 'magic' information to detect file types...odd, but...
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/bin/php
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/PEAR/Config.php
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/bin/php-cgi
# verify these...
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/etc/opt/csw/php5/php.ini.CSW

CHECKPKG_OVERRIDES_CSWphp5 += file-collision|/opt/csw/php5/include/php/ext/sqlite3/libsqlite/sqlite3.h|CSWphp5|CSWphp5-sqlite

PACKAGES += CSWphp5-dev
CATALOGNAME_CSWphp5-dev   = php5_dev
SPKG_DESC_CSWphp5-dev     = Development files for php5
RUNTIME_DEP_PKGS_CSWphp5-dev      = CSWphp5
OBSOLETED_BY_CSWphp5-dev = CSWphp5devel
PKGFILES_CSWphp5-dev  = $(prefix)/php5/bin/php-config
PKGFILES_CSWphp5-dev  = $(prefix)/bin/php-config
PKGFILES_CSWphp5-dev += $(prefix)/php5/bin/phpize
PKGFILES_CSWphp5-dev += $(prefix)/php5/bin/peardev
PKGFILES_CSWphp5-dev += $(prefix)/bin/peardev
PKGFILES_CSWphp5-dev += $(prefix)/php5/lib/php/build/.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/TSRM.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/Zend.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/include.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/main.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/regex.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/ext/date.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/ext/filter.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/ext/libxml.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/ext/pcre.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/ext/spl.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/ext/standard.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/include/php/ext/xml.*
PKGFILES_CSWphp5-dev += $(prefix)/php5/man/man1/php-config.1
PKGFILES_CSWphp5-dev += $(prefix)/php5/man/man1/phpize.1
CHECKPKG_OVERRIDES_CSWphp5-dev += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-dev += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/libtool.m4
CHECKPKG_OVERRIDES_CSWphp5-dev += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/acinclude.m4
CHECKPKG_OVERRIDES_CSWphp5-dev += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/shtool
CHECKPKG_OVERRIDES_CSWphp5-dev += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/phpize.m4
CHECKPKG_OVERRIDES_CSWphp5-dev += file-with-bad-content|/usr/local|root/opt/csw/php5/man/man1/php-config.1

PACKAGES += CSWap2-modphp5
CATALOGNAME_CSWap2-modphp5 = ap2_modphp5
SPKG_DESC_CSWap2-modphp5 = The apache 2.2.x php5 module
RUNTIME_DEP_PKGS_CSWap2-modphp5  = CSWphp5 CSWapache2 CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWap2-modphp5 += CSWlibexpat1 CSWlibz1
RUNTIME_DEP_PKGS_CSWap2-modphp5 += CSWlibicui18n49
RUNTIME_DEP_PKGS_CSWap2-modphp5 += CSWlibicuuc49
OBSOLETED_BY_CSWap2-modphp5 = CSWap2modphp5
PKGFILES_CSWap2-modphp5 += $(prefix)/apache2.*
CHECKPKG_OVERRIDES_CSWap2-modphp5 += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWap2-modphp5 += file-with-bad-content|/usr/local|root/opt/csw/apache2/libexec/libphp5.so

$(eval $(call php5_subpackage,bcmath,))
$(eval $(call php5_subpackage,bz2,CSWlibbz2-1-0))
$(eval $(call php5_subpackage,calendar,))
$(eval $(call php5_subpackage,ctype,))
$(eval $(call php5_subpackage,curl,CSWlibcurl4))
$(eval $(call php5_subpackage,dba,CSWlibgdbm4 CSWbdb42))
$(eval $(call php5_subpackage,dom,CSWlibxml2-2))
PKGFILES_CSWphp5-dom += .*include/php/ext/dom.*
$(eval $(call php5_subpackage,exif,))
$(eval $(call php5_subpackage,ftp,CSWlibssl1-0-0))
$(eval $(call php5_subpackage,gd,CSWlibgd2 CSWlibt1-5))
PKGFILES_CSWphp5-gd += .*/include/php/ext/gd.*
$(eval $(call php5_subpackage,gettext,CSWlibintl8))
$(eval $(call php5_subpackage,gmp,CSWlibgmp10))
$(eval $(call php5_subpackage,hash,))
PKGFILES_CSWphp5-hash += .*/include/php/ext/hash.*
$(eval $(call php5_subpackage,iconv,CSWlibiconv2))
PKGFILES_CSWphp5-iconv += .*/include/php/ext/iconv.*
$(eval $(call php5_subpackage,imap,CSWlibc-client2007f))
$(eval $(call php5_subpackage,json,))
$(eval $(call php5_subpackage,ldap,CSWliblber2-4-2 CSWlibldap2-4-2))
$(eval $(call php5_subpackage,mbstring,))
PKGFILES_CSWphp5-mbstring += .*/include/php/ext/mbstring.*
$(eval $(call php5_subpackage,mcrypt,CSWlibmcrypt4))
$(eval $(call php5_subpackage,mssql,CSWlibsybdb5))
$(eval $(call php5_subpackage,mysql,CSWlibmysqlclient18 CSWlibssl1-0-0))
# likely a checkpkg glitch (uses sparcv8plus+vis path for the library)
CHECKPKG_OVERRIDES_CSWphp5-mysql += surplus-dependency|CSWlibssl1-0-0
$(eval $(call php5_subpackage,mysqli,CSWlibmysqlclient18))
$(eval $(call php5_subpackage,odbc,CSWlibodbc2))
$(eval $(call php5_subpackage,openssl,CSWlibssl1-0-0))
$(eval $(call php5_subpackage,pcntl,))
$(eval $(call php5_subpackage,pdo,))
PKGFILES_CSWphp5-pdo += .*/include/php/ext/pdo.*
$(eval $(call php5_subpackage,pdomysql,CSWlibmysqlclient18 CSWphp5-pdo))
PKGFILES_CSWphp5-pdomysql += .*/lib/php/extensions/.*/pdo_mysql.so
PKGFILES_CSWphp5-pdomysql += .*extensions/pdo_mysql
CHECKPKG_OVERRIDES_CSWphp5-pdomysql += surplus-dependency|CSWphp5-pdo
CHECKPKG_OVERRIDES_CSWphp5-pdomysql += surplus-dependency|CSWphp5
$(eval $(call php5_subpackage,pdoodbc,CSWlibodbc2 CSWphp5-pdo))
PKGFILES_CSWphp5-pdoodbc += .*/lib/php/extensions/.*/pdo_odbc.so
PKGFILES_CSWphp5-pdoodbc += .*extensions/pdo_odbc
CHECKPKG_OVERRIDES_CSWphp5-pdoodbc += surplus-dependency|CSWphp5-pdo
CHECKPKG_OVERRIDES_CSWphp5-pdoodbc += surplus-dependency|CSWphp5
$(eval $(call php5_subpackage,pdopgsql,CSWlibpq5 CSWphp5-pdo))
PKGFILES_CSWphp5-pdopgsql += .*/lib/php/extensions/.*/pdo_pgsql.so
PKGFILES_CSWphp5-pdopgsql += .*extensions/pdo_pgsql
CHECKPKG_OVERRIDES_CSWphp5-pdopgsql += surplus-dependency|CSWphp5-pdo
CHECKPKG_OVERRIDES_CSWphp5-pdopgsql += surplus-dependency|CSWphp5
$(eval $(call php5_subpackage,pdosqlite,CSWphp5-pdo))
PKGFILES_CSWphp5-pdosqlite += .*/lib/php/extensions/.*/pdo_sqlite.so
PKGFILES_CSWphp5-pdosqlite += .*extensions/pdo_sqlite
CHECKPKG_OVERRIDES_CSWphp5-pdosqlite += surplus-dependency|CSWphp5-pdo
CHECKPKG_OVERRIDES_CSWphp5-pdosqlite += surplus-dependency|CSWphp5
$(eval $(call php5_subpackage,pgsql,CSWlibpq5))
$(eval $(call php5_subpackage,posix,))
$(eval $(call php5_subpackage,pspell,CSWlibaspell15))
$(eval $(call php5_subpackage,readline,CSWlibreadline6))
$(eval $(call php5_subpackage,session,CSWlibmm))
PKGFILES_CSWphp5-session += .*/include/php/ext/session.*
$(eval $(call php5_subpackage,shmop,))
$(eval $(call php5_subpackage,snmp,CSWlibnetsnmp25))
$(eval $(call php5_subpackage,soap,CSWlibxml2-2))
$(eval $(call php5_subpackage,sockets,))
$(eval $(call php5_subpackage,sysvmsg,))
$(eval $(call php5_subpackage,sysvsem,))
$(eval $(call php5_subpackage,sysvshm,))
$(eval $(call php5_subpackage,tidy,CSWlibtidy0-99))
$(eval $(call php5_subpackage,tokenizer,))
$(eval $(call php5_subpackage,wddx,))
$(eval $(call php5_subpackage,xmlreader,CSWlibxml2-2))
$(eval $(call php5_subpackage,xmlrpc,CSWlibiconv2 CSWlibexpat1))
$(eval $(call php5_subpackage,xmlwriter,CSWlibxml2-2))
$(eval $(call php5_subpackage,xsl,CSWlibxml2-2 CSWlibxslt1 CSWlibexslt0))
$(eval $(call php5_subpackage,zip,CSWlibz1))

EXTRA_CFLAGS = -I$(prefix)/include/ncursesw
EXTRA_LIB = /opt/csw/postgresql/lib

# We link with /usr/ccs/bin/ld which requires setting the path to libCstd.so,
# using CC as linker would have made this automatic.
SUBDIR64-sparc = v9
SUBDIR64-i386 = amd64
EXTRA_LINKER_FLAGS = -L$($(GARCOMPILER)_CC_HOME)/lib/$(SUBDIR$(MEMORYMODEL)-$(GARCH)) -lCstd -lz

NOISALIST = 1
STRIP_LIBTOOL = 1

sysconfdir = /etc$(prefix)/php5

CONFIGURE_ARGS += --prefix=$(prefix)/php5
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)
## build this static, php can not run without it.
## it is more efficient to have this built into the php binary
CONFIGURE_ARGS += --enable-simplexml
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-xml
CONFIGURE_ARGS += --enable-intl
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-config-file-path=$(sysconfdir)
CONFIGURE_ARGS += --with-config-file-scan-dir=$(sysconfdir)/conf.d
CONFIGURE_ARGS += --enable-bcmath=shared
CONFIGURE_ARGS += --enable-calendar=shared
CONFIGURE_ARGS += --enable-ctype=shared
CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --enable-dom=shared
CONFIGURE_ARGS += --enable-exif=shared
CONFIGURE_ARGS += --enable-filter=shared
CONFIGURE_ARGS += --enable-ftp=shared
CONFIGURE_ARGS += --enable-gd-jis-conv
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-hash=shared
CONFIGURE_ARGS += --enable-json=shared
CONFIGURE_ARGS += --enable-magic-quotes
CONFIGURE_ARGS += --enable-mbstring=shared
CONFIGURE_ARGS += --enable-pcntl=shared
#CONFIGURE_ARGS += --enable-pdo=shared
CONFIGURE_ARGS += --enable-phar=shared
CONFIGURE_ARGS += --enable-posix=shared
CONFIGURE_ARGS += --enable-session=shared
CONFIGURE_ARGS += --enable-shmop=shared
CONFIGURE_ARGS += --enable-soap=shared
CONFIGURE_ARGS += --enable-sockets=shared
#CONFIGURE_ARGS += --enable-sqlite-utf8
CONFIGURE_ARGS += --enable-sysvmsg=shared
CONFIGURE_ARGS += --enable-sysvsem=shared
CONFIGURE_ARGS += --enable-sysvshm=shared
CONFIGURE_ARGS += --enable-tokenizer=shared
CONFIGURE_ARGS += --enable-wddx=shared
CONFIGURE_ARGS += --enable-xmlreader=shared
CONFIGURE_ARGS += --enable-xmlwriter=shared
CONFIGURE_ARGS += --enable-zip=shared
CONFIGURE_ARGS += --with-bz2=shared,$(prefix)
CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --with-curlwrappers
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb4
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/php5/bin
CONFIGURE_ARGS += --with-freetype-dir=$(prefix)
CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-gettext=shared,$(prefix)
CONFIGURE_ARGS += --with-gmp=shared,$(prefix)
CONFIGURE_ARGS += --with-iconv=shared,$(prefix)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)
CONFIGURE_ARGS += --with-imap=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-libedit=no
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)
CONFIGURE_ARGS += --with-mcrypt=shared,$(prefix)
CONFIGURE_ARGS += --with-mhash=shared,$(prefix)
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --with-mssql=shared,$(prefix)
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)
CONFIGURE_ARGS += --with-mysqli=shared,$(prefix)/bin/mysql_config
CONFIGURE_ARGS += --with-ndbm
CONFIGURE_ARGS += --with-openssl=shared,$(prefix)
CONFIGURE_ARGS += --with-pcre-dir=$(prefix)
CONFIGURE_ARGS += --with-pcre-regex
# not documented, but you can pass the path to mysql_config directly
# we need the 32-bit version, so we have to force this
CONFIGURE_ARGS += --with-pdo-mysql=shared,$(prefix)/bin/mysql_config
CONFIGURE_ARGS += --with-pdo-odbc=shared,unixODBC,$(prefix)
CONFIGURE_ARGS += --with-pdo-pgsql=shared,$(bindir)/
#CONFIGURE_ARGS += --with-pdo-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --with-pear=shared
CONFIGURE_ARGS += --with-pgsql=shared,$(bindir)/
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-pspell=shared,$(prefix)
CONFIGURE_ARGS += --with-readline=shared,/opt/csw
CONFIGURE_ARGS += --with-snmp=shared,$(prefix)
CONFIGURE_ARGS += --with-t1lib=$(prefix)
CONFIGURE_ARGS += --with-tidy=shared,$(prefix)
CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)
CONFIGURE_ARGS += --with-xmlrpc=shared
CONFIGURE_ARGS += --with-xpm-dir=$(prefix)
CONFIGURE_ARGS += --with-xsl=shared,$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --enable-cli

ifeq ($(SAPI),ap2)
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs
endif

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
#ENABLE_CHECK = 0
TEST_TARGET = test

include gar/category.mk

# they're using git now and ship a .gitignore that excludes aclocal.m4
# that broke one of our patches so we'll nuke .gitignore before we patch
pre-patch-modulated:
	@(cd $(WORKSRC); rm .gitignore; git add -A; git commit -m 'adding files that were previously ignored' )
	@$(MAKECOOKIE)

pre-configure-modulated:
	@echo Munging c-client routine in configure.
	@(cd $(WORKSRC); \
		perl -pi -e "s|c-client4 c-client|c-client.2007f|g" configure; \
		git add configure; git commit -m 'modify c-client finding routine')
	@$(MAKECOOKIE)

# this allows apxs to install the module.  stupid, but i couldn't make
# the darn thing _not_ do try to add the httpd.conf lines, even with
# patching...
pre-install-modulated: AP2SYSCONF=/opt/csw/apache2/etc
pre-install-modulated: $(PI_SCRIPTS)
	@(mkdir -p $(DESTDIR)$(AP2SYSCONF); \
		cp $(AP2SYSCONF)/httpd.conf $(DESTDIR)$(AP2SYSCONF) )
	@$(MAKECOOKIE)

post-install-modulated: AP2SYSCONF=/opt/csw/apache2/etc/httpd.conf
post-install-modulated: AP2EXTCONF=/opt/csw/apache2/etc/extra
post-install-modulated: INIDEST=$(DESTDIR)/etc$(prefix)/php5/php.ini
post-install-modulated:
	@rm -f $(DESTDIR)$(AP2SYSCONF)
	@mkdir -p $(DESTDIR)$(AP2EXTCONF)
	@cp $(WORKDIR)/httpd-php5.conf $(DESTDIR)$(AP2EXTCONF)
	@cp $(WORKSRC)/php.ini-production $(INIDEST)
	@ginstall -m 0755 $(DOWNLOADDIR)/phpext $(DESTDIR)$(prefix)/php5/bin/
	@perl -pi -e 's/^;extension=php_(.*).dll/;extension=$$1.so/' $(INIDEST)
	@rm -rf $(DESTDIR)/.cha* $(DESTDIR)/.dep* $(DESTDIR)/.reg* $(DESTDIR)/.l* $(DESTDIR)/.f*
	@perl -pi -e 's!s:17:"http://proxy:3128!s:0:"!' $(DESTDIR)$(sysconfdir)/pear.conf*
	@mkdir -p $(DESTDIR)/opt/csw/bin
	@( cd $(DESTDIR)/opt/csw/bin; \
	   for f in pear peardev pecl phar php php-config; do \
		ln -s ../php5/bin/$$f $$f; \
	   done )
	@$(MAKECOOKIE)

post-merge:
	@echo " ==> Killing phar"
	@(rm $(PKGROOT)/opt/csw/php5/extensions/phar)
	@echo " ==> Fixing php.ini: adding loadable session.so support"
	@( cd $(PKGROOT)/$(sysconfdir)/; \
		perl -pi -e 's/extension=bz2.so/extension=session.so\n;extension=bz2.so/' php.ini.CSW; )
	@( cd $(PKGROOT)/$(sysconfdir)/; \
		perl -pi -e 's/extension=bz2.so/extension=ctype.so\n;extension=bz2.so/' php.ini.CSW; )
	@echo " ==> Fixing php.ini: adding loadable ctype.so support"
	@$(MAKECOOKIE)
