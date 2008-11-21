GARNAME = php
GARVERSION = 5.2.6
CATEGORIES = lang

# This directory is for the build and packaging of the Apache 1.3.x
# SAPI module for PHP5.  PHP CGI/CLI and extensions are built along
# with the Apache 2.0.x SAPI.

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

# PHP Apache SAPI
ADMFILES   = depend prototype preremove postinstall space
DISTFILES += $(call admfiles,CSWmodphp5,$(ADMFILES))

# Patches
include files/patches.mk

# Dependencies
include files/depend.mk
DEPENDS += server/apache

# SAPI Common Configuration
include files/config.mk

# Apache SAPI Specific Configuration
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache/bin/apxs
INSTALL_SCRIPTS = sapi-only

# System Rules/Configuration
include ../category.mk

# Common Rules
include files/rules.mk

# SAPI Specific Rules
STRIP_DIRS += $(DESTDIR)$(prefix)/apache/libexec

install-sapi-only:
	@( cd $(WORKSRC) ; $(INSTALL_ENV) $(MAKE) install-sapi )

