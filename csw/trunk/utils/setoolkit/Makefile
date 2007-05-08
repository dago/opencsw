GARNAME = setoolkit
GARVERSION = current-r26
CATEGORIES = utils

DESCRIPTION = A system performance monitoring tool
define BLURB
  The SE Toolkit is
  * An interpreter for a programming language that is both a subset of C and C++.
    Syntactically, it looks like C, but it contains a limited class mechanism.
  * Include files for use by toolkit scripts.
  * A bunch of example scripts.
  * A set of extensions for writing GUIs and "network aware" scripts.
endef

MASTER_SITES = 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsetoolkit,)

CONFIGURE_ARGS = $(DIRPATHS)
WORKSRC = $(WORKDIR)/se

include ../category.mk

pre-configure:
	@echo "==> Auto-reconfiguring"
	@(cd $(WORKSRC); autoreconf -if)
