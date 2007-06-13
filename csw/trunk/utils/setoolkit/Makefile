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

include ../category.mk

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

INSTALL_SCRIPTS = custom
install-custom:
	# Nothing gets installed, everything is picked up on packaging
	$(MAKECOOKIE)

pre-package:
	@echo " ==> Building 64 bit version"
	gmake ISA=$(ARCH64) build
	$(MAKECOOKIE)

post-clean:
	@gmake ISA=$(ARCH64) clean

