NAME = augeas
VERSION = 0.10.0
CATEGORIES = lib

DESCRIPTION = A configuration editing tool
define BLURB
  Augeas is a configuration editing tool. It parses configuration files in
  their native formats and transforms them into a tree. Configuration changes
  are made by manipulating this tree and saving it back into native config
  files.
endef

MASTER_SITES = http://augeas.net/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
VENDOR_URL = http://augeas.net

BUILD_DEP_PKGS    = CSWlibxml2-2 CSWlibxml2-dev
RUNTIME_DEP_PKGS  = CSWgcc4corert CSWlibgnugetopt
RUNTIME_DEP_PKGS += CSWlibreadline6 CSWlibxml2-2
GARCOMPILER = GCC4
EXTRA_LDFLAGS = -lgnugetopt
PATCHFILES += 0001-fix-compiling-on-solaris.patch \
  0002-regexp-escape.patch \
  0003-Remove-Linux-isms-so-tests-can-run-on-Solaris.patch \
  0004-pkg-config-Augeas-requires-libxml2.patch

# Building on Solaris 10 doesn't work as it support C99 and the above fixes are
# not necessary there.
# Disable 64 bit for now.
# BUILD64 = 1
# NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

CHECKPKG_OVERRIDES_CSWaugeas += file-with-bad-content
CHECKPKG_OVERRIDES_CSWaugeas += non-uniform-lib-versions-in-package|sonames=libaugeas.so.0,libfa.so.1
CHECKPKG_OVERRIDES_CSWaugeas += shared-lib-package-contains-so-symlink

EXTRA_MERGE_EXCLUDE_FILES = .*/charset.alias
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

# Local bin/ for readlink, /opt/csw/gnu for GNU tail, diff
PATH := $(abspath ./bin):/opt/csw/gnu:$(PATH)
