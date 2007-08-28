GARNAME = libart_lgpl
GARVERSION = 2.3.19
CATEGORIES = lib

DESCRIPTION = libart - High performance 2D graphics library
define BLURB
  Libart is a library of functions for 2D graphics supporting a superset of
  the PostScript imaging model, designed to be integrated with graphics,
  artwork, and illustration programs. It is written in optimized C, and is
  fully compatible with C++. With a small footprint of 10,000 lines of code,
  it is especially suitable for embedded applications. Libart is currently
  being used in several free software applications, including Gill
  (the Gnome SVG editor), the Gnome Canvas, and several others under
  development.
endef

sparc_ARCH  = sparc
i386_ARCH   = i386
sparc_ARCH64 = sparcv9
i386_ARCH64  = amd64

ARCH=$($(GARCH)_ARCH)
ARCH64=$($(GARCH)_ARCH64)

ifndef DO64
MM=32
else
MM=64
endif

ifdef ISA
ISALIST = $(ISA)
else
ifndef DO64
ISA = $(ARCH)
else
ISA = $(ARCH64)
endif
endif

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWlibart,prototype depend)
DISTFILES   += $(call admfiles,CSWlibart-rt,prototype)
DISTFILES   += $(call admfiles,CSWlibart-devel,prototype)

WORKDIR       = $(WORKROOTDIR)/$(DESTIMG).d/$(ISA)
COOKIEROOTDIR = cookies.$(ISA)

CONFIGURE_ARGS = $(DIRPATHS)

# Optimizer flags for architecture
OPTARCH_sparcv9 = v9
OPTARCH_amd64   = amd64

CLEAN_SCRIPTS = custom

ifdef DO64
	bindir = $(exec_prefix)/bin/$(ISA)
	libdir = $(exec_prefix)/lib/$(ISA)
endif

include ../category.mk

OPTARCH = $(OPTARCH_$(ISA))

build64:
	@echo " ==> Building 64 bit version"
	gmake DO64=1 build
	$(MAKECOOKIE)

install64: build64
	@echo " ==> Installing 64 bit version"
	gmake DO64=1 install

pre-package: install64

clean64:
	gmake DO64=1 clean-all

clean-custom: clean64 clean-all
