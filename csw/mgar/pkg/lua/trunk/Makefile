# $Id$

# Open issues:
# - no .pc file
# - provide different C/C++ libs for liblua as discussed here:
#     http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=560139

NAME = lua
VERSION = 5.2.0
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Light-weight language designed for extending applications
define BLURB
  Lua is a powerful light-weight programming language designed for extending
  applications. Lua is also frequently used as a general-purpose, stand-alone
  language.
endef

MASTER_SITES = http://www.lua.org/ftp/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Make-shared-lib.patch

VENDOR_URL = http://www.lua.org

LICENSE = doc/readme.html

PACKAGES += CSWlua
SPKG_DESC_CSWlua = Light-weight language designed for extending applications
# PKGFILES is catchall

PACKAGES += CSWliblua5-2
SPKG_DESC_CSWliblua5-2 = Library for the LUA langauge, liblua.so.5.2
PKGFILES_CSWliblua5-2 += $(call pkgfiles_lib,liblua.so.5.2)

PACKAGES += CSWlua-dev
SPKG_DESC_CSWlua-dev = Development files for liblua.so.5.2
PKGFILES_CSWlua-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlua-dev += CSWliblua5-2

REINPLACEMENTS += luaroot
REINPLACE_MATCH_luaroot = (\#define\s+LUA_ROOT\s+).*
REINPLACE_WITH_luaroot = $$1"$(prefix)"
REINPLACE_FILES_luaroot += src/luaconf.h

# No configure
CONFIGURE_SCRIPTS =

EXTRA_CFLAGS += -KPIC

BUILD_ARGS += solaris
BUILD_ARGS += CC=$(CC)
BUILD_ARGS += CFLAGS="$(CFLAGS)"
BUILD_ARGS += MYLIBS="-ldl"
BUILD_ARGS += LDFLAGS="$(LDFLAGS)"

TEST_TARGET = test

INSTALL_ARGS += INSTALL=ginstall
INSTALL_ARGS += INSTALL_TOP=$(DESTDIR)$(prefix)
INSTALL_ARGS += INSTALL_MAN=$(DESTDIR)$(mandir)/man1

include gar/category.mk
