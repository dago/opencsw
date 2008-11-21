GARNAME = setoolkit
GARVERSION = 3.5.0.b1
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
ifndef DO64
ISA = $(ARCH)
else
ISA = $(ARCH64)
endif
endif

#SF_PROJ = setoolkit
#MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsetoolkit,prototype depend)

WORKDIR       = $(WORKROOTDIR)/$(DESTIMG).d/$(ISA)
COOKIEROOTDIR = cookies.$(ISA)

CONFIGURE_ARGS = $(DIRPATHS)

# Optimizer flags for architecture
OPTARCH_sparcv9 = v9
OPTARCH_amd64   = amd64

OPTDIR32 = $(shell $(GARBIN)/isadir $(OPTARCH_$(ARCH)))
OPTDIR64 = $(shell $(GARBIN)/isadir $(OPTARCH_$(ARCH64)))

# Package doesn't have test
SKIPTEST = 1

INSTALL_SCRIPTS = custom
CLEAN_SCRIPTS = custom

include ../category.mk

# CFLAGS += -g

ifdef ISA
OPTARCH = $(OPTARCH_$(ISA))
endif

# ARCH      is where things get installed (e.g. bin/$(ARCH)/, lib/$(ARCH)/, ...)
# WORKDIR   is the source of most files
# WORKDIR64 is the source of 64 bit files
MKPACKAGE_ARGS = \
	-v garname=$(GARNAME) \
	-v arch=$(ARCH)		-v arch64=$(ARCH64) \
	-v optdir32=$(OPTDIR32)	-v optdir64=$(OPTDIR64) \
	-v WORKDIR=$(GARNAME)-$(GARVERSION) \
				-v WORKDIR64=../$(ARCH64)/$(GARNAME)-$(GARVERSION)

env:
	@echo "      GARCH = $(GARCH)"
	@echo " GARVERSION = $(GARVERSION)"
	@echo "        ISA = $(ISA)"
	@echo "     CFLAGS = $(CFLAGS)"
	@echo "    OPTARCH = $(OPTARCH)"

#pre-configure:
#	@echo "==> Auto-reconfiguring"
#	@(cd $(WORKSRC); autoreconf -if)
#	$(MAKECOOKIE)

build64:
	@echo " ==> Building 64 bit version"
	gmake DO64=1 build
	$(MAKECOOKIE)

install-custom: build build64
	# Nothing gets installed, everything is picked up on packaging
	$(MAKECOOKIE)

#pre-package:
#	@echo " ==> Building 64 bit version"
#	gmake ISA=$(ARCH64) build
#	$(MAKECOOKIE)

clean64:
	gmake DO64=1 clean-all

clean-custom: clean64 clean-all

