# $Id$

NAME = lua
VERSION = 5.1.4
CATEGORIES = lang

DESCRIPTION = Light-weight language designed for extending applications
define BLURB
  Lua is a powerful light-weight programming language designed for extending
  applications. Lua is also frequently used as a general-purpose, stand-alone
  language.
endef

SPKG_SOURCEURL = http://www.lua.org/
MASTER_SITES = http://www.lua.org/ftp/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = dynamic.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =

BUILD_ARGS += solaris CC=$(CC)
BUILD_ARGS += CFLAGS="${CFLAGS}
BUILD_ARGS += -DLUA_USE_POSIX
BUILD_ARGS += -DLUA_USE_DLOPEN
BUILD_ARGS += -KPIC" MYLIBS="-ldl"

INSTALL_ARGS += INSTALL=ginstall
INSTALL_ARGS += INSTALL_TOP=$(DESTDIR)$(prefix)
INSTALL_ARGS += INSTALL_MAN=$(DESTDIR)$(mandir)/man1

LICENSE = COPYRIGHT

include gar/category.mk
