NAME = Net-SSLeay
VERSION = 1.36
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = FLORA

DESCRIPTION = Extension for using OpenSSL
define BLURB
  This module offers some high level convinience functions for accessing web
  pages on SSL servers (for symmetry, same API is offered for accessing http
  servers, too), a sslcat() function for writing your own clients, and finally
  access to the SSL api of SSLeay/OpenSSL package so you can write servers or
  clients for more complicated applications.
endef

MODDIST  = $(DISTNAME).tar.gz

PACKAGES = CSWpmnetssleay
CATALOGNAME = pm_netssleay

RUNTIME_DEP_PKGS = CSWosslrt
BUILD_DEP_PKGS = CSWossldevel

PERL_CONFIGURE_ARGS = $(prefix) INSTALLDIRS=vendor

CONFIGURE_ENV = OPENSSL_PREFIX=$(prefix) AUTOMATED_TESTING=1 PERL_MM_USE_DEFAULT=1

include gar/category.mk

