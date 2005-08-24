GARNAME = mono
GARVERSION = 1.0.5
CATEGORIES = lang

DESCRIPTION = Mono Runtime
define BLURB
  Mono is a comprehensive open source development platform based on the .NET
  framework that allows developers to build Linux and cross-platform
  applications with unprecedented productivity. Mono's .NET implementation is
  based on the ECMA standards for C# and  the Common Language Infrastructure.
endef

MASTER_SITES = http://www.go-mono.com/archive/1.0.5/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += CSWmono.gspec CSWmono.depend CSWmono.prototype

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
