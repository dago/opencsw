# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = nodejs
VERSION = 0.10.31
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Node.js JavaScript interpreter
define BLURB
endef

MASTER_SITES = http://nodejs.org/dist/v$(VERSION)/
DISTNAME = node-v$(VERSION)
DISTFILES += $(DISTNAME).tar.gz

LICENSE = LICENSE

PACKAGING_PLA1-sparc solaris11-i386
GARCOMPILER = GNU

BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibcares-devspath $(WORKSRC))

RUNTIME_DEP_PKGS_CSWnodejs += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWnodejs += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWnodejs += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWnoRUNTIME_DEP_PKGS_CSWnodejs += CSWlibcares2
CHECKPKG_OVERRIDES_CSWnodejs += missing-dependency|CSWemacs-common
CHECKPKG_OVERRIDES_CSWnodejs += file-with-bad-content
CHECKPKG_OVERRIDES_CSWnodejs += discouraged-path-in-pkgmap|/opt/csw/lib/node_modules/npm/node_modules/request/node_modules/qs/.gitmodules

# Pathes are difficult to adjust, skip 64 bit for now
# BUILD64 = 1

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --shared-openssl-prefix=$(prefix)
CONFIGURE_ARGS += --openssl-includes=$(includedir)
CONFIGURE_ARGS += --openssl-lCONFIGURE_ARGS += --shared-zlib
CONFIGURE_ARGS += --shared-zlib-include=$(includedir)
CONFIGURE_ARGS += --shared-zlib-libpath=$(libdir)
CONFIGURE_ARGS += --shared-cares
CONFIGURE_ARGS += --shared-cares-includes=$(includedir)
CONFIGURE_ARGS += --shared-cares-libpath=$(libdir)
CPU-32 = ia32
CPU-64 = x64
CONFIGURE_ARGS += --dest-cpu=$(CPU-$(MEMORYMODEL))

# Node.js needs to find objdump from binutils, gobjdump is not sufficient,
# otherwise strange error like this occur:
#   dtrace: failed to compile script src/v8ustack.d: line 399: failed to resolve V8DBG_OFF_FP_CONTEXT: Unknown variable name
# https://github.com/joyent/node/issues/7933
CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)
BUILD_ENV_PATH = /opt/csw/gnu:$(PATH)

TEST_TARGET = test

# There are some tests failing, mostly because of too low limits for open filedescriptors and timeouts
SKIPTEST ?= 1

include gar/category.mk
