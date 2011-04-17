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

PACKAGES += CSWphp5-exif
PACKAGES += CSWphp5-ftp
PACKAGES += CSWphp5-gd
PACKAGES += CSWphp5-gettext
PACKAGES += CSWphp5-gmp
PACKAGES += CSWphp5-hash
PACKAGES += CSWphp5-iconv
PACKAGES += CSWphp5-imap
PACKAGES += CSWphp5-json
PACKAGES += CSWphp5-ldap
PACKAGES += CSWphp5-mbstring
PACKAGES += CSWphp5-mcrypt
PACKAGES += CSWphp5-mssql
PACKAGES += CSWphp5-mysql
PACKAGES += CSWphp5-mysqli
PACKAGES += CSWphp5-odbc
PACKAGES += CSWphp5-openssl
PACKAGES += CSWphp5-pcntl
PACKAGES += CSWphp5-pdo
PACKAGES += CSWphp5-pdomysql
PACKAGES += CSWphp5-pdoodbc
PACKAGES += CSWphp5-pdopgsql
PACKAGES += CSWphp5-pdosqlite
PACKAGES += CSWphp5-pgsql
PACKAGES += CSWphp5-posix
PACKAGES += CSWphp5-pspell
PACKAGES += CSWphp5-readline
PACKAGES += CSWphp5-session
PACKAGES += CSWphp5-shmop
PACKAGES += CSWphp5-snmp
PACKAGES += CSWphp5-soap
PACKAGES += CSWphp5-sockets
PACKAGES += CSWphp5-sqlite
PACKAGES += CSWphp5-sysvmsg
PACKAGES += CSWphp5-sysvsem
PACKAGES += CSWphp5-sysvshm
PACKAGES += CSWphp5-tidy
PACKAGES += CSWphp5-tokenizer
PACKAGES += CSWphp5-wddx
PACKAGES += CSWphp5-xmlreader
PACKAGES += CSWphp5-xmlrpc
PACKAGES += CSWphp5-xmlwriter
PACKAGES += CSWphp5-xsl
PACKAGES += CSWphp5-zip

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

CATALOGNAME_CSWphp5-exif = php5_exif
SPKG_DESC_CSWphp5-exif = The exif extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-exif = CSWphp5
OBSOLETED_BY_CSWphp5-exif = CSWphp5exif

CATALOGNAME_CSWphp5-ftp = php5_ftp
SPKG_DESC_CSWphp5-ftp = The ftp extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-ftp = CSWphp5 CSWosslrt
OBSOLETED_BY_CSWphp5-ftp = CSWphp5ftp

CATALOGNAME_CSWphp5-gd = php5_gd
SPKG_DESC_CSWphp5-gd = The gd extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-gd  = CSWphp5 CSWftype2 CSWlibgd2 CSWjpeg
RUNTIME_DEP_PKGS_CSWphp5-gd += CSWpng CSWt1lib CSWxpm CSWzlib
OBSOLETED_BY_CSWphp5-gd = CSWphp5gd

CATALOGNAME_CSWphp5-gettext = php5_gettext
SPKG_DESC_CSWphp5-gettext = The gettext extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-gettext = CSWphp5 CSWlibintl8
OBSOLETED_BY_CSWphp5-gettext = CSWphp5gettext

CATALOGNAME_CSWphp5-gmp = php5_gmp
SPKG_DESC_CSWphp5-gmp = The gmp extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-gmp = CSWphp5 CSWlibgmp
OBSOLETED_BY_CSWphp5-gmp = CSWphp5gmp

CATALOGNAME_CSWphp5-hash = php5_hash
SPKG_DESC_CSWphp5-hash = The hash extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-hash = CSWphp5
OBSOLETED_BY_CSWphp5-hash = CSWphp5hash

CATALOGNAME_CSWphp5-iconv = php5_iconv
SPKG_DESC_CSWphp5-iconv = The iconv extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-iconv = CSWphp5 CSWiconv
OBSOLETED_BY_CSWphp5-iconv = CSWphp5iconv

CATALOGNAME_CSWphp5-imap = php5_imap
SPKG_DESC_CSWphp5-imap = The imap extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-imap = CSWphp5 CSWimaprt CSWkrb5lib CSWosslrt
OBSOLETED_BY_CSWphp5-imap = CSWphp5imap

CATALOGNAME_CSWphp5-json = php5_json
SPKG_DESC_CSWphp5-json = The json extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-json = CSWphp5
OBSOLETED_BY_CSWphp5-json = CSWphp5json

CATALOGNAME_CSWphp5-ldap = php5_ldap
SPKG_DESC_CSWphp5-ldap = The ldap extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-ldap = CSWphp5 CSWoldaprt CSWsasl

CATALOGNAME_CSWphp5-mbstring = php5_mbstring
SPKG_DESC_CSWphp5-mbstring = The mbstring extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-mbstring = CSWphp5
OBSOLETED_BY_CSWphp5-mbstring = CSWphp5mbstring

CATALOGNAME_CSWphp5-mcrypt = php5_mcrypt
SPKG_DESC_CSWphp5-mcrypt = The mcrypt extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-mcrypt = CSWphp5 CSWlibmcrypt CSWlibltdl7
OBSOLETED_BY_CSWphp5-mcrypt = CSWphp5mcrypt

CATALOGNAME_CSWphp5-mssql = php5_mssql
SPKG_DESC_CSWphp5-mssql = The mssql extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-mssql = CSWphp5 CSWfreetds
OBSOLETED_BY_CSWphp5-mssql = CSWphp5mssql

CATALOGNAME_CSWphp5-mysql = php5_mysql
SPKG_DESC_CSWphp5-mysql = The mysql extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-mysql = CSWphp5 CSWmysql5rt
OBSOLETED_BY_CSWphp5-mysql = CSWphp5mysql

CATALOGNAME_CSWphp5-mysqli = php5_mysqli
SPKG_DESC_CSWphp5-mysqli = The mysqli extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-mysqli = CSWphp5 CSWmysql5rt CSWzlib
OBSOLETED_BY_CSWphp5-mysqli = CSWphp5mysqli

CATALOGNAME_CSWphp5-odbc = php5_odbc
SPKG_DESC_CSWphp5-odbc = The odbc extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-odbc = CSWphp5 CSWunixodbc
OBSOLETED_BY_CSWPhp5-odbc = CSWphp5odbc

CATALOGNAME_CSWphp5-openssl = php5_openssl
SPKG_DESC_CSWphp5-openssl = The openssl extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-openssl = CSWphp5 CSWosslrt CSWkrb5lib
OBSOLETED_BY_CSWphp5-openssl = CSWphp5openssl

CATALOGNAME_CSWphp5-pcntl = php5_pcntl
SPKG_DESC_CSWphp5-pcntl = The pcntl extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-pcntl = CSWphp5
OBSOLETED_BY_CSWphp5-pcntl = CSWphp5pcntl

CATALOGNAME_CSWphp5-pdo = php5_pdo
SPKG_DESC_CSWphp5-pdo = A database access abstraction module for PHP applications
RUNTIME_DEP_PKGS_CSWphp5-pdo = CSWphp5 
OBSOLETED_BY_CSWphp5-pdo = CSWphp5pdo

CATALOGNAME_CSWphp5-pdomysql = php5_pdomysql
SPKG_DESC_CSWphp5-pdomysql = A MySQL specific database access abstraction module for PHP applications (pdo version)
RUNTIME_DEP_PKGS_CSWphp5-pdomysql = CSWphp5 CSWmysql5rt CSWzlib CSWphp5-pdo
OBSOLETED_BY_CSWphp5-pdomysql = CSWphp5pdomysql

CATALOGNAME_CSWphp5-pdoodbc = php5_pdoodbc
SPKG_DESC_CSWphp5-pdoodbc = An ODBC specific database access abstraction module for PHP applications
RUNTIME_DEP_PKGS_CSWphp5-pdoodbc = CSWphp5 CSWunixodbc CSWphp5-pdo
OBSOLETED_BY_CSWphp5-pdoodbc = CSWphp5pdoodbc

CATALOGNAME_CSWphp5-pdopgsql = php5_pdopgsql
SPKG_DESC_CSWphp5-pdopgsql = A PgSQL specific database access abstraction module for PHP applications (pdo version)
RUNTIME_DEP_PKGS_CSWphp5-pdopgsql = CSWphp5 CSWlibpq CSWphp5-pdo
OBSOLETED_BY_CSWphp5-pdopgsql = CSWphp5pdopgsql

CATALOGNAME_CSWphp5-pdosqlite = php5_pdosqlite
SPKG_DESC_CSWphp5-pdosqlite = A Sqlite specific database access abstraction module for PHP applications (pdo version)
RUNTIME_DEP_PKGS_CSWphp5-pdosqlite = CSWphp5 CSWphp5-pdo CSWsqlite3rt
OBSOLETED_BY_CSWphp5-pdosqlite = CSWphp5pdosqlite

CATALOGNAME_CSWphp5-pgsql = php5_pgsql
SPKG_DESC_CSWphp5-pgsql = The pgsql extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-pgsql = CSWphp5 CSWlibpq
OBSOLETED_BY_CSWphp5-pgsql = CSWphp5pgsql

CATALOGNAME_CSWphp5-posix = php5_posix
SPKG_DESC_CSWphp5-posix = The posix extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-posix = CSWphp5
OBSOLETED_BY_CSWphp5-posix = CSWphp5posix

CATALOGNAME_CSWphp5-pspell = php5_pspell
SPKG_DESC_CSWphp5-pspell = The pspell extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-pspell = CSWphp5 CSWaspell
OBSOLETED_BY_CSWphp5-pspell = CSWphp5pspell

CATALOGNAME_CSWphp5-readline = php5_readline
SPKG_DESC_CSWphp5-readline = The readline extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-readline = CSWphp5 CSWreadline CSWncurses
OBSOLETED_BY_CSWphp5-readline = CSWphp5readline

CATALOGNAME_CSWphp5-session = php5_session
SPKG_DESC_CSWphp5-session = The session extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-session = CSWphp5 CSWlibmm
OBSOLETED_BY_CSWphp5-session = CSWphp5session

CATALOGNAME_CSWphp5-shmop = php5_shmop
SPKG_DESC_CSWphp5-shmop = The shmop extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-shmop = CSWphp5
OBSOLETED_BY_CSWphp5-shmop = CSWphp5shmop

CATALOGNAME_CSWphp5-snmp = php5_snmp
SPKG_DESC_CSWphp5-snmp = The snmp extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-snmp = CSWphp5 CSWnetsnmp
OBSOLETED_BY_CSWphp5-snmp = CSWphp5snmp

CATALOGNAME_CSWphp5-soap = php5_soap
SPKG_DESC_CSWphp5-soap = The soap extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-soap = CSWphp5 CSWiconv CSWlibxml2 CSWzlib
OBSOLETED_BY_CSWphp5-soap = CSWphp5soap

CATALOGNAME_CSWphp5-sockets = php5_sockets
SPKG_DESC_CSWphp5-sockets = The sockets extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-sockets = CSWphp5
OBSOLETED_BY_CSWphp5-sockets = CSWphp5sockets

CATALOGNAME_CSWphp5-sqlite = php5_sqlite
SPKG_DESC_CSWphp5-sqlite = The sqlite extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-sqlite = CSWphp5 CSWsqlite
OBSOLETED_BY_CSWphp5-sqlite = CSWphp5sqlite

CATALOGNAME_CSWphp5-sysvmsg = php5_sysvmsg
SPKG_DESC_CSWphp5-sysvmsg = The sysvmsg extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-sysvmsg = CSWphp5
OBSOLETED_BY_CSWphp5-sysvmsg = CSWphp5sysvmsg

CATALOGNAME_CSWphp5-sysvsem = php5_sysvsem
SPKG_DESC_CSWphp5-sysvsem = The sysvsem extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-sysvsem = CSWphp5
OBSOLETED_BY_CSWphp5-sysvsem = CSWphp5sysvsem

CATALOGNAME_CSWphp5-sysvshm = php5_sysvshm
SPKG_DESC_CSWphp5-sysvshm = The sysvshm extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-sysvshm = CSWphp5
OBSOLETED_BY_CSWphp5-sysvshm = CSWphp5sysvshm

CATALOGNAME_CSWphp5-tidy = php5_tidy
SPKG_DESC_CSWphp5-tidy = The tidy extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-tidy = CSWphp5 CSWhtmltidy
OBSOLETED_BY_CSWphp5-tidy = CSWphp5tidy

CATALOGNAME_CSWphp5-tokenizer = php5_tokenizer
SPKG_DESC_CSWphp5-tokenizer = The tokenizer extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-tokenizer = CSWphp5
OBSOLETED_BY_CSWphp5-tokenizer = CSWphp5tokenizer

CATALOGNAME_CSWphp5-wddx = php5_wddx
SPKG_DESC_CSWphp5-wddx = The wddx extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-wddx = CSWphp5
OBSOLETED_BY_CSWphp5-wddx = CSWphp5wddx

CATALOGNAME_CSWphp5-xmlreader = php5_xmlreader
SPKG_DESC_CSWphp5-xmlreader = The xmlreader extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-xmlreader = CSWphp5 CSWiconv CSWlibxml2 CSWzlib
OBSOLETED_BY_CSWphp5-xmlreader = CSWphp5xmlreader

CATALOGNAME_CSWphp5-xmlrpc = php5_xmlrpc
SPKG_DESC_CSWphp5-xmlrpc = The xmlrpc extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-xmlrpc = CSWphp5 CSWiconv CSWexpat
OBSOLETED_BY_CSWphp5-xmlrpc = CSWphp5xmlrpc

CATALOGNAME_CSWphp5-xmlwriter = php5_xmlwriter
SPKG_DESC_CSWphp5-xmlwriter = The xmlwriter extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-xmlwriter = CSWphp5 CSWiconv CSWlibxml2 CSWzlib
OBSOLETED_BY_CSWphp5-xmlwriter = CSWphp5xmlwriter

CATALOGNAME_CSWphp5-xsl = php5_xsl
SPKG_DESC_CSWphp5-xsl = The xsl extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-xsl  = CSWphp5 CSWiconv CSWlibxml2 
RUNTIME_DEP_PKGS_CSWphp5-xsl += CSWlibxslt CSWzlib
OBSOLETED_BY_CSWphp5-xsl = CSWphp5xsl

CATALOGNAME_CSWphp5-zip = php5_zip
SPKG_DESC_CSWphp5-zip = The zip extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-zip = CSWphp5 CSWzlib
OBSOLETED_BY_CSWphp5-zip = CSWphp5zip

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

PKGFILES_CSWphp5-dbase = .*/lib/php/extensions/.*/dbase.*

PKGFILES_CSWphp5-exif = .*/lib/php/extensions/.*/exif.*

PKGFILES_CSWphp5-ftp = .*/lib/php/extensions/.*/ftp.*

PKGFILES_CSWphp5-gd  = .*/lib/php/extensions/.*/gd.*
PKGFILES_CSWphp5-gd  += .*/include/php/ext/gd.*

PKGFILES_CSWphp5-gettext = .*/lib/php/extensions/.*/gettext.*

PKGFILES_CSWphp5-gmp = .*/lib/php/extensions/.*/gmp.*

PKGFILES_CSWphp5-hash = .*/lib/php/extensions/.*/hash.*
PKGFILES_CSWphp5-hash += .*/include/php/ext/hash.*

PKGFILES_CSWphp5-iconv = .*/lib/php/extensions/.*/iconv.*
PKGFILES_CSWphp5-iconv += .*/include/php/ext/iconv.*

PKGFILES_CSWphp5-imap = .*/lib/php/extensions/.*/imap.*

PKGFILES_CSWphp5-json = .*/lib/php/extensions/.*/json.*

PKGFILES_CSWphp5-ldap = .*/lib/php/extensions/.*/ldap.*

PKGFILES_CSWphp5-mbstring = .*/lib/php/extensions/.*/mbstring.*
PKGFILES_CSWphp5-mbstring += .*/include/php/ext/mbstring.*

PKGFILES_CSWphp5-mcrypt = .*/lib/php/extensions/.*/mcrypt.*

PKGFILES_CSWphp5-mimemagic = .*/lib/php/extensions/.*/mime_magic.*

PKGFILES_CSWphp5-mssql = .*/lib/php/extensions/.*/mssql.*

PKGFILES_CSWphp5-mysql = .*/lib/php/extensions/.*/mysql\.so

PKGFILES_CSWphp5-mysqli = .*/lib/php/extensions/.*/mysqli.*

PKGFILES_CSWphp5-ncurses = .*/lib/php/extensions/.*/ncurses.*

PKGFILES_CSWphp5-odbc = .*/lib/php/extensions/.*/odbc.*

PKGFILES_CSWphp5-openssl = .*/lib/php/extensions/.*/openssl.*

PKGFILES_CSWphp5-pcntl = .*/lib/php/extensions/.*/pcntl.*

PKGFILES_CSWphp5-pdo  = .*/lib/php/extensions/.*/pdo\.so*
PKGFILES_CSWphp5-pdo += .*/include/php/ext/pdo.*

PKGFILES_CSWphp5-pdomysql = .*/lib/php/extensions/.*/pdo_mysql.*

PKGFILES_CSWphp5-pdoodbc = .*/lib/php/extensions/.*/pdo_odbc.*

PKGFILES_CSWphp5-pdopgsql = .*/lib/php/extensions/.*/pdo_pgsql.*

PKGFILES_CSWphp5-pdosqlite = .*/lib/php/extensions/.*/pdo_sqlite.*

PKGFILES_CSWphp5-pgsql = .*/lib/php/extensions/.*/pgsql.*

PKGFILES_CSWphp5-posix = .*/lib/php/extensions/.*/posix.*

PKGFILES_CSWphp5-pspell = .*/lib/php/extensions/.*/pspell.*

PKGFILES_CSWphp5-readline = .*/lib/php/extensions/.*/readline.*

PKGFILES_CSWphp5-session = .*/lib/php/extensions/.*/session.*
PKGFILES_CSWphp5-session += .*/include/php/ext/session.*

PKGFILES_CSWphp5-shmop = .*/lib/php/extensions/.*/shmop.*

PKGFILES_CSWphp5-snmp = .*/lib/php/extensions/.*/snmp.*

PKGFILES_CSWphp5-soap = .*/lib/php/extensions/.*/soap.*

PKGFILES_CSWphp5-sockets = .*/lib/php/extensions/.*/sockets.*

PKGFILES_CSWphp5-sqlite = .*/lib/php/extensions/.*/sqlite.*
PKGFILES_CSWphp5-sqlite += .*/include/php/ext/sqlite.*

PKGFILES_CSWphp5-sysvmsg = .*/lib/php/extensions/.*/sysvmsg.*

PKGFILES_CSWphp5-sysvsem = .*/lib/php/extensions/.*/sysvsem.*

PKGFILES_CSWphp5-sysvshm = .*/lib/php/extensions/.*/sysvshm.*

PKGFILES_CSWphp5-tidy = .*/lib/php/extensions/.*/tidy.*

PKGFILES_CSWphp5-tokenizer = .*/lib/php/extensions/.*/tokenizer.*

PKGFILES_CSWphp5-wddx = .*/lib/php/extensions/.*/wddx.*

PKGFILES_CSWphp5-xmlreader = .*/lib/php/extensions/.*/xmlreader.*

PKGFILES_CSWphp5-xmlrpc = .*/lib/php/extensions/.*/xmlrpc.*

PKGFILES_CSWphp5-xmlwriter = .*/lib/php/extensions/.*/xmlwriter.*

PKGFILES_CSWphp5-xsl = .*/lib/php/extensions/.*/xsl.*

PKGFILES_CSWphp5-zip = .*/lib/php/extensions/.*/zip.*

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
CHECKPKG_OVERRIDES_CSWphp5-pdo += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-gd += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-tidy += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pdopgsql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-snmp += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-hash += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-sysvshm += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-xmlwriter += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-xmlreader += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-mysql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-iconv += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-dbase += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-mbstring += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-xsl += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-exif += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pdoodbc += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-sysvmsg += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-imap += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-odbc += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-readline += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-openssl += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pdosqlite += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-sockets += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-ldap += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-ncurses += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-json += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-tokenizer += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-soap += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pspell += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-wddx += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-gmp += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-gmp += surplus-dependency|CSWlibgmp
CHECKPKG_OVERRIDES_CSWphp5-mssql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pcntl += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-zip += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pdomysql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-mimemagic += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-posix += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-ftp += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-gettext += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-mcrypt += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-sqlite += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-xmlrpc += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pgsql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-shmop += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-session += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pdosqlite += surplus-dependency|CSWphp5-pdo
CHECKPKG_OVERRIDES_CSWphp5-sysvsem += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pdomysql += surplus-dependency|CSWphp5-pdo
CHECKPKG_OVERRIDES_CSWphp5-pdopgsql += surplus-dependency|CSWphp5-pdo
CHECKPKG_OVERRIDES_CSWphp5-mysqli += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-pdoodbc += surplus-dependency|CSWphp5-pdo
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

