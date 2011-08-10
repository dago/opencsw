# $Id$
#
NAME = ppl
VERSION = 0.11.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Parma Polyhedra Library
define BLURB
endef

BUILD_DEP_PKGS = CSWlibgmp-dev
BUILD_DEP_PKGS += CSWlibmpfr-dev
BUILD_DEP_PKGS += CSWlibmpc-dev
BUILD_DEP_PKGS += CSWgm4

MASTER_SITES = http://www.cs.unipr.it/ppl/Download/ftp/releases/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.cs.unipr.it/ppl/

# C++ bindings require the consistency between GMP, PPL and GCC.
GARCOMPILER = GNU

BUILD64 = 1

# Undefined symbol __sync_fetch_and_add_4
# http://www.mail-archive.com/maintainers@lists.opencsw.org/msg06095.html
# http://opencsw.wikidot.com/porting-faq#toc6
ifeq ($(ISA),sparcv8)
OPT_FLAGS_GCC = -O0
endif
ifeq ($(ISA),i386)
OPT_FLAGS_GCC = -O0
endif

# http://wiki.opencsw.org/porting-faq#toc13
RUNTIME_DEP_PKGS = $(RUNTIME_DEP_PKGS_$(GAROSREL))
RUNTIME_DEP_PKGS_5.9 = CSWlibgnugetopt
EXTRA_LDFLAGS = $(EXTRA_LDFLAGS_$(GAROSREL))
EXTRA_LDFLAGS_5.9 = -lgnugetopt

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# To help the configure script find GNU M4
PATH := /opt/csw/gnu:$(PATH)
