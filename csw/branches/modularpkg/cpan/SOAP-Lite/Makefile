GARNAME = SOAP-Lite
GARVERSION = 0.69
CATEGORIES = cpan
AUTHOR = BYRNE

DESCRIPTION = client and server side SOAP implementation
define BLURB
  SOAP::Lite is a collection of Perl modules which provides a simple and
  lightweight interface to the Simple Object Access Protocol (SOAP) both on
  client and server side.
endef

DISTFILES += $(call admfiles,CSWpmsoaplite,depend prototype)

DEPENDS += cpan/URI
DEPENDS += cpan/XML-Parser
DEPENDS += cpan/libwww-perl
DEPENDS += cpan/MIME-Lite
DEPENDS += cpan/MIME-tools
DEPENDS += cpan/Compress-Zlib

CONFIGURE_ARGS = --noprompt

include ../category.mk

