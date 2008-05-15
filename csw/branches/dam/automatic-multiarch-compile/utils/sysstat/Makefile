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

# Put manpages in share/man/ instead of man/
PATCHFILES = patch-sysstat-shareman.diff

# skip extra dir-hierarchie from isaexec
PATCHFILES += patch-isaexec-compat.diff

CONFIGURE_SCRIPTS = custom

# As kernel data is accessed we need separate builds for 32 and 64 bit
# choosen by the current kernel with isaexec
BUILD64 = 1

# The package doesn't have a test script
TEST_TARGET =

include ../category.mk

# We don't have a autoconf-style configure. The configure script
# supplied with the package is custom made and is not flexible
# enough to set all necessary parameters, so we generate the
# resulting parametrization directly.
configure-custom: $(WORKSRC)/mkrules
	@cat $<

$(WORKSRC)/mkrules:
	@(	echo "OS              = SunOS"; \
		echo "INSTALL         = /usr/sbin/install"; \
		echo "CC              = ${CC}"; \
		echo "C_CFLAGS        = ${CFLAGS} -DUSECURSES -DSOLARIS=`echo ${GAROSREL} | sed -e 's/5\.//'`"; \
		echo "D_CFLAGS        = ${CFLAGS} -DUSECURSES -DSOLARIS=`echo ${GAROSREL} | sed -e 's/5\.//'`"; \
		echo "CDIR            = SunOS-`uname -m`"; \
		echo "DDIR            = daemon-${ISA}"; \
		echo "C_LIBS          += ${LDFLAGS} -lcurses -lsocket -lnsl"; \
		echo "PREFIX          = ${DESTDIR}${prefix}"; \
		echo "modules:        $$(CDIR)/sysstat $$(DDIR)/sysstatd"; \
		echo "install:        install_sysstatd install_sysstat" \
	) > $@
