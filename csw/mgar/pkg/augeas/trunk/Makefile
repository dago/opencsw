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

PACKAGES = CSWaugeas CSWlibaugeas0-19-0 CSWlibfa1-4-0

SPKG_DESC_CSWaugeas = $(DESCRIPTION)
SPKG_DESC_CSWlibaugeas0-19-0 = The libaugeas.so.0.* files 
SPKG_DESC_CSWlibfa1-4-0 = The libfa.so.1.* files

PKGFILES_CSWlibaugeas0-19-0 = $(libdir)/libaugeas.so.*
PKGFILES_CSWlibfa1-4-0 = $(libdir)/libfa.so.*

BUILD_DEP_PKGS = CSWlibxml2-2
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWgcc4core
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibgnugetopt-dev
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWcoreutils

RUNTIME_DEP_PKGS_augeas = CSWlibreadline6
RUNTIME_DEP_PKGS_augeas += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_augeas += CSWlibfa1-4-0
RUNTIME_DEP_PKGS_augeas += CSWlibxml2-2
RUNTIME_DEP_PKGS_augeas += CSWlibgcc-s1

RUNTIME_DEP_PKGS_CSWaugeas = $(RUNTIME_DEP_PKGS_augeas) 
RUNTIME_DEP_PKGS_CSWaugeas += CSWlibaugeas0-19-0

RUNTIME_DEP_PKGS_CSWlibaugeas0-19-0 = $(RUNTIME_DEP_PKGS_augeas)

RUNTIME_DEP_PKGS_CSWlibfa1-4-0 = CSWlibgnugetop0
RUNTIME_DEP_PKGS_CSWlibfa1-4-0 = CSWlibgcc-s1

GARCOMPILER = GCC4
EXTRA_LDFLAGS = -lgnugetopt

# Building on Solaris 10 doesn't work as it support C99 and the above fixes are
# not necessary there.
# Disable 64 bit for now.
# BUILD64 = 1
# NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

# test are currently failing (sudo, sip_conf)
#SKIPTEST=1

EXTRA_MERGE_EXCLUDE_FILES = .*/charset.alias
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

# Local bin/ for readlink, /opt/csw/gnu for GNU tail, diff
PATH := $(abspath ./bin):/opt/csw/gnu:$(PATH)
