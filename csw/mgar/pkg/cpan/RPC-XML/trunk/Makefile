GARNAME = RPC-XML
GARVERSION = 0.59
CATEGORIES = cpan
AUTHOR = RJRAY

DESCRIPTION = A set of classes for core data, message and XML handling
define BLURB
	The package provides a set of classes for creating values to pass to the
	constructors for requests and responses. These are lightweight objects, most
	of which are implemented as tied scalars so as to associate specific type
	information with the value. Classes are also provided for requests,
	responses, faults (errors) and a parser based on the XML::Parser package
	from CPAN.
endef

DISTFILES = $(call admfiles,CSWpmrpcxml,depend prototype)

DEPENDS += cpan/XML-LibXML
#DEPENDS += cpan/libwww-perl

include gar/category.mk

