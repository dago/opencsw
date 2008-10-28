GARNAME = php
GARVERSION = 5.2.6
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

# Auxilliary files
DISTFILES += php.ini.CSW phpext
DISTFILES += CSWphp5_ext_enable.sh CSWphp5_ext_disable.sh
DISTFILES += CSWphp5_ext.depend

# PHP CGI SAPI + Core
DISTFILES += $(call admfiles,CSWphp5,prototype depend postinstall)
DISTFILES += $(call admfiles,CSWphp5devel,prototype depend)

# PHP Extensions
include files/extensions.mk

# Patches
include files/patches.mk

# Dependencies
include files/depend.mk

# SAPI Common Configuration
include files/config.mk

# SAPI Specific Configuration
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --enable-fastcgi
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-pcntl

# System Rules/Configuration
include ../category.mk

# Common Rules
include files/rules.mk

# SAPI Specific Rules
STRIP_DIRS += $(DESTDIR)$(prefix)/apache2/libexec

# Copy over template config files and utility scripts
post-install: install-templates

php5_root = $(DESTDIR)$(prefix)/php5
php5_bin = $(php5_root)/bin
php5_lib = $(php5_root)/lib

install-templates:
	ginstall -m 0755 \
		$(WORKDIR)/phpext \
		$(DESTDIR)$(prefix)/php5/bin
	gsed -i -e s,PHPEXTDIR,$(shell $(DESTDIR)$(prefix)/php5/bin/php-config --extension-dir), $(WORKDIR)/php.ini.CSW
	ginstall -m 0644 \
		$(WORKDIR)/php.ini.CSW \
		$(DESTDIR)$(prefix)/php5/lib
	@$(MAKECOOKIE)

