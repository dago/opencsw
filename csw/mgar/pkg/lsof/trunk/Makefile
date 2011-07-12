# TBD:
# - Probably VxFS bindings

NAME = lsof
VERSION = 4.84
CATEGORIES = utils

DESCRIPTION = List open files
define BLURB
  Lsof is a Unix-specific diagnostic tool. Its name stands for LiSt Open Files,
  and it does just that. It lists information about any files that are open by
  processes currently running on the system. It can also list communications
  open by each process.
endef

MASTER_SITES = ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof/
DISTNAME = $(NAME)_$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += lsof-license

# This seems to be necessary as the above comment says
PATCHFILES += 0001-Use-lgrp.h.patch

SRCDIST = $(DISTNAME)_src
WORKSRC   = $(WORKDIR)/$(DISTNAME)/$(SRCDIST)

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

VENDOR_URL = http://people.freebsd.org/~abe/
LICENSE = lsof-license

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS    = -n solariscc

TEST_SCRIPTS = custom

# Tests require root
SKIPTEST ?= 1

INSTALL_SCRIPTS = custom

# Environment variables affecting Solaris builds:
#   SOLARIS_23P101318     If this environment variable has a non-NULL value, the
#   SOLARIS_24P101945     If this environment variable has a non-NULL value, the
#   SOLARIS_24P102303     If this environment variable has a non-NULL value, the
#   SOLARIS_26PR_GWINDOWS If this environment variable has a value of "Y" or "y",
#   SOLARIS_26PR_LDT      If this environment variable has a value of "Y" or "y",
#   SOLARIS_CCDIR         specifies the path to the Sun C compiler -- i.e., when
#   SOLARIS_INSTR         specifies the Sun C compiler target instruction set
#   SOLARIS_KERNBITS      specifies the number of bits in the Solaris 7, 8, 9 or
#   SOLARIS_VSOCK         If this environment variable has a value of "Y" or "y",
#   SOLARIS_VXFSINCL      This environment variable defines the path to the
#   SOLARIS_VXFSLIB               This environment variable defines the path to the

CONFIGURE_EXPORTS = LSOF_CFGF SOLARIS_CCDIR SOLARIS_INSTR SOLARIS_KERNBITS
SOLARIS_CCDIR = $(CC_HOME)/bin
SOLARIS_INSTR = $(ISA)
SOLARIS_KERNBITS = $(MEMORYMODEL)

BUILD_OVERRIDE_VARS = CDEF
BUILD_OVERRIDE_VAR_CDEF = $(CFLAGS)

PROTOTYPE_MODIFIERS = lsof
PROTOTYPE_FILES_lsof = $(bindir)/lsof
PROTOTYPE_GROUP_lsof = sys
PROTOTYPE_PERMS_lsof = 2755

include gar/category.mk

INSTALLISADIR ?= $(WORKROOTDIR)/install-$(MODULATION)

post-extract-modulated:
	@echo " ==> Extracting source distribution"
	@$(if $(filter-out global,$(MODULATION)),( cd $(WORKDIR)/$(DISTNAME) ; tar xf $(SRCDIST).tar ))
	@$(MAKECOOKIE)

configure-custom:
	@echo " ==> Configuring in $(WORKSRC)"
	( cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing in $(WORKSRC)/tests"
	$(MAKE) -C $(WORKSRC)/tests
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) $(VERSION) for $(MODULATION)"
	echo DESTDIR: $(DESTDIR)
	@( cd $(WORKSRC) ; \
		ginstall -d $(DESTDIR)$(bindir) ; \
		ginstall -m 755 lsof $(DESTDIR)$(bindir) ; \
		ginstall -d $(DESTDIR)$(mandir)/man8 ; \
		ginstall -m 444 lsof.8 $(DESTDIR)$(mandir)/man8 )
	@$(MAKECOOKIE)
