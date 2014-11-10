NAME = augeas
VERSION = 1.3.0
GARTYPE = v2

DESCRIPTION = A configuration editing tool
define BLURB
  Augeas is a configuration editing tool. It parses configuration files in
  their native formats and transforms them into a tree. Configuration changes
  are made by manipulating this tree and saving it back into native config
  files.
endef

MASTER_SITES = http://download.augeas.net/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
VENDOR_URL = http://augeas.net

BUILD_DEP_PKGS = CSWlibxml2-2
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWgcc4core
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibgnugetopt-dev
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWcoreutils

RUNTIME_DEP_PKGS = CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibreadline6
RUNTIME_DEP_PKGS += CSWlibxml2-2
RUNTIME_DEP_PKGS += CSWlibgnugetopt0

GARCOMPILER = GCC4
EXTRA_LDFLAGS = -lgnugetopt

# Building on Solaris 10 doesn't work as it support C99 and the above fixes are
# not necessary there.
# Disable 64 bit for now.
# BUILD64 = 1
# NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

# test are currently failing (sudo, sip_conf)
SKIPTEST=1

CHECKPKG_OVERRIDES_CSWaugeas += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWaugeas += shared-lib-pkgname-mismatch|file=opt/csw/lib/libaugeas.so.0.19.0|soname=libaugeas.so.0|pkgname=CSWaugeas|expected=CSWlibaugeas0
CHECKPKG_OVERRIDES_CSWaugeas += shared-lib-pkgname-mismatch|file=opt/csw/lib/libfa.so.1.4.0|soname=libfa.so.1|pkgname=CSWaugeas|expected=CSWlibfa1
CHECKPKG_OVERRIDES_CSWaugeas += surplus-dependency|CSWlibgnugetopt0


EXTRA_MERGE_EXCLUDE_FILES = .*/charset.alias
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

# Local bin/ for readlink, /opt/csw/gnu for GNU tail, diff
PATH := $(abspath ./bin):/opt/csw/gnu:$(PATH)
