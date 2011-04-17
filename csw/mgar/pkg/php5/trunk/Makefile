NAME     = php5
VERSION  = 5.3.6
CATEGORIES  = lang
SF_PROJ     = $(shell echo $(NAME) | sed -e 's/[0-9]//g')
DISTNAME    = $(SF_PROJ)-$(VERSION)

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

# turn on the build scripts to enable/disable modules
PHP5_EXT = 1

# at least for a decent echo used during build.
PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)

VENDOR_URL     = http://www.php.net/
MASTER_SITES   = http://us.php.net/distributions/
INSTALL_ENV   += INSTALL_ROOT=$(DESTDIR)
#STRIP_DIRS    := $(shell $(call _get_php_prefix,$(DESTDIR))/bin/php-config --extension-dir)/*/

LICENSE = LICENSE

DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += phpext pear.conf.CSW CSWphp5.postinstall
DISTFILES += CSWphp5.cswreleasenotes

PATCHFILES += 0001-Strip-usr-ucblib-references.patch
# this one is filed upstream: http://bugs.php.net/bug.php?id=54318
PATCHFILES += 0002-Correct-non-portable-use-of-grep-q-in-configure.patch

define php5_subpackage
PACKAGES += CSWphp5-$(1)
CATALOGNAME_CSWphp5-$(1) ?= php5_$(1)
SPKG_DESC_CSWphp5-$(1) ?= The $(1) extention for PHP5
RUNTIME_DEP_PKGS_CSWphp5-$(1) ?= CSWphp5 $(2)
OBSOLETED_BY_CSWphp5-$(1) ?= CSWphp5$(1)
PKGFILES_CSWphp5-$(1) ?= .*lib/php/extensions/.*/$(1).so .*php5/extensions/$(1)
CHECKPKG_OVERRIDES_CSWphp5-$(1) += surplus-dependency|CSWphp5
endef

PACKAGES = CSWphp5 CSWphp5-dev
PACKAGES += CSWap2-modphp5

$(eval $(call php5_subpackage,bcmath))
$(eval $(call php5_subpackage,bz2,CSWbzip2))
$(eval $(call php5_subpackage,calendar))
$(eval $(call php5_subpackage,ctype))
$(eval $(call php5_subpackage,curl,CSWcurlrt CSWlibidn11 CSWoldaprt CSWosslrt CSWzlib CSWlibcares))
$(eval $(call php5_subpackage,dba,CSWlibgdbm3 CSWbdb42))
$(eval $(call php5_subpackage,dom,CSWiconv CSWlibxml2 CSWzlib))
PKGFILES_CSWphp5-dom += .*include/php/ext/dom.*
$(eval $(call php5_subpackage,exif))
$(eval $(call php5_subpackage,ftp,CSWosslrt))
$(eval $(call php5_subpackage,gd,CSWftype2 CSWlibgd2 CSWjpeg CSWpng CSWt1lib CSWxpm CSWzlib))
PKGFILES_CSWphp5-gd += .*/include/php/ext/gd.*
$(eval $(call php5_subpackage,gettext,CSWlibintl8))
$(eval $(call php5_subpackage,gmp,CSWlibgmp))
$(eval $(call php5_subpackage,hash))
PKGFILES_CSWphp5-hash += .*/include/php/ext/hash.*
$(eval $(call php5_subpackage,iconv,CSWiconv))
PKGFILES_CSWphp5-iconv += .*/include/php/ext/iconv.*
$(eval $(call php5_subpackage,imap,CSWimaprt CSWkrb5lib CSWosslrt))
$(eval $(call php5_subpackage,json))
$(eval $(call php5_subpackage,ldap,CSWoldaprt CSWsasl))
$(eval $(call php5_subpackage,mbstring))
PKGFILES_CSWphp5-mbstring += .*/include/php/ext/mbstring.*
$(eval $(call php5_subpackage,mcrypt,CSWlibmcrypt CSWlibltdl7))
$(eval $(call php5_subpackage,mssql,CSWfreetds))
$(eval $(call php5_subpackage,mysql,CSWmysql5rt))
$(eval $(call php5_subpackage,mysqli,CSWmysql5rt CSWzlib))
$(eval $(call php5_subpackage,odbc,CSWunixodbc))
$(eval $(call php5_subpackage,openssl,CSWosslrt CSWkrb5lib))
$(eval $(call php5_subpackage,pcntl))
$(eval $(call php5_subpackage,pdo))
PKGFILES_CSWphp5-pdo += .*/include/php/ext/pdo.*
$(eval $(call php5_subpackage,pdomysql,CSWmysql5rt CSWzlib CSWphp5-pdo))
PKGFILES_CSWphp5-pdopgsql = .*/lib/php/extensions/.*/pdo_mysql.so
CHECKPKG_OVERRIDES_CSWphp5-pdomysql += surplus-dependency|CSWphp5-pdo
$(eval $(call php5_subpackage,pdoodbc,CSWunixodbc CSWphp5-pdo))
PKGFILES_CSWphp5-pdoodbc = .*/lib/php/extensions/.*/pdo_odbc.so
CHECKPKG_OVERRIDES_CSWphp5-pdoodbc += surplus-dependency|CSWphp5-pdo
$(eval $(call php5_subpackage,pdopgsql,CSWlibpq CSWphp5-pdo))
PKGFILES_CSWphp5-pdopgsql = .*/lib/php/extensions/.*/pdo_pgsql.so
CHECKPKG_OVERRIDES_CSWphp5-pdoodbc += surplus-dependency|CSWphp5-pdo
$(eval $(call php5_subpackage,pdosqlite,CSWsqlite3rt CSWphp5-pdo))
PKGFILES_CSWphp5-pdosqlite = .*/lib/php/extensions/.*/pdo_sqlite.so
CHECKPKG_OVERRIDES_CSWphp5-pdosqlite += surplus-dependency|CSWphp5-pdo
$(eval $(call php5_subpackage,pgsql,CSWlibpq))
$(eval $(call php5_subpackage,posix))
$(eval $(call php5_subpackage,pspell,CSWaspell))
$(eval $(call php5_subpackage,readline,CSWreadline CSWncurses))
$(eval $(call php5_subpackage,session,CSWlibmm))
PKGFILES_CSWphp5-session += .*/include/php/ext/session.*
$(eval $(call php5_subpackage,shmop))
$(eval $(call php5_subpackage,snmp,CSWnetsnmp))
$(eval $(call php5_subpackage,soap,CSWiconv CSWlibxml2 CSWzlib))
$(eval $(call php5_subpackage,sockets))
$(eval $(call php5_subpackage,sqlite,CSWsqlite))
PKGFILES_CSWphp5-sqlite += .*/include/php/ext/sqlite.*
$(eval $(call php5_subpackage,sysvmsg))
$(eval $(call php5_subpackage,sysvsem))
$(eval $(call php5_subpackage,sysvshm))
$(eval $(call php5_subpackage,tidy,CSWhtmltidy))
$(eval $(call php5_subpackage,tokenizer))
$(eval $(call php5_subpackage,wddx))
$(eval $(call php5_subpackage,xmlreader,CSWiconv CSWlibxml2 CSWzlib))
$(eval $(call php5_subpackage,xmlrpc,CSWiconv CSWexpat))
$(eval $(call php5_subpackage,xmlwriter,CSWiconv CSWlibxml2 CSWzlib))
$(eval $(call php5_subpackage,xsl,CSWiconv CSWlibxml2 CSWlibxslt CSWzlib))
$(eval $(call php5_subpackage,zip,CSWzlib))

BUILD_DEP_PKGS += CSWlibgdbm-dev CSWlibidn-dev CSWlibgd-dev CSWcoreutils

CATALOGNAME_CSWphp5        = php5
SPKG_DESC_CSWphp5          = A High-Level Scripting Language
RUNTIME_DEP_PKGS_CSWphp5 += CSWlibxml2 CSWiconv CSWexpat CSWzlib
INCOMPATIBLE_PKGS_CSWphp5 = CSWphp5mimemagic CSWphp5mhash CSWphp5dbase
INCOMPATIBLE_PKGS_CSWphp5 += CSWphp5ncurses CSWmodphp5

# embeded 'magic' information to detect file types...odd, but...
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/bin/php
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/libtool.m4
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/acinclude.m4
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/shtool
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/build/phpize.m4
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php/PEAR/Config.php
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/man/man1/php-config.1
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/bin/php-cgi
# verify these...
CHECKPKG_OVERRIDES_CSWphp5 += file-with-bad-content|/usr/local|root/opt/csw/php5/lib/php.ini.CSW


# end verify...

CATALOGNAME_CSWphp5-dev   = php5_dev
SPKG_DESC_CSWphp5-dev     = Development files for php5
RUNTIME_DEP_PKGS_CSWphp5-dev      = CSWphp5
OBSOLETED_BY_CSWphp5-dev = CSWphp5devel

CATALOGNAME_CSWap2-modphp5 = ap2_modphp5
SPKG_DESC_CSWap2-modphp5 = The apache 2.2.x php5 module
RUNTIME_DEP_PKGS_CSWap2-modphp5  = CSWphp5 CSWapache2 CSWlibxml2 CSWiconv
RUNTIME_DEP_PKGS_CSWap2-modphp5 += CSWexpat CSWzlib
OBSOLETED_BY_CSWap2-modphp5 = CSWap2modphp5

PKGFILES_CSWphp5-dev  = $(bindir)/php-config
PKGFILES_CSWphp5-dev += $(bindir)/phpize
PKGFILES_CSWphp5-dev += $(bindir)/peardev
PKGFILES_CSWphp5-dev += $(libdir)/php/build/.*
PKGFILES_CSWphp5-dev += $(includedir)/php/TSRM.*
PKGFILES_CSWphp5-dev += $(includedir)/php/Zend.*
PKGFILES_CSWphp5-dev += $(includedir)/php/include.*
PKGFILES_CSWphp5-dev += $(includedir)/php/main.*
PKGFILES_CSWphp5-dev += $(includedir)/php/regex.*
PKGFILES_CSWphp5-dev += $(includedir)/php/ext/date.*
PKGFILES_CSWphp5-dev += $(includedir)/php/ext/filter.*
PKGFILES_CSWphp5-dev += $(includedir)/php/ext/libxml.*
PKGFILES_CSWphp5-dev += $(includedir)/php/ext/pcre.*
PKGFILES_CSWphp5-dev += $(includedir)/php/ext/spl.*
PKGFILES_CSWphp5-dev += $(includedir)/php/ext/standard.*
PKGFILES_CSWphp5-dev += $(includedir)/php/ext/xml.*
PKGFILES_CSWphp5-dev += $(mandir)/man1/php-config.1
PKGFILES_CSWphp5-dev += $(mandir)/man1/phpize.1

PKGFILES_CSWap2-modphp5 += $(prefix)/apache2.*

# PATCHFILES += configure.diff
# PATCHFILES += odbc.diff
# PATCHFILES += pdopgsql.diff
# PATCHFILES += pgsql.diff

# PHP Extensions, currently deactivated
#
# GAR needs performance enhancements to handle an integrated build with
# all the extensions otherwise the build takes ages.
# 1) File downloads are triggered via gmake invocations -> s l o w !!
# 2) Unless gmake is called -r there are heaps of implicit rule searches
#      for the included Makefiles (gmake tries to remake them)
# 3) ... TBD, probably more
#
EXTENSION_MAKEFILES := $(wildcard extensions/*/Makefile)
#include $(EXTENSION_MAKEFILES)

EXTRA_CFLAGS = -I$(prefix)/include/ncursesw

#LIBS += -lrt -lintl 

NOISALIST = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS += --prefix=$(prefix)/php5
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/php5/bin
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --enable-magic-quotes
CONFIGURE_ARGS += --with-pcre-regex
CONFIGURE_ARGS += --with-pear=shared
CONFIGURE_ARGS += --with-pear=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --enable-bcmath=shared
CONFIGURE_ARGS += --with-bz2=shared,$(prefix)
CONFIGURE_ARGS += --enable-calendar=shared
CONFIGURE_ARGS += --enable-ctype=shared
CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --with-curlwrappers
CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --with-ndbm
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb4
CONFIGURE_ARGS += --enable-dom=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --enable-exif=shared
CONFIGURE_ARGS += --enable-filter=shared
CONFIGURE_ARGS += --with-pcre-dir=$(prefix)
CONFIGURE_ARGS += --enable-ftp=shared
CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-xpm-dir=$(prefix)
CONFIGURE_ARGS += --with-freetype-dir=$(prefix)
CONFIGURE_ARGS += --with-t1lib=$(prefix)
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-gd-jis-conv
CONFIGURE_ARGS += --with-gettext=shared,$(prefix)
CONFIGURE_ARGS += --with-gmp=shared,$(prefix)
CONFIGURE_ARGS += --enable-hash=shared
CONFIGURE_ARGS += --with-iconv=shared,$(prefix)
CONFIGURE_ARGS += --with-imap=shared,$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)
CONFIGURE_ARGS += --enable-json=shared
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)
CONFIGURE_ARGS += --enable-mbstring=shared
CONFIGURE_ARGS += --enable-mbregex=shared
CONFIGURE_ARGS += --with-mcrypt=shared,$(prefix)
CONFIGURE_ARGS += --with-mhash=shared,$(prefix)
CONFIGURE_ARGS += --enable-phar=shared
CONFIGURE_ARGS += --with-mssql=shared,$(prefix)
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)/mysql5
CONFIGURE_ARGS += --with-mysqli=shared,$(prefix)/mysql5/bin/$(ISA_DEFAULT)/mysql_config
CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)
CONFIGURE_ARGS += --with-openssl=shared,$(prefix)
CONFIGURE_ARGS += --enable-pcntl=shared
CONFIGURE_ARGS += --enable-pdo=shared
# not documented, but you can pass the path to mysql_config directly
# we need the 32-bit version, so we have to force this
CONFIGURE_ARGS += --with-pdo-mysql=shared,$(prefix)/mysql5/bin/$(ISA_DEFAULT)/mysql_config
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-pdo-odbc=shared,unixODBC,$(prefix)
CONFIGURE_ARGS += --with-pdo-pgsql=shared,$(prefix)/postgresql
CONFIGURE_ARGS += --with-pdo-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --with-pgsql=shared,$(prefix)/postgresql
CONFIGURE_ARGS += --enable-posix=shared
CONFIGURE_ARGS += --with-pspell=shared,$(prefix)
CONFIGURE_ARGS += --with-libedit=no
CONFIGURE_ARGS += --with-readline=shared,/opt/csw
CONFIGURE_ARGS += --enable-session=shared
CONFIGURE_ARGS += --enable-shmop=shared
## build this static, php can not run without it.
## it is more efficient to have this built into the php binary
CONFIGURE_ARGS += --enable-simplexml
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
##
CONFIGURE_ARGS += --with-snmp=shared,$(prefix)
CONFIGURE_ARGS += --enable-soap=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --enable-sockets=shared
CONFIGURE_ARGS += --with-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --enable-sqlite-utf8
CONFIGURE_ARGS += --enable-sysvmsg=shared
CONFIGURE_ARGS += --enable-sysvsem=shared
CONFIGURE_ARGS += --enable-sysvshm=shared
CONFIGURE_ARGS += --with-tidy=shared,$(prefix)
CONFIGURE_ARGS += --enable-tokenizer=shared
CONFIGURE_ARGS += --enable-wddx=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)
CONFIGURE_ARGS += --enable-xml
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)
CONFIGURE_ARGS += --enable-xmlreader=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-xmlrpc=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)
CONFIGURE_ARGS += --enable-xmlwriter=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-xsl=shared,$(prefix)
CONFIGURE_ARGS += --enable-zip=shared
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
#ENABLE_CHECK = 0

CHECKPKG_OVERRIDES_CSWphp5-dev += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWap2-modphp5 += surplus-dependency|CSWphp5

include gar/category.mk

# this allows apxs to install the module.  stupid, but i couldn't make
# the darn thing _not_ do try to add the httpd.conf lines, even with
# patching...
pre-install-modulated: AP2SYSCONF=/opt/csw/apache2/etc
pre-install-modulated: $(PI_SCRIPTS)
	@(mkdir -p $(DESTDIR)$(AP2SYSCONF); \
		cp $(AP2SYSCONF)/httpd.conf $(DESTDIR)$(AP2SYSCONF) )
	@$(MAKECOOKIE)

post-install-modulated: AP2SYSCONF=/opt/csw/apache2/etc/httpd.conf
post-install-modulated: INIDEST=$(DESTDIR)$(prefix)/php5/lib/php.ini.CSW
post-install-modulated:
	@rm -f $(DESTDIR)$(AP2SYSCONF)
	@cp $(WORKSRC)/php.ini-production $(INIDEST)
	@ginstall -m 0755 $(DOWNLOADDIR)/phpext $(DESTDIR)$(prefix)/php5/bin/
	@perl -pi -e 's/^;extension=php_(.*).dll/;extension=$$1.so/' $(INIDEST)
	@$(MAKECOOKIE)

install-extras:
	gmv $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/etc/pear.conf $(DESTDIR)$(call _get_php_prefix,$(DESTDIR))/etc/pear.conf.CSW
	@$(MAKECOOKIE)

