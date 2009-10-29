GARNAME = lsof
GARVERSION = 4.81
CATEGORIES = utils

DESCRIPTION = List open files
define BLURB
  Lsof is a Unix-specific diagnostic tool. Its name stands for LiSt Open Files,
  and it does just that. It lists information about any files that are open by
  processes currently running on the system. It can also list communications
  open by each process.
endef

MASTER_SITES = ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof/
TOPDIST   = $(GARNAME)_$(GARVERSION)
SRCDIST   = $(TOPDIST)_src
DISTFILES = $(TOPDIST).tar.bz2
WORKSRC   = $(WORKDIR)/$(TOPDIST)/$(SRCDIST)

SPKG_SOURCEURL = http://people.freebsd.org/~abe/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)_(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS    = -n solariscc

TEST_SCRIPTS = custom
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
SOLARIS_CCDIR = $(CC_HOME)
SOLARIS_INSTR = $(ISA)
SOLARIS_KERNBITS = $(MEMORYMODEL)

include gar/category.mk

post-extract-modulated:
	@echo " ==> Extracting source distribution"
	@( cd $(WORKDIR)/$(TOPDIST) ; tar xf $(SRCDIST).tar )

configure-custom:
	@echo " ==> Configuring in $(WORKSRC)"
	( cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) )

test-custom-modulated:
	@echo " ==> Testing in $(WORKSRC)/tests"
	@$(MAKE) -C $(WORKSRC)/tests

install-custom-modulated:
	@echo " ==> Installing $(GARNAME) $(GARVERSION)"
	@( cd $(WORKSRC) ; \
		install -m 2755 -g sys lsof $(DESTDIR)$(bindir) ; \
		install -d $(DESTDIR)$(mandir)/man8 ; \
		install -m 444 lsof.8 $(DESTDIR)$(mandir)/man8 )
