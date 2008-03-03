# TODO:
#  - Test the build in Solaris 8 environment -- including SPARC.
#    I currently have only tested this package on Solaris Express x86.
# 
#  - Fix mysql dependency. It currently builds against SUNWmysqlu;
#    this needs to be changed to CSWmysql5rt
#
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
