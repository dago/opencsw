# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pubcookie
VERSION = 3.3.4a
GARTYPE = v2

DESCRIPTION = Open-source software for intra-institutional web authentication

MASTER_SITES += http://www.pubcookie.org/downloads/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.pubcookie.org

AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-login
CONFIGURE_ARGS += --enable-default-des
#CONFIGURE_ARGS += --enable-krb5
CONFIGURE_ARGS += --enable-ldap
CONFIGURE_ARGS += --enable-shadow
CONFIGURE_ARGS += --enable-apache
CONFIGURE_ARGS += --with-apxs=/opt/csw/apache2/sbin/apxs 

CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --with-krb5-dir=$(prefix)
CONFIGURE_ARGS += --with-ldap-dir=$(prefix)

# The package does not provide a check
#TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS = AP2_LIBEXEC
INSTALL_OVERRIDE_VAR_AP2_LIBEXEC = $(AP2_LIBEXEC)

include gar/category.mk

