GARNAME = Net-SSLeay
GARVERSION = 1.30
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

DISTNAME = $(subst -,_,$(GARNAME)).pm-$(GARVERSION)
MODDIST  = $(DISTNAME).tar.gz
WORKSRC  = $(WORKDIR)/$(DISTNAME)

DISTFILES += $(call admfiles,CSWpmnetssleay,depend prototype)

# Convince Makefile.PL to use our OpenSSL
PATCHFILES += ossl-0.9.8a.diff

PERL_CONFIGURE_ARGS = $(prefix) INSTALLDIRS=vendor

# Test disabled: Bug 3287
TEST_SCRIPTS =

include ../category.mk

