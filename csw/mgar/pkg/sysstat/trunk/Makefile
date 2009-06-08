GARNAME = sysstat
GARVERSION = 20090606
CATEGORIES = utils

DESCRIPTION = Key system statistics at a glance
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

REQUIRED_PKGS = CSWncurses

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.maier-komor.de/sysstat.html

PATCHFILES = patch-onlyisaexec-sysstatd.diff

CONFIGURE_SCRIPTS = custom

# As kernel data is accessed we need separate builds for 32 and 64 bit
# choosen by the current kernel with isaexec
BUILD64 = 1

# There are no optimized libraries
NOISALIST = 1

MKRULES_MODULES_32 = daemon/sysstatd app/sysstat
MKRULES_MODULES_64 = daemon/sysstatd
MKRULES_MODULES = $(MKRULES_MODULES_$(MEMORYMODEL))

MKRULES_INSTALL_32 = install_sysstatd install_sysstat
MKRULES_INSTALL_64 = install_sysstatd
MKRULES_INSTALL = $(MKRULES_INSTALL_$(MEMORYMODEL))

# The package doesn't have a test script
TEST_TARGET =

INSTALL_SCRIPTS = custom

# The main sysstat binary is 32 bit only, kernel access is
# only done via sysstatd which uses isaexec.
ISAEXEC_FILES = $(sbindir)/sysstatd

PROTOTYPE_FILTER = awk '$$$$3 ~ /\/sysstatd$$$$/ { $$$$4 = "4755" } { print }'

include gar/category.mk

# We don't have a autoconf-style configure. The configure script
# supplied with the package is custom made and is not flexible
# enough to set all necessary parameters, so we generate the
# resulting parametrization directly.
configure-custom: $(WORKSRC)/mkrules
	@cat $<
	@$(MAKECOOKIE)

QUOTED_LDFLAGS = $(shell echo '$(LDFLAGS)')
SOLARIS = $(shell echo ${GAROSREL} | sed -e 's/5\.//')

$(WORKSRC)/mkrules:
	@(	echo "OS              = SunOS"; \
		echo "INSTALL         = /usr/sbin/install"; \
		echo "CC              = ${CC}"; \
		echo "C_CFLAGS        = ${CFLAGS} -xc99=no_lib -I$(includedir)/ncurses -DUSECURSES -DSOLARIS=$(SOLARIS)"; \
		echo "D_CFLAGS        = ${CFLAGS} -xc99=no_lib -I$(includedir)/ncurses -DUSECURSES -DSOLARIS=$(SOLARIS)"; \
		echo "CDIR            = app"; \
		echo "DDIR            = daemon"; \
		echo 'C_LIBS          += $(LDFLAGS) -lncurses -lsocket -lnsl'; \
		echo 'LIBS            = '; \
		echo "PREFIX          = ${DESTDIR}${prefix}"; \
		echo "ISAEXEC         = ${bindir}/isaexec"; \
		echo "MKDEP           = ${CC} -xM1 ${CFLAGS} -I$(includedir)/ncurses"; \
		echo "modules:        $(MKRULES_MODULES)"; \
		echo "install:        $(MKRULES_INSTALL)"; \
	) > $@

install-custom:
	if [ -f $(WORKSRC)/app/sysstat ]; then ginstall -D $(WORKSRC)/app/sysstat $(DESTDIR)$(bindir)/sysstat; fi
	# The next line installs the binary with the correct permissions, but fails if the package
	# is build without root-permissions. Therefore the binaries are installed with default
	# permissions which are fixed during install with the provided prototype.
	#ginstall -D -m 04755 -o root -g bin $(WORKSRC)/daemon/sysstatd $(DESTDIR)$(sbindir)/sysstatd
	ginstall -D $(WORKSRC)/daemon/sysstatd $(DESTDIR)$(sbindir)/sysstatd
	ginstall -D $(WORKSRC)/sysstat.1m $(DESTDIR)$(mandir)/man1/sysstat.1m
	@$(MAKECOOKIE)
