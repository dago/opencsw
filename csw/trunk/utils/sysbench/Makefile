GARNAME = sysbench
GARVERSION = 0.4.7
CATEGORIES = utils

DESCRIPTION = System evaluation benchmark
define BLURB
    A modular, cross-platform and multi-threaded benchmark tool for
    evaluating OS parameters that are important for a system running a
    database under intensive load.
endef

MASTER_SITES = http://umn.dl.sourceforge.net/sourceforge/sysbench/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES += $(call admfiles,CSWsysbench,)
DISTFILES += $(call admfiles,CSWsysbench,depend prototype)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include ../category.mk
