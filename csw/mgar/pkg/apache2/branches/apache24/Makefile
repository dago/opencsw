# $Id: Makefile 18185 2012-06-01 02:30:46Z bdwalton $

NAME = httpd
VERSION = 2.4.3
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A high performance HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

# Source location
MASTER_SITES  = http://www.eu.apache.org/dist/httpd/

# work around dumb checkpkg not recognizing the license file ...
LICENSE = LICENSE

# Build multiple mpm's and merge them all into one install
#EXTRA_MODULATORS = MPM
# !!!NOTE, NOTE, NOTE!!! prefork must be last as it's the one where
# all modules are built.  This affects the default httpd.conf that
# gets generated.  The other modulations will generate httpd.conf
# files that lack the important LoadModule lines.  This is primarily
# useful at version bump time when files/httpd.conf.CSW may need an
# update to reflect new modules, etc.
#MODULATIONS_MPM = worker prefork

# MERGE_SCRIPTS_isa-default-mpm-prefork = copy-all
# MERGE_SCRIPTS_isa-default-mpm-worker = copy-all

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(NAME)-$(VERSION).tar.gz
# Standard package bits
DISTFILES += cswapache2

PATCHFILES += 0001-Add-an-OpenCSW-option-to-config.layout.patch

BUILD_DEP_PKGS += CSWlibaprutil-dev

# The SMF support: you don't need to specify cswinitsmf any more.  You need to
# make sure the the /etc/opt/csw/init.d/cswapache file gets installed during
# the post-install stage, and add "INITSMF = /etc/opt/csw/init.d/cswapache" to
# the Makefile.
INITSMF = /etc/opt/csw/init.d/cswapache2

# Build Configuration
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/bin/apu-1-config
CONFIGURE_ARGS += --with-mpm=$(MPM)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-rule=SSL_EXPERIMENTAL
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --with-z=$(prefix)
CONFIGURE_ARGS += --with-ssl=$(prefix)

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

TEST_TARGET = test

include gar/category.mk

CFLAGS := -DSSL_EXPERIMENTAL -DSSL_ENGINE $(CFLAGS)

FIXCONFIG_DIRS     = $(DESTDIR)
FIXCONFIG_RMPATHS  = $(DESTDIR)

pre-configure-modulated:
	(cd $(WORKDIR)/$(NAME)-$(VERSION); ./buildconf)
	@gsed -e s,INSTALL_PREFIX,$(prefix)/apache2,g \
		$(WORKDIR)/config.layout > $(WORKDIR)/$(NAME)-$(VERSION)/config.layout
	@$(MAKECOOKIE)
