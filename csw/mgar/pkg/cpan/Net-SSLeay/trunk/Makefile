GARNAME = Net-SSLeay
GARVERSION = 1.35
CATEGORIES = cpan
AUTHOR = FLORA

DESCRIPTION = extension for using OpenSSL
define BLURB
  This module offers some high level convinience functions for accessing web
  pages on SSL servers (for symmetry, same API is offered for accessing http
  servers, too), a sslcat() function for writing your own clients, and finally
  access to the SSL api of SSLeay/OpenSSL package so you can write servers or
  clients for more complicated applications.
endef

MODDIST  = $(DISTNAME).tar.gz
WORKSRC  = $(WORKDIR)/$(DISTNAME)

DISTFILES += $(call admfiles,CSWpmnetssleay,depend)

PERL_CONFIGURE_ARGS = $(prefix) INSTALLDIRS=vendor

CONFIGURE_ENV = OPENSSL_PREFIX=$(prefix) AUTOMATED_TESTING=1 PERL_MM_USE_DEFAULT=1

include gar/category.mk

