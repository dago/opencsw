GARNAME = php
GARVERSION = 5.0.5
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
DISTFILES += php.ini ext_enable.sh ext_disable.sh

# PHP Core
DISTFILES += CSWphp5.gspec CSWphp5.prototype CSWphp5.depend
DISTFILES += CSWphp5devel.gspec CSWphp5devel.prototype CSWphp5devel.depend

# PHP Apache2 SAPI
DISTFILES += CSWap2modphp5.gspec CSWap2modphp5.prototype CSWap2modphp5.depend 
DISTFILES += CSWap2modphp5.space CSWap2modphp5.postinstall CSWap2modphp5.preremove

# PHP Extensions
include files/extensions.mk

# Apply patches from the workdir
PATCHDIR = $(WORKDIR)
PATCHDIRLEVEL = 0

# Fix up configure script
PATCHFILES += config.diff

# Fix ssl paths for uw-imap c-client
PATCHFILES += imap-ssl.diff

# Don't hardcode $(CC)
PATCHFILES += imap-cc.diff

#DEPENDS += server/apache2 server/mysql4

# Configuration
include files/config.mk
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-imap=$(C_CLIENT)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)/ssl

# Some tests are failing -- report submitted to PHP QA
ENABLE_TEST = 0

include ../category.mk

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

EXTRA_LIB = $(prefix)/bdb43/lib
EXTRA_INC = $(prefix)/bdb43/include

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
	@$(MAKECOOKIE)
