GARNAME = Net-SSLeay
GARVERSION = 1.25
CATEGORIES = cpan
AUTHOR = SAMPO

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

DISTFILES += CSWpmnetssleay.gspec

CONFIGURE_ARGS = $(tool_prefix)

# Test disabled: Bug 3287
ENABLE_TEST = 0

include ../category.mk
