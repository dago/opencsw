GARNAME = IO-Socket-SSL
GARVERSION = 0.97
CATEGORIES = cpan
AUTHOR = BEHROOZI

DESCRIPTION = nearly transparent SSL encapsulation for IO::Socket::INET.
define BLURB
  This module is a true drop-in replacement for IO::Socket::INET that uses SSL
  to encrypt data before it is transferred to a remote server or client.
  IO::Socket::SSL supports all the extra features that one needs to write a
  full-featured SSL client or server application: multiple SSL contexts,
  cipher selection, certificate verification, and SSL version selection. As an
  extra bonus, it works perfectly with mod_perl.
endef

DISTFILES += CSWpmiosocketssl.gspec CSWpmiosocketssl.depend

DEPENDS += cpan/Net-SSLeay

include gar/category.mk
