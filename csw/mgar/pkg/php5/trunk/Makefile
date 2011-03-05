NAME     = php5
VERSION  = 5.3.5
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

VENDOR_URL     = http://www.php.net/
MASTER_SITES   = http://us.php.net/distributions/
INSTALL_ENV   += INSTALL_ROOT=$(DESTDIR)
STRIP_DIRS    := $(shell $(call _get_php_prefix,$(DESTDIR))/bin/php-config --extension-dir)/*/

LICENSE = LICENSE

DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += php.ini.CSW phpext pear.conf.CSW CSWphp5.postinstall

PACKAGES = CSWphp5 CSWphp5devel
PACKAGES += CSWphp5-bcmath
PACKAGES += CSWphp5-bz2
PACKAGES += CSWphp5-calendar
PACKAGES += CSWphp5-ctype
PACKAGES += CSWphp5curl
PACKAGES += CSWphp5dba
PACKAGES += CSWphp5dbase
PACKAGES += CSWphp5dom
PACKAGES += CSWphp5exif
PACKAGES += CSWphp5ftp
PACKAGES += CSWphp5gd
PACKAGES += CSWphp5gettext
PACKAGES += CSWphp5gmp
PACKAGES += CSWphp5hash
PACKAGES += CSWphp5iconv
PACKAGES += CSWphp5imap
PACKAGES += CSWphp5json
PACKAGES += CSWphp5ldap
PACKAGES += CSWphp5mbstring
PACKAGES += CSWphp5mcrypt
PACKAGES += CSWphp5mhash
PACKAGES += CSWphp5mimemagic
PACKAGES += CSWphp5mssql
PACKAGES += CSWphp5mysql
PACKAGES += CSWphp5-mysqli
PACKAGES += CSWphp5ncurses
PACKAGES += CSWphp5odbc
PACKAGES += CSWphp5openssl
PACKAGES += CSWphp5pcntl
PACKAGES += CSWphp5pdo
PACKAGES += CSWphp5pdomysql
PACKAGES += CSWphp5pdoodbc
PACKAGES += CSWphp5pdopgsql
PACKAGES += CSWphp5pdosqlite
PACKAGES += CSWphp5pgsql
PACKAGES += CSWphp5posix
PACKAGES += CSWphp5pspell
PACKAGES += CSWphp5-readline
PACKAGES += CSWphp5session
PACKAGES += CSWphp5shmop
PACKAGES += CSWphp5snmp
PACKAGES += CSWphp5soap
PACKAGES += CSWphp5sockets
PACKAGES += CSWphp5sqlite
PACKAGES += CSWphp5sysvmsg
PACKAGES += CSWphp5sysvsem
PACKAGES += CSWphp5-sysvshm
PACKAGES += CSWphp5tidy
PACKAGES += CSWphp5tokenizer
PACKAGES += CSWphp5wddx
PACKAGES += CSWphp5xmlreader
PACKAGES += CSWphp5xmlrpc
PACKAGES += CSWphp5xmlwriter
PACKAGES += CSWphp5xsl
PACKAGES += CSWphp5zip

BUILD_DEP_PKGS += CSWlibgdbm-dev

CATALOGNAME_CSWphp5        = php5
SPKG_DESC_CSWphp5          = A High-Level Scripting Language

CATALOGNAME_CSWphp5devel   = php5_devel
SPKG_DESC_CSWphp5devel     = Development files for php5
RUNTIME_DEP_PKGS_CSWphp5      = CSWiconv 
RUNTIME_DEP_PKGS_CSWphp5     += CSWlibxml2 CSWzlib
RUNTIME_DEP_PKGS_CSWphp5     += CSWlibmm CSWapache2

CATALOGNAME_CSWphp5-bcmath = php5_bcmath
SPKG_DESC_CSWphp5-bcmath = The bcmath extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-bcmath = CSWphp5
OBSOLETES_CSWphp5-bcmath = CSWphp5bcmath

CATALOGNAME_CSWphp5-bz2 = php5_bz2
SPKG_DESC_CSWphp5-bz2 = The bz2 extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-bz2 = CSWphp5 CSWbzip2
OBSOLETES_CSWphp5-bz2 = CSWphp5bz2

CATALOGNAME_CSWphp5-calendar = php5_calendar
SPKG_DESC_CSWphp5-calendar = The calendar extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-calendar = CSWphp5
OBSOLETES_CSWphp5-calendar = CSWphp5calendar

CATALOGNAME_CSWphp5-ctype = php5_ctype
SPKG_DESC_CSWphp5-ctype = The ctype extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-ctype = CSWphp5
OBSOLETES_CSWphp5-ctype = CSWphp5ctype

CATALOGNAME_CSWphp5curl = php5_curl
SPKG_DESC_CSWphp5curl = The curl extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5curl  = CSWphp5 CSWcurlrt CSWlibidn 
RUNTIME_DEP_PKGS_CSWphp5curl += CSWoldaprt CSWosslrt CSWzlib

CATALOGNAME_CSWphp5dba = php5_dba
SPKG_DESC_CSWphp5dba = The dba extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5dba = CSWphp5 CSWlibgdbm3 CSWbdb42

CATALOGNAME_CSWphp5dbase = php5_dbase
SPKG_DESC_CSWphp5dbase = The dbase extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5dbase = CSWphp5

CATALOGNAME_CSWphp5dom = php5_dom
SPKG_DESC_CSWphp5dom = The dom extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5dom = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CATALOGNAME_CSWphp5exif = php5_exif
SPKG_DESC_CSWphp5exif = The exif extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5exif = CSWphp5

CATALOGNAME_CSWphp5ftp = php5_ftp
SPKG_DESC_CSWphp5ftp = The ftp extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5ftp = CSWphp5 CSWosslrt

CATALOGNAME_CSWphp5gd = php5_gd
SPKG_DESC_CSWphp5gd = The gd extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5gd  = CSWphp5 CSWftype2 CSWgd CSWjpeg
RUNTIME_DEP_PKGS_CSWphp5gd += CSWpng CSWt1lib CSWxpm CSWzlib

CATALOGNAME_CSWphp5-gettext = php5_gettext
SPKG_DESC_CSWphp5-gettext = The gettext extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-gettext = CSWphp5 CSWggettextrt
OBSOLETES_CSWphp5-gettext = CSWphp5gettext

CATALOGNAME_CSWphp5gmp = php5_gmp
SPKG_DESC_CSWphp5gmp = The gmp extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5gmp = CSWphp5 CSWlibgmp

CATALOGNAME_CSWphp5hash = php5_hash
SPKG_DESC_CSWphp5hash = The hash extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5hash = CSWphp5

CATALOGNAME_CSWphp5iconv = php5_iconv
SPKG_DESC_CSWphp5iconv = The iconv extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5iconv = CSWphp5 CSWiconv

CATALOGNAME_CSWphp5imap = php5_imap
SPKG_DESC_CSWphp5imap = The imap extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5imap = CSWphp5 CSWimaprt CSWkrb5lib CSWosslrt

CATALOGNAME_CSWphp5json = php5_json
SPKG_DESC_CSWphp5json = The json extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5json = CSWphp5

CATALOGNAME_CSWphp5ldap = php5_ldap
SPKG_DESC_CSWphp5ldap = The ldap extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5ldap = CSWphp5 CSWoldaprt CSWsasl

CATALOGNAME_CSWphp5mbstring = php5_mbstring
SPKG_DESC_CSWphp5mbstring = The mbstring extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5mbstring = CSWphp5

CATALOGNAME_CSWphp5mcrypt = php5_mcrypt
SPKG_DESC_CSWphp5mcrypt = The mcrypt extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5mcrypt = CSWphp5 CSWlibmcrypt CSWlibltdl7

CATALOGNAME_CSWphp5mhash = php5_mhash
SPKG_DESC_CSWphp5mhash = The mhash extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5mhash = CSWphp5 CSWlibmhash

CATALOGNAME_CSWphp5mimemagic = php5_mime_magic
SPKG_DESC_CSWphp5mimemagic = The mime magic Extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5mimemagic = CSWphp5

CATALOGNAME_CSWphp5mssql = php5_mssql
SPKG_DESC_CSWphp5mssql = The mssql extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5mssql = CSWphp5 CSWfreetds

CATALOGNAME_CSWphp5mysql = php5_mysql
SPKG_DESC_CSWphp5mysql = The mysql extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5mysql = CSWphp5 CSWmysql5rt

CATALOGNAME_CSWphp5-mysqli = php5_mysqli
SPKG_DESC_CSWphp5-mysqli = The mysqli extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-mysqli = CSWphp5 CSWmysql5rt CSWzlib
OBSOLETES_CSWphp5-mysqli = CSWphp5mysqli

CATALOGNAME_CSWphp5ncurses = php5_ncurses
SPKG_DESC_CSWphp5ncurses = The ncurses extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5ncurses = CSWphp5 CSWncurses

CATALOGNAME_CSWphp5odbc = php5_odbc
SPKG_DESC_CSWphp5odbc = The odbc extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5odbc = CSWphp5 CSWunixodbc

CATALOGNAME_CSWphp5openssl = php5_openssl
SPKG_DESC_CSWphp5openssl = The openssl extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5openssl = CSWphp5 CSWosslrt CSWkrb5lib

CATALOGNAME_CSWphp5pcntl = php5_pcntl
SPKG_DESC_CSWphp5pcntl = The pcntl extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5pcntl = CSWphp5

CATALOGNAME_CSWphp5pdo = php5_pdo
SPKG_DESC_CSWphp5pdo = A database access abstraction module for PHP applications
RUNTIME_DEP_PKGS_CSWphp5pdo = CSWphp5 

CATALOGNAME_CSWphp5pdomysql = php5_pdomysql
SPKG_DESC_CSWphp5pdomysql = A MySQL specific database access abstraction module for PHP applications (pdo version)
RUNTIME_DEP_PKGS_CSWphp5pdomysql = CSWphp5 CSWmysql5rt CSWzlib CSWphp5pdo

CATALOGNAME_CSWphp5pdoodbc = php5_pdoodbc
SPKG_DESC_CSWphp5pdoodbc = An ODBC specific database access abstraction module for PHP applications
RUNTIME_DEP_PKGS_CSWphp5pdoodbc = CSWphp5 CSWunixodbc CSWphp5pdo

CATALOGNAME_CSWphp5pdopgsql = php5_pdopgsql
SPKG_DESC_CSWphp5pdopgsql = A PgSQL specific database access abstraction module for PHP applications (pdo version)
RUNTIME_DEP_PKGS_CSWphp5pdopgsql = CSWphp5 CSWlibpq CSWphp5pdo

CATALOGNAME_CSWphp5pdosqlite = php5_pdosqlite
SPKG_DESC_CSWphp5pdosqlite = A Sqlite specific database access abstraction module for PHP applications (pdo version)
RUNTIME_DEP_PKGS_CSWphp5pdosqlite = CSWphp5 CSWphp5pdo

CATALOGNAME_CSWphp5pgsql = php5_pgsql
SPKG_DESC_CSWphp5pgsql = The pgsql extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5pgsql = CSWphp5 CSWlibpq

CATALOGNAME_CSWphp5posix = php5_posix
SPKG_DESC_CSWphp5posix = The posix extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5posix = CSWphp5

CATALOGNAME_CSWphp5pspell = php5_pspell
SPKG_DESC_CSWphp5pspell = The pspell extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5pspell = CSWphp5 CSWaspell

CATALOGNAME_CSWphp5-readline = php5_readline
SPKG_DESC_CSWphp5-readline = The readline extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-readline = CSWphp5 CSWreadline CSWncurses
OBSOLETES_CSWphp5-readline = CSWphp5readline

CATALOGNAME_CSWphp5session = php5_session
SPKG_DESC_CSWphp5session = The session extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5session = CSWphp5 CSWlibmm

CATALOGNAME_CSWphp5shmop = php5_shmop
SPKG_DESC_CSWphp5shmop = The shmop extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5shmop = CSWphp5

CATALOGNAME_CSWphp5snmp = php5_snmp
SPKG_DESC_CSWphp5snmp = The snmp extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5snmp = CSWphp5 CSWnetsnmp CSWosslrt CSWtcpwrap

CATALOGNAME_CSWphp5soap = php5_soap
SPKG_DESC_CSWphp5soap = The soap extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5soap = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CATALOGNAME_CSWphp5sockets = php5_sockets
SPKG_DESC_CSWphp5sockets = The sockets extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5sockets = CSWphp5

CATALOGNAME_CSWphp5sqlite = php5_sqlite
SPKG_DESC_CSWphp5sqlite = The sqlite extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5sqlite = CSWphp5 CSWsqlite

CATALOGNAME_CSWphp5sysvmsg = php5_sysvmsg
SPKG_DESC_CSWphp5sysvmsg = The sysvmsg extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5sysvmsg = CSWphp5

CATALOGNAME_CSWphp5sysvsem = php5_sysvsem
SPKG_DESC_CSWphp5sysvsem = The sysvsem extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5sysvsem = CSWphp5

CATALOGNAME_CSWphp5-sysvshm = php5_sysvshm
SPKG_DESC_CSWphp5-sysvshm = The sysvshm extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5-sysvshm = CSWphp5
OBSOLETES_CSWphp5-sysvshm = CSWphp5sysvshm

CATALOGNAME_CSWphp5tidy = php5_tidy
SPKG_DESC_CSWphp5tidy = The tidy extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5tidy = CSWphp5 CSWhtmltidy

CATALOGNAME_CSWphp5tokenizer = php5_tokenizer
SPKG_DESC_CSWphp5tokenizer = The tokenizer extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5tokenizer = CSWphp5

CATALOGNAME_CSWphp5wddx = php5_wddx
SPKG_DESC_CSWphp5wddx = The wddx extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5wddx = CSWphp5

CATALOGNAME_CSWphp5xmlreader = php5_xmlreader
SPKG_DESC_CSWphp5xmlreader = The xmlreader extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5xmlreader = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CATALOGNAME_CSWphp5xmlrpc = php5_xmlrpc
SPKG_DESC_CSWphp5xmlrpc = The xmlrpc extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5xmlrpc = CSWphp5 CSWiconv CSWlibxml2 CSWzlib CSWexpat

CATALOGNAME_CSWphp5xmlwriter = php5_xmlwriter
SPKG_DESC_CSWphp5xmlwriter = The xmlwriter extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5xmlwriter = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CATALOGNAME_CSWphp5xsl = php5_xsl
SPKG_DESC_CSWphp5xsl = The xsl extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5xsl  = CSWphp5 CSWiconv CSWlibxml2 
RUNTIME_DEP_PKGS_CSWphp5xsl += CSWlibxslt CSWzlib

CATALOGNAME_CSWphp5zip = php5_zip
SPKG_DESC_CSWphp5zip = The zip extension for PHP5
RUNTIME_DEP_PKGS_CSWphp5zip = CSWphp5 CSWzlib

PKGFILES_CSWphp5devel  = $(bindir)/php-config
PKGFILES_CSWphp5devel += $(bindir)/phpize
PKGFILES_CSWphp5devel += $(bindir)/peardev
PKGFILES_CSWphp5devel += $(libdir)/php/build/.*
PKGFILES_CSWphp5devel += $(includedir)/php/TSRM.*
PKGFILES_CSWphp5devel += $(includedir)/php/Zend.*
PKGFILES_CSWphp5devel += $(includedir)/php/include.*
PKGFILES_CSWphp5devel += $(includedir)/php/main.*
PKGFILES_CSWphp5devel += $(includedir)/php/regex.*
PKGFILES_CSWphp5devel += $(includedir)/php/ext/date.*
PKGFILES_CSWphp5devel += $(includedir)/php/ext/filter.*
PKGFILES_CSWphp5devel += $(includedir)/php/ext/libxml.*
PKGFILES_CSWphp5devel += $(includedir)/php/ext/pcre.*
PKGFILES_CSWphp5devel += $(includedir)/php/ext/spl.*
PKGFILES_CSWphp5devel += $(includedir)/php/ext/standard.*
PKGFILES_CSWphp5devel += $(includedir)/php/ext/xml.*
PKGFILES_CSWphp5devel += $(mandir)/man1/php-config.1
PKGFILES_CSWphp5devel += $(mandir)/man1/phpize.1

PKGFILES_CSWphp5-bcmath = .*/lib/php/extensions/.*/bcmath.*

PKGFILES_CSWphp5-bz2 = .*/lib/php/extensions/.*/bz2.*

PKGFILES_CSWphp5-calendar = .*/lib/php/extensions/.*/calendar.*

PKGFILES_CSWphp5-ctype = .*/lib/php/extensions/.*/ctype.*

PKGFILES_CSWphp5curl = .*/lib/php/extensions/.*/curl.*

PKGFILES_CSWphp5dba = .*/lib/php/extensions/.*/dba\.so

PKGFILES_CSWphp5dbase = .*/lib/php/extensions/.*/dbase.*

PKGFILES_CSWphp5dom = .*/lib/php/extensions/.*/dom.*
PKGFILES_CSWphp5dom += .*/include/php/ext/dom.*

PKGFILES_CSWphp5exif = .*/lib/php/extensions/.*/exif.*

PKGFILES_CSWphp5ftp = .*/lib/php/extensions/.*/ftp.*

PKGFILES_CSWphp5gd  = .*/lib/php/extensions/.*/gd.*
PKGFILES_CSWphp5gd  += .*/include/php/ext/gd.*

PKGFILES_CSWphp5-gettext = .*/lib/php/extensions/.*/gettext.*

PKGFILES_CSWphp5gmp = .*/lib/php/extensions/.*/gmp.*

PKGFILES_CSWphp5hash = .*/lib/php/extensions/.*/hash.*
PKGFILES_CSWphp5hash += .*/include/php/ext/hash.*

PKGFILES_CSWphp5iconv = .*/lib/php/extensions/.*/iconv.*
PKGFILES_CSWphp5iconv += .*/include/php/ext/iconv.*

PKGFILES_CSWphp5imap = .*/lib/php/extensions/.*/imap.*

PKGFILES_CSWphp5json = .*/lib/php/extensions/.*/json.*

PKGFILES_CSWphp5ldap = .*/lib/php/extensions/.*/ldap.*

PKGFILES_CSWphp5mbstring = .*/lib/php/extensions/.*/mbstring.*
PKGFILES_CSWphp5mbstring += .*/include/php/ext/mbstring.*

PKGFILES_CSWphp5mcrypt = .*/lib/php/extensions/.*/mcrypt.*

PKGFILES_CSWphp5mhash = .*/lib/php/extensions/.*/mhash.*

PKGFILES_CSWphp5mimemagic = .*/lib/php/extensions/.*/mime_magic.*

PKGFILES_CSWphp5mssql = .*/lib/php/extensions/.*/mssql.*

PKGFILES_CSWphp5mysql = .*/lib/php/extensions/.*/mysql\.so

PKGFILES_CSWphp5-mysqli = .*/lib/php/extensions/.*/mysqli.*

PKGFILES_CSWphp5ncurses = .*/lib/php/extensions/.*/ncurses.*

PKGFILES_CSWphp5odbc = .*/lib/php/extensions/.*/odbc.*

PKGFILES_CSWphp5openssl = .*/lib/php/extensions/.*/openssl.*

PKGFILES_CSWphp5pcntl = .*/lib/php/extensions/.*/pcntl.*

PKGFILES_CSWphp5pdo  = .*/lib/php/extensions/.*/pdo\.so*
PKGFILES_CSWphp5pdo += .*/include/php/ext/pdo.*

PKGFILES_CSWphp5pdomysql = .*/lib/php/extensions/.*/pdo_mysql.*

PKGFILES_CSWphp5pdoodbc = .*/lib/php/extensions/.*/pdo_odbc.*

PKGFILES_CSWphp5pdopgsql = .*/lib/php/extensions/.*/pdo_pgsql.*

PKGFILES_CSWphp5pdosqlite = .*/lib/php/extensions/.*/pdo_sqlite.*

PKGFILES_CSWphp5pgsql = .*/lib/php/extensions/.*/pgsql.*

PKGFILES_CSWphp5posix = .*/lib/php/extensions/.*/posix.*

PKGFILES_CSWphp5pspell = .*/lib/php/extensions/.*/pspell.*

PKGFILES_CSWphp5-readline = .*/lib/php/extensions/.*/readline.*

PKGFILES_CSWphp5session = .*/lib/php/extensions/.*/session.*
PKGFILES_CSWphp5session += .*/include/php/ext/session.*

PKGFILES_CSWphp5shmop = .*/lib/php/extensions/.*/shmop.*

PKGFILES_CSWphp5snmp = .*/lib/php/extensions/.*/snmp.*

PKGFILES_CSWphp5soap = .*/lib/php/extensions/.*/soap.*

PKGFILES_CSWphp5sockets = .*/lib/php/extensions/.*/sockets.*

PKGFILES_CSWphp5sqlite = .*/lib/php/extensions/.*/sqlite.*
PKGFILES_CSWphp5sqlite += .*/include/php/ext/sqlite.*

PKGFILES_CSWphp5sysvmsg = .*/lib/php/extensions/.*/sysvmsg.*

PKGFILES_CSWphp5sysvsem = .*/lib/php/extensions/.*/sysvsem.*

PKGFILES_CSWphp5-sysvshm = .*/lib/php/extensions/.*/sysvshm.*

PKGFILES_CSWphp5tidy = .*/lib/php/extensions/.*/tidy.*

PKGFILES_CSWphp5tokenizer = .*/lib/php/extensions/.*/tokenizer.*

PKGFILES_CSWphp5wddx = .*/lib/php/extensions/.*/wddx.*

PKGFILES_CSWphp5xmlreader = .*/lib/php/extensions/.*/xmlreader.*

PKGFILES_CSWphp5xmlrpc = .*/lib/php/extensions/.*/xmlrpc.*

PKGFILES_CSWphp5xmlwriter = .*/lib/php/extensions/.*/xmlwriter.*

PKGFILES_CSWphp5xsl = .*/lib/php/extensions/.*/xsl.*

PKGFILES_CSWphp5zip = .*/lib/php/extensions/.*/zip.*

PATCHFILES += configure.diff
PATCHFILES += odbc.diff
PATCHFILES += pdopgsql.diff
PATCHFILES += pgsql.diff

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
EXTRA_CFLAGS   += -I/opt/csw/include

export CPPFLAGS
EXTRA_CPPFLAGS = -I../ext/mbstring

EXTRA_LDFLAGS += -L$(libdir) -R$(libdir)
LIBS += -lrt -lintl 

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
CONFIGURE_ARGS += --with-iconv=shared
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
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
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)
CONFIGURE_ARGS += --enable-xmlwriter=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-xsl=shared,$(prefix)
CONFIGURE_ARGS += --enable-zip=shared
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
#ENABLE_CHECK = 0

CHECKPKG_OVERRIDES_CSWphp5pdo += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-bcmath += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5gd += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5tidy += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5pdopgsql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5snmp += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-ctype += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-calendar += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5hash += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-sysvshm += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5xmlwriter += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5xmlreader += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5mysql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5iconv += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5dbase += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5mbstring += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5xsl += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5exif += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-bz2 += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5pdoodbc += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5dba += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5sysvmsg += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5imap += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5odbc += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-readline += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5openssl += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5pdosqlite += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5sockets += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5ldap += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5ncurses += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5json += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5tokenizer += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5dom += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5soap += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5pspell += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5wddx += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5gmp += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5mssql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5pcntl += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5zip += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5pdomysql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5curl += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5sysvsem += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-mysqli += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5mimemagic += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5posix += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5ftp += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5-gettext += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5mcrypt += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5sqlite += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5xmlrpc += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5pgsql += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5shmop += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5mhash += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWphp5session += surplus-dependency|CSWphp5

include files/scripts.mk
include gar/category.mk
