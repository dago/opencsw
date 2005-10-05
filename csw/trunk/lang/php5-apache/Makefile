GARNAME = php
GARVERSION = 5.0.5
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

# Can't do direct downloads of PHP from php.net
#MASTER_SITES = http://www.php.net/downloads.php
MASTER_SITES = ftp://ftp.cac.washington.edu/imap/

SPKG_SOURCEURL = http://www.php.net/downloads.php

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += c-client.tar.Z

IMAPDIR  = imap-2004f
C_CLIENT = ../$(IMAPDIR)

# PHP Apache SAPI
DISTFILES += CSWmodphp5.gspec CSWmodphp5.prototype CSWmodphp5.depend 
DISTFILES += CSWmodphp5.space CSWmodphp5.postinstall CSWmodphp5.preremove

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
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache/bin/apxs
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

