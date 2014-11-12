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

RUNTIME_DEP_PKGS_augeas += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_augeas += CSWlibfa1
RUNTIME_DEP_PKGS_augeas += CSWlibxml2-2
RUNTIME_DEP_PKGS_augeas += CSWlibgcc-s1

PACKAGES = CSWaugeas
SPKG_DESC_CSWaugeas = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWaugeas += $(RUNTIME_DEP_PKGS_augeas)
RUNTIME_DEP_PKGS_CSWaugeas += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWaugeas += CSWlibaugeas0

PACKAGES += CSWlibaugeas-dev
SPKG_DESC_CSWlibaugeas-dev = The libaugeas development files
PKGFILES_CSWlibaugeas-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibaugeas-dev += CSWlibfa1
RUNTIME_DEP_PKGS_CSWlibaugeas-dev += CSWlibaugeas0

PACKAGES += CSWlibaugeas0
SPKG_DESC_CSWlibaugeas0 = The libaugeas.so.* files 
PKGFILES_CSWlibaugeas0 = $(call pkgfiles_lib,libaugeas.so.0)   
RUNTIME_DEP_PKGS_CSWlibaugeas0 = $(RUNTIME_DEP_PKGS_augeas)

PACKAGES += CSWlibfa1
SPKG_DESC_CSWlibfa1 = The libfa.so.* files
PKGFILES_CSWlibfa1 = $(call pkgfiles_lib,libfa.so.1)   
RUNTIME_DEP_PKGS_CSWlibfa1 += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibfa1 += CSWlibgcc-s1

BUILD64_LIBS_ONLY = 1

BUILD_DEP_PKGS += CSWlibxml2-2
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWgcc4core
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibgnugetopt-dev
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWcoreutils

CHECKPKG_OVERRIDES_CSWaugeas += surplus-dependency|CSWlibxml2-2
CHECKPKG_OVERRIDES_CSWaugeas += surplus-dependency|CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWaugeas += surplus-dependency|CSWlibgnugetopt0
CHECKPKG_OVERRIDES_CSWlibfa1 += surplus-dependency|CSWlibgnugetopt0
CHECKPKG_OVERRIDES_CSWlibaugeas0 += surplus-dependency|CSWlibgnugetopt0

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

EXTRA_MERGE_EXCLUDE_FILES = .*/charset.alias
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

# Local bin/ for readlink, /opt/csw/gnu for GNU tail, diff
PATH := $(abspath ./bin):/opt/csw/gnu:$(PATH)
