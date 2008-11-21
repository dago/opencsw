GARNAME = make
GARVERSION = 3.80
CATEGORIES = devel

DESCRIPTION = Controls generation of executables and other compile-related tasks
define BLURB
  GNU Make examines the timestamps on a set of interdependent files, and, if
  necessary, issues commands to bring them up-to-date. The user creates a
  makefile describing the files, their relationships, and the commands to run.
  Most often make is used to rebuild libraries and programs when their sources
  are changed, but it can be used for any situation where one set of files needs
  to be generated from another set.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
