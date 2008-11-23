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
DISTFILES += httpd-php5.conf.CSW

# PHP Apache2 SAPI
ADMFILES   = depend prototype postinstall preremove space
DISTFILES += $(call admfiles,CSWap2modphp5,$(ADMFILES))

# Patches
include files/patches.mk

# Dependencies
include files/depend.mk
DEPENDS += server/apache2

# SAPI Common Configuration
include files/config.mk

# Apache2 SAPI Specific Configuration
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs

# System Rules/Configuration
include gar/category.mk

# Common Rules
include files/rules.mk

# SAPI Specific Rules
STRIP_DIRS += $(DESTDIR)$(prefix)/apache2/libexec

# Copy over template config files and utility scripts
post-install:
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 \
		$(WORKDIR)/httpd-php5.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc/extra
	@$(MAKECOOKIE)

