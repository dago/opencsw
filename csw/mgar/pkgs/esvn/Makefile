GARNAME = esvn
GARVERSION = 0.6.11_1
DISTVERSION = $(subst _,-,$(GARVERSION))
CATEGORIES = utils

DESCRIPTION = A GUI frontend to the Subversion revision system
define BLURB
  A GUI frontend to the Subversion revision system.
endef

MASTER_SITES = http://esvn.umputun.com/
DISTFILES = $(GARNAME)-$(DISTVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(GARNAME)

# Specs and pre-built prototypes
#DISTFILES += CSWesvn.gspec
#DISTFILES += CSWesvn.gspec CSWesvn.prototype

# Patch hard coded install paths
PATCHFILES += cswbuild.diff

# No test suite
TEST_SCRIPTS =

GARCOMPILER = GNU
CONFIGURE_SCRIPTS =

include ../category.mk

QTDIR = $(prefix)/kde-gcc
export QTDIR

PATH := $(PATH):$(QTDIR)/bin
export PATH

