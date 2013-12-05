NAME = SOAP-WSDL
VERSION = 2.00.10
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MKUTTER

DESCRIPTION = SOAP with WSDL support
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-template
BUILD_DEP_PKGS += CSWpm-class-std-fast
BUILD_DEP_PKGS += CSWpm-module-build
BUILD_DEP_PKGS += CSWpm-libwww-perl
BUILD_DEP_PKGS += CSWpm-timedate
BUILD_DEP_PKGS += CSWpm-xml-parser

PACKAGES += CSWpm-soap-wsdl
CATALOGNAME_CSWpm-soap-wsdl = pm_soap_wsdl
SPKG_DESC_CSWpm-soap-wsdl = SOAP with WSDL support
ARCHALL_CSWpm-soap-wsdl = 1
RUNTIME_DEP_PKGS_CSWpm-soap-wsdl += CSWpm-template
RUNTIME_DEP_PKGS_CSWpm-soap-wsdl += CSWpm-term-readkey
RUNTIME_DEP_PKGS_CSWpm-soap-wsdl += CSWpm-uri
RUNTIME_DEP_PKGS_CSWpm-soap-wsdl += CSWpm-class-std-fast
RUNTIME_DEP_PKGS_CSWpm-soap-wsdl += CSWpm-libwww-perl
RUNTIME_DEP_PKGS_CSWpm-soap-wsdl += CSWpm-timedate
RUNTIME_DEP_PKGS_CSWpm-soap-wsdl += CSWpm-xml-parser

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
