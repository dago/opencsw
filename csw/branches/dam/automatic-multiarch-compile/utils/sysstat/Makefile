GARNAME = sysstat
GARVERSION = 20080501
CATEGORIES = utils

DESCRIPTION = Complementary tool for system observation
define BLURB
  sysstat is thought to be a complementary tool in the list of utilities
  included in Solaris for system observation (prstat, vmstat, iostat, mpstat,
  nfsstat, netstat, ...). It provides an overall view of the current system
  performance. Its key feature is to present all most important performance
  metrics to the user at a single glance. Use it to get a general idea of
  what is happening on the system. If you encounter any bottlenecks,
  please ask the standard board utilities for more detailed statistics to
  find out what is going on. sysstat might point you into the right direction,
  but it probably won't be able to give you all the information you need
  in more complex scenarios.
endef

MASTER_SITES = http://www.maier-komor.de/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWsysstat)

CONFIGURE_SCRIPTS = custom

BUILD64 = 1

TEST_TARGET =

include ../category.mk

configure-custom: $(WORKSRC)/mkrules
	@cat $(WORKSRC)/mkrules

$(WORKSRC)/mkrules:
	@echo | /usr/bin/tee mkrules << MAKERULES
OS              = $OS
INSTALL         = $install
CC              = $CC
C_CFLAGS        = $cflags -DSOLARIS=$solaris
D_CFLAGS        = $cflags $d_cflags -DSOLARIS=$solaris
CDIR            = $OS-$PROC
DDIR            = daemon-$KERNEL
C_LIBS          += $lflags
PREFIX          = $prefix
modules: $modules
install: $toinstall
MAKERULES

