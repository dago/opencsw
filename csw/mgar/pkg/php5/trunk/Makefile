# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Re-enable the integrated PHP extension builds. This either requires
#   performance enhancements to GAR or a completely different approach.
#   Details documented below.
#
GARNAME     = php5
GARVERSION  = 5.3.3
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

VENDOR_URL     = http://www.php.net/
MASTER_SITES   = http://us.php.net/distributions/
INSTALL_ENV   += INSTALL_ROOT=$(DESTDIR)
STRIP_DIRS    := $(shell $(call _get_php_prefix,$(DESTDIR))/bin/php-config --extension-dir)/*/

DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += php.ini.CSW phpext pear.conf.CSW CSWphp5.postinstall

PACKAGES = CSWphp5 CSWphp5devel

CATALOGNAME_CSWphp5        = php5
SPKG_DESC_CSWphp5          = A High-Level Scripting Language
CATALOGNAME_CSWphp5devel   = php5_devel
SPKG_DESC_CSWphp5devel     = Development files for php5
RUNTIME_DEP_PKGS_CSWphp5      = CSWexpat CSWggettextrt CSWiconv CSWpng CSWsqlite
RUNTIME_DEP_PKGS_CSWphp5     += CSWlibxml2 CSWzlib CSWmysql5rt CSWxpm CSWt1lib
RUNTIME_DEP_PKGS_CSWphp5     += CSWftype2 CSWgd CSWjpeg CSWlibmm
RUNTIME_DEP_PKGS_CSWphp5devel = CSWphp5

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

PATCHFILES += configure.diff

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

NOISALIST = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS += --prefix=$(prefix)/php5
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/php5/bin
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --enable-fastcgi
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --enable-magic-quotes
CONFIGURE_ARGS += --enable-spl=shared
CONFIGURE_ARGS += --with-pcre-regex
CONFIGURE_ARGS += --with-pear=shared
CONFIGURE_ARGS += --with-pear=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
#ENABLE_CHECK = 0

include files/scripts.mk
include gar/category.mk
