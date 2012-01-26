NAME = gluezilla
VERSION = 2.6
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Mono Runtime
define BLURB
  Mono is a comprehensive open source development platform based on the .NET
  framework that allows developers to build Linux and cross-platform
  applications with unprecedented productivity. Mono's .NET implementation is
  based on the ECMA standards for C# and  the Common Language Infrastructure.
endef

MASTER_SITES = http://ftp.novell.com/pub/mono/sources/mono/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2 

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
