NAME = RPC-XML
VERSION = 0.74
CATEGORIES = cpan
GARTYPE = v2
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

RUNTIME_DEP_PKGS_CSWpmrpcxml = CSWpmlibwww CSWpmxmllibxml CSWpmcompresszlib
BUILD_DEP_PKGS_CSWpmrpcxml = CSWpmlibwww CSWpmxmllibxml CSWpmcompresszlib

PACKAGES = CSWpmrpcxml
CATALOGNAME = pm_rpcxml
ARCHALL = 1

LICENSE = README

include gar/category.mk
