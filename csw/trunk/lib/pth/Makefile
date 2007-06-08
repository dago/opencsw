GARNAME = pth
GARVERSION = 2.0.7
CATEGORIES = lib

DESCRIPTION = The GNU Portable Threads
define BLURB
  Pth is a very portable POSIX/ANSI-C based library for Unix platforms which
  provides non-preemptive priority-based scheduling for multiple threads of
  execution (aka ``multithreading'') inside event-driven applications
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpth,)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
