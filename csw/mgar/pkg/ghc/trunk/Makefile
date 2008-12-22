# Copyright 2008 OpenCSW
#
# Redistribution and/or use, with or without modification, is
# permitted. This software is without warranty of any kind. The
# author(s) shall not be liable in the event that use of the
# software causes damage.

# TODO: Unpack the bootstrap binaries. Right now they're assumed to be installed under /tmp/ghc. 
#       Might not be too useful when re-building this package.

GARNAME = ghc
GARVERSION = 6.8.3
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

# Calculate the correct platform specification for ghc to use when bootstrapping
ifeq ($(shell uname -p),sparc)
GHC_PLATFORM = sparc-sun
else
GHC_PLATFORM = i386-unknown
endif

# The location of the solaris binaries seems to vary a bit from version to version

MASTER_SITES = http://www.haskell.org/ghc/dist/$(GARVERSION)/ http://www.haskell.org/ghc/dist/$(GARVERSION)/maeder/
DISTFILES  = $(GARNAME)-$(GARVERSION)-src.tar.bz2 ghc-$(GARVERSION)-$(GHC_PLATFORM)-solaris2.tar.bz2 testsuite-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSW$(GARNAME),)
DISTFILES += $(call admfiles,CSW$(GARNAME)-prof,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARVERSION)/$(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PKGFILES_CSWghc-prof = $(prefix)/.*\.p_hi

CONFIGURE_ARGS  = $(DIRPATHS)
# Disabled for now
TEST_SCRIPTS =
#TEST_SCRIPTS = custom

include gar/category.mk

PATH := /tmp/ghc/bin:$(PATH)

LD_LIBRARY_PATH=/opt/csw/lib
export LD_LIBRARY_PATH

# This might not be needed anymore
pre-build-modulated:
	@( cd $(WORKSRC); $(MAKE) -C utils/pwd boot )

pre-test-custom:
	@echo Extracting the testsuite
	@( echo cd $(WORKSRC); echo gtar jxf $(DOWNLOADDIR)/testsuite-$(GARVERSION).tar.gz)
	false
	@$(MAKECOOKIE)

test-custom:
	@echo *******************************
	@echo *** RUNNING TESTS (not)
	@echo *******************************
	@( cd $(WORKSRC)/testsuite/tests/ghc-regress; echo $(MAKE) stage=2 )
	@$(MAKECOOKIE)
