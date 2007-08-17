GARNAME = setoolkit
GARVERSION = snapshot
CATEGORIES = utils

DESCRIPTION = A system performance monitoring tool
define BLURB
  The SE Toolkit is
  * An interpreter for a programming language that is both a subset of C and C++.
    Syntactically, it looks like C, but it contains a limited class mechanism.
  * Include files for use by toolkit scripts.
  * A bunch of example scripts.
  * A set of extensions for writing GUIs and "network aware" scripts.
endef

sparc_ARCH  = sparc
i386_ARCH   = i386
sparc_ARCH64 = sparcv9
i386_ARCH64  = amd64

ARCH=$($(GARCH)_ARCH)
ARCH64=$($(GARCH)_ARCH64)

ifdef ISA
ISALIST = $(ISA)
else
ISA = $(ARCH)
endif

#SF_PROJ = setoolkit
#MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsetoolkit,prototype)
#DISTFILES += $(call admfiles,CSWsetoolkit,prototype depend)

WORKDIR       = $(WORKROOTDIR)/$(DESTIMG).d/$(ISA)
COOKIEROOTDIR = cookies.$(ISA)

CONFIGURE_ARGS = $(DIRPATHS)
WORKSRC = $(WORKDIR)/se

# Optimizer flags for architecture
OPTARCH_sparcv9 = v9
OPTARCH_amd64   = amd64

INSTALL_SCRIPTS = custom

CLEAN_SCRIPTS = custom

include ../category.mk

# Default is -xO3 which breaks se on Sun Studio 12 in run.c:
#(dbx) list 2710,2730
# 2710   {
# 2711     T_RETURN *rp = sp->s_un.s_return;
# 2712     T_STATEMENT statement;
# 2713     T_ASSIGN assign;
# 2714   
# 2715     /* returning an expression */
# 2716     if (rp->ret_expr) {
# 2717       assign.a_variable = rp->ret_block->b_return;
# 2718       assign.a_op = A_ASSIGN;
# 2719       assign.a_expression = rp->ret_expr;
# 2720       statement.s_un.s_assign = &assign;
# 2721       run_assign(&statement);
# 2722     }
# 2723     longjmp(sp->s_un.s_return->ret_block->b_jmpbuf, 1);		<-- Dumps core
# 2724   }
# 2725   
# 2726   static void
# 2727   run_break(T_STATEMENT *sp)
# 2728   {
# 2729     T_BREAK *bp = sp->s_un.s_break;
# 2730   
SUN_CC_OPT  = -xO2 -xarch=$(OPTARCH) -xspace -xildoff
SUN_CXX_OPT = -xO2 -xarch=$(OPTARCH) -xspace -xildoff

CFLAGS += -g

ifdef ISA
OPTARCH = $(OPTARCH_$(ISA))
endif

# ARCH      is where things get installed (e.g. bin/$(ARCH)/, lib/$(ARCH)/, ...)
# WORKDIR   is the source of most files
# WORKDIR64 is the source of 64 bit files
MKPACKAGE_ARGS = \
	-v arch=$(ARCH)		-v arch64=$(ARCH64) \
	-v se=se.$(ARCH)	-v se64=se.$(ARCH64) \
	-v WORKDIR=se		-v WORKDIR64=../$(ARCH64)/se

env:
	@echo "      GARCH = $(GARCH)"
	@echo " GARVERSION = $(GARVERSION)"
	@echo "        ISA = $(ISA)"
	@echo "     CFLAGS = $(CFLAGS)"
	@echo "    OPTARCH = $(OPTARCH)"

pre-configure:
	@echo "==> Auto-reconfiguring"
	@(cd $(WORKSRC); autoreconf -if)
	$(MAKECOOKIE)

install-custom:
	# Nothing gets installed, everything is picked up on packaging
	$(MAKECOOKIE)

pre-package:
	@echo " ==> Building 64 bit version"
	gmake ISA=$(ARCH64) build
	$(MAKECOOKIE)

clean-custom: clean-all
	gmake ISA=$(ARCH64) clean-all

