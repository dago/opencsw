# Copyright 2008 OpenCSW
#
# Redistribution and/or use, with or without modification, is
# permitted. This software is without warranty of any kind. The
# author(s) shall not be liable in the event that use of the
# software causes damage.

# TODO: Run the test suite
# This assumes that you already have the stage1 compiler installed under ~/opencsw/ghc-bootstrap-$(GARVERSION)
# Download it from http://www.haskell.org/ghc/dist/$(GARVERSION)/maeder/

GARNAME = ghc
GARVERSION = 6.10.4
CATEGORIES = apps

DESCRIPTION = State-of-the-art, compiler and interactive environment for Haskell.
define BLURB
Haskell is an advanced purely functional programming language. An open source
product of more than twenty years of cutting edge research, it allows rapid
development of robust, concise, correct software. With strong support for
integration with other languages, built-in concurrency and parallelism,
debuggers, profilers, rich libraries and an active community, Haskell makes it
easier to produce flexible, maintainable high-quality software
endef

GARCOMPILER = GCC4

REQUIRED_PKGS_CSWghc  = CSWiconv
REQUIRED_PKGS_CSWghc += CSWlibgmp
REQUIRED_PKGS_CSWghc += CSWncurses

# The location of the solaris binaries seems to vary a bit from version to version
MASTER_SITES = http://www.haskell.org/ghc/dist/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION)-src.tar.bz2
PATCHFILES  = 0001-mk-build.mk-Adding-correct-runtime-options.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARVERSION)/$(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

#PKGFILES_CSWghc-prof  = $(prefix)/.*\.p_hi
#PKGFILES_CSWghc-prof += $(prefix)/.*\.so

MERGE_EXCLUDE_STATICLIBS =

PKGFILES_CSWghc  =
PKGFILES_CSWghc  = $(prefix)/.*
PKGFILES_CSWghc += $(prefix)/.*\.a
PKGFILES_CSWghc += $(PKGFILES_DEVEL)
PKGFILES_CSWghc += $(PKGFILES_RT)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gcc=/opt/csw/gcc4/bin/gcc
CONFIGURE_ARGS += --with-gmp-includes=/opt/csw/include
CONFIGURE_ARGS += --with-gmp-libraries=/opt/csw/lib
CONFIGURE_ARGS += --with-readline-includes=/opt/csw/include
CONFIGURE_ARGS += --with-readline-libraries=/opt/csw/lib
CONFIGURE_ENV  = PATH=$(HOME)/opencsw/ghc-bootstrap-6.10.4/bin:$(PATH)

BUILD_ENV  = PATH=$(HOME)/opencsw/ghc-bootstrap-6.10.4/bin:$(PATH) LD_LIBRARY_PATH=/opt/csw/lib

# Disabled for now
TEST_SCRIPTS =

include gar/category.mk
