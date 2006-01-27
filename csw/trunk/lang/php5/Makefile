GARNAME = php
GARVERSION = 5.1.2
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

# Can't do direct downloads of PHP from php.net
#MASTER_SITES = http://www.php.net/downloads.php
MASTER_SITES = ftp://ftp.cac.washington.edu/imap/

SPKG_SOURCEURL = http://www.php.net/downloads.php

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += c-client.tar.Z

IMAPDIR  = imap-2004f
C_CLIENT = ../$(IMAPDIR)

# Auxilliary files
DISTFILES += php.ini phpext
DISTFILES += CSWphp5_ext_enable.sh CSWphp5_ext_disable.sh 

# PHP Core
DISTFILES += $(call admfiles,CSWphp5,prototype depend postinstall)
DISTFILES += $(call admfiles,CSWphp5devel,prototype depend)

# PHP Apache2 SAPI
DISTFILES += $(call admfiles,CSWap2modphp5,prototype depend space postinstall preremove)

# PHP Extensions
include files/extensions.mk

# Apply patches from the workdir
PATCHDIR = $(WORKDIR)
PATCHDIRLEVEL = 0

# Disable apache module activation
PATCHFILES += config.diff

# Fix ssl paths for uw-imap c-client
PATCHFILES += imap-ssl.diff

# Don't hardcode $(CC)
PATCHFILES += imap-cc.diff

# Respect my CFLAGS
PATCHFILES += imap-cflags.diff

#DEPENDS += server/apache2 server/mysql4

# Configuration
include files/config.mk
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-imap=$(C_CLIENT)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)/ssl
CONFIGURE_ARGS += --with-kerberos=$(prefix)

# Some tests are failing -- report submitted to PHP QA
ENABLE_TEST = 0

include ../category.mk

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

EXTRA_LIB = $(prefix)/bdb43/lib
EXTRA_INC = $(prefix)/bdb43/include

PHP5ROOT    = $(DESTDIR)$(prefix)/php5
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin
STRIP_DIRS += $(DESTDIR)$(prefix)/apache2/libexec

# Build the imap client library first
pre-configure:
	@( cd $(WORKDIR)/$(IMAPDIR) ; $(BUILD_ENV) make soc )
	@$(MAKECOOKIE)

# This is required so that we don't try to regen the
# sqlite parser.
pre-build:
	@touch $(WORKSRC)/ext/sqlite/libsqlite/src/parse.c
	@$(MAKECOOKIE)

# Copy over a starter config file (based on php.ini-recommended)
post-install:
	@sed -e s,PHPEXTDIR,$(shell $(DESTDIR)$(prefix)/php5/bin/php-config --extension-dir), $(WORKDIR)/php.ini > $(DESTDIR)$(prefix)/php5/lib/php.ini
	@cp $(WORKDIR)/phpext $(DESTDIR)$(prefix)/php5/bin
	@$(MAKECOOKIE)
