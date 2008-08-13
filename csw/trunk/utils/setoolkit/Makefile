GARNAME = setoolkit
GARVERSION = 3.5.0-dev-1
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
DISTFILES += $(call admfiles,CSWsetoolkit,depend)

WORKDIR       = $(WORKROOTDIR)/$(DESTIMG).d/$(ISA)
COOKIEROOTDIR = cookies.$(ISA)

CONFIGURE_ARGS = $(DIRPATHS)

# Optimizer flags for architecture
OPTARCH_sparc   = v8
OPTARCH_sparcv9 = v9
OPTARCH_i386    = 386
OPTARCH_amd64   = amd64
OPTARCH = $(OPTARCH_$(ISA))

OPTDIR32 = $(shell $(GARBIN)/isadir $(OPTARCH_$(ARCH)))
OPTDIR64 = $(shell $(GARBIN)/isadir $(OPTARCH_$(ARCH64)))

bindir = $(exec_prefix)/bin/$(shell $(GARBIN)/isadir $(OPTARCH_$(ISA)))
ifdef DO64
	libdir = $(exec_prefix)/lib/$(OPTDIR64)
endif

# Package doesn't have test
SKIPTEST = 1

#INSTALL_SCRIPTS = custom
CLEAN_SCRIPTS = custom

include ../category.mk

# CFLAGS += -g


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

build64:
	@echo " ==> Building 64 bit version"
	@gmake DO64=1 build
	@$(MAKECOOKIE)

#prototype:
#	@echo " ==> Making prototype"
#	@cp $(DOWNLOADDIR)/CSWsetoolkit.prototype-head $(DOWNLOADDIR)/CSWsetoolkit.prototype
#	
#	@$(MAKECOOKIE)

#install-custom: build build64
#	# Nothing gets installed, everything is picked up on packaging
#	$(MAKECOOKIE)

install64:
	@echo " ==> Installing 64 bit version"
	@gmake DO64=1 install
	@$(MAKECOOKIE)

PROT = $(WORKDIR)/CSWsetoolkit.prototype

pre-package: $(PROT)

$(PROT):
	@echo " ==> Generating prototype"
	@cp $(FILEDIR)/CSWsetoolkit.prototype-head $(PROT)

	@echo "d none $(datadir)/$(GARNAME)/include 0755 root bin" >>$(PROT)
	@(cd $(WORKSRC); for FILE in include/* sex/gui/include/* sex/net/include/* adrian/include/*; do \
		echo "f none $(datadir)/$(GARNAME)/include/`basename $$FILE`=\$$WORKDIR/$$FILE"; \
	done) >>$(PROT)

	@(cd $(WORKSRC); for DIR in examples sex/gui/examples sex/net/examples adrian/examples; do \
         for FILE in $$DIR/*; do \
	    echo "f none $(datadir)/$(GARNAME)/examples/`basename $$FILE`=\$$WORKDIR/$$FILE"; \
          done \
	done) >>$(PROT)

	@(cd $(WORKSRC); for DIR in etc contrib toptool dio perfmon workollator; do \
          echo "d none $(datadir)/$(GARNAME)/$$DIR 0755 root bin"; \
          for FILE in $$DIR/*; do \
	    echo "f none $(datadir)/$(GARNAME)/$$DIR/$$FILE=\$$WORKDIR/$$FILE"; \
          done \
	done) >>$(PROT)

clean64:
	@echo " ==> Cleaning up 64 bit version"
	@gmake DO64=1 clean-all

clean-custom: clean64 clean-all

