GARNAME = SOAP-WSDL
GARVERSION = 1.20
CATEGORIES = cpan
AUTHOR = MKUTTER

DESCRIPTION = Web Service Descriptor Language support for SOAP::Lite
define BLURB
  SOAP::WSDL provides decent WSDL support for SOAP::Lite. It is built as a
  add-on to SOAP::Lite, and will sit on top of it, forwarding all the actual
  request-response to SOAP::Lite - somewhat like a pre-processor.
endef

DISTFILES += CSWpmsoapwsdl.gspec CSWpmsoapwsdl.depend

DEPENDS += cpan/URI cpan/XML-Parser cpan/libwww-perl
DEPENDS += cpan/MIME-Lite cpan/MIME-tools cpan/Compress-Zlib

CONFIGURE_ARGS = --noprompt

include gar/category.mk
