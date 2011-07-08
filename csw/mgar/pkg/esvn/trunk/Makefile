NAME = esvn
VERSION = 0.6.11_1
DISTVERSION = $(subst _,-,$(VERSION))
GARTYPE = v1
CATEGORIES = utils

DESCRIPTION = A GUI frontend to the Subversion revision system
define BLURB
  A GUI frontend to the Subversion revision system.
endef

MASTER_SITES = http://esvn.umputun.com/
DISTFILES = $(NAME)-$(DISTVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(NAME)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Specs and pre-built prototypes
#DISTFILES += CSWesvn.gspec
#DISTFILES += CSWesvn.gspec CSWesvn.prototype

# Patch hard coded install paths
PATCHFILES += cswbuild.diff

# No test suite
TEST_SCRIPTS =

GARCOMPILER = GNU
CONFIGURE_SCRIPTS =

include gar/category.mk

QTDIR = $(prefix)/kde-gcc
export QTDIR

PATH := $(PATH):$(QTDIR)/bin
export PATH

