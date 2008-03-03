GARNAME = mono
GARVERSION = 1.1.10
CATEGORIES = lang

DESCRIPTION = Mono Runtime
define BLURB
  Mono is a comprehensive open source development platform based on the .NET
  framework that allows developers to build Linux and cross-platform
  applications with unprecedented productivity. Mono's .NET implementation is
  based on the ECMA standards for C# and  the Common Language Infrastructure.
endef

MASTER_SITES = http://go-mono.com/sources/mono-1.1/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += CSWmono.gspec CSWmono.depend CSWmono.prototype

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk
