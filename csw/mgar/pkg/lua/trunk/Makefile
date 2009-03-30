GARNAME = lua
GARVERSION = 5.1.4
CATEGORIES = lang

DESCRIPTION = light-weight language designed for extending applications
define BLURB
  Lua is a powerful light-weight programming language designed for extending
  applications. Lua is also frequently used as a general-purpose, stand-alone
  language.
endef

MASTER_SITES = http://www.lua.org/ftp/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWlua.gspec 
PATCHFILES = dynamic.patch

#CSWlua.prototype CSWlua.depend

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#LIBDEPS += lib/db lib/gdbm

# Configuration flags
CONFIGURE_SCRIPTS=

BUILD_ARGS += solaris CC=$(CC) CFLAGS="${CFLAGS} -DLUA_USE_POSIX -DLUA_USE_DLOPEN -KPIC" MYLIBS="-ldl"

INSTALL_ARGS += INSTALL=ginstall INSTALL_TOP=$(DESTDIR)$(prefix) INSTALL_MAN=$(DESTDIR)$(mandir)/man1

include gar/category.mk
