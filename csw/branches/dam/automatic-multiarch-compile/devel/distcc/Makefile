GARNAME = distcc
GARVERSION = 3.0
CATEGORIES = devel

DESCRIPTION = Distributed compilation for faster C/C++ builds
define BLURB
  distcc is a program to distribute builds of C, C++, Objective C or
  Objective C++ code across several machines on a network. distcc should
  always generate the same results as a local build, is simple to install
  and use, and is usually much faster than a local compile.
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWdistcc,)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
