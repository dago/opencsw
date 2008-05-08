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

DIRS="/usr/local /opt/sfw /opt/csw /usr/local /opt/local $HOME /usr"
OS=`/usr/bin/uname -s`
PROC=`/usr/bin/uname -m`

        BITS=`/usr/bin/isainfo -b`
        KERNEL=`/usr/bin/isainfo -k`
SOLARIS_RELEASE = $(shell /usr/bin/uname -r | /usr/bin/cut -d. -f2)
SOLARIS_PROC = $(shell /usr/bin/uname -m)
        modules="\$(CDIR)/sysstat \$(DDIR)/sysstatd"
        toinstall="install_sysstatd install_sysstat"
        install=/usr/sbin/install


$(WORKSRC)/mkrules:
	@echo | /usr/bin/tee mkrules << MAKERULES
OS              = SunOS
INSTALL         = /usr/sbin/install
CC              = ${CC}
C_CFLAGS        = ${CFLAGS} -DSOLARIS=$(SOLARIS_RELEASE)
D_CFLAGS        = $cflags $d_cflags -DSOLARIS=$(SOLARIS_RELEASE)
CDIR            = SunOS-$(SOLARIS_PROC)
DDIR            = daemon-$(ISA)
C_LIBS          += $lflags
PREFIX          = $(prefix)
modules: $(bindir)/sysstat $(bindir)/sysstatd
install: install_sysstatd install_sysstat
MAKERULES

