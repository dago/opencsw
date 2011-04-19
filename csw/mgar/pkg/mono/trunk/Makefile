NAME = mono
VERSION = 2.10.1
CATEGORIES = lang

DESCRIPTION = Mono Runtime
define BLURB
  Mono is a comprehensive open source development platform based on the .NET
  framework that allows developers to build Linux and cross-platform
  applications with unprecedented productivity. Mono's .NET implementation is
  based on the ECMA standards for C# and  the Common Language Infrastructure.
endef

MASTER_SITES = http://ftp.novell.com/pub/mono/sources/mono/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += CSWmono.gspec CSWmono.depend CSWmono.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk
