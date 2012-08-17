NAME = IO-Socket-SSL
VERSION = 1.76
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SULLR

DESCRIPTION = Nearly transparent SSL encapsulation for IO::Socket::INET.
define BLURB
  This module is a true drop-in replacement for IO::Socket::INET that uses SSL
  to encrypt data before it is transferred to a remote server or client.
  IO::Socket::SSL supports all the extra features that one needs to write a
  full-featured SSL client or server application: multiple SSL contexts,
  cipher selection, certificate verification, and SSL version selection. As an
  extra bonus, it works perfectly with mod_perl.
endef

DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += COPYING

#PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES = CSWpm-io-socket-ssl
CATALOGNAME = pm_io_socket_ssl
SPKG_DESC_CSWpm-io-socket-ssl = $(DESCRIPTION)

# Name change
OBSOLETED_BY_CSWpm-io-socket-ssl = CSWpmiosocketssl
CATALOGNAME_CSWpmiosocketssl = pm_iosocketssl_stub

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmnetssleay

include gar/category.mk
