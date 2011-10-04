# $Id$

NAME = mono
VERSION = 2.10.6
GARTYPE = v2
CATEGORIES = lang

DESCRIPTION = Mono Runtime
define BLURB
  Mono is a comprehensive open source development platform based on the .NET
  framework that allows developers to build Linux and cross-platform
  applications with unprecedented productivity. Mono's .NET implementation is
  based on the ECMA standards for C# and  the Common Language Infrastructure.
endef

MASTER_SITES = http://download.mono-project.com/sources/mono/	
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER = GNU

include gar/category.mk
