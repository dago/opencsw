GARNAME = SOAP-Lite
GARVERSION = 0.55
CATEGORIES = cpan
AUTHOR = KULCHENKO
GARCH = all

DESCRIPTION = client and server side SOAP implementation
define BLURB
  SOAP::Lite is a collection of Perl modules which provides a simple and
  lightweight interface to the Simple Object Access Protocol (SOAP) both on
  client and server side.
endef

DISTFILES += CSWpmsoaplite.gspec CSWpmsoaplite.depend

DEPENDS += cpan/URI cpan/XML-Parser cpan/libwww-perl
DEPENDS += cpan/MIME-Lite cpan/MIME-tools cpan/Compress-Zlib

CONFIGURE_ARGS = --noprompt

include ../category.mk
