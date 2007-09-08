GARNAME = qt4
GARVERSION = 4.3.1
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  Qt is a comprehensive cross-platform C++ application framework. Qt 4.3
  introduces new features and many improvements over the 3.x series. See
  http://doc.trolltech.com/4.3/qt4-intro.html for details.
endef

sparc_ARCH  = sparc
i386_ARCH   = i386
sparc_ARCH64 = sparcv9
i386_ARCH64  = amd64

ARCH=$($(GARCH)_ARCH)
ARCH64=$($(GARCH)_ARCH64)

ifndef DO64
PLATFORM=solaris-cc
else
PLATFORM=solaris-cc-64
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

MASTER_SITES = ftp://ftp.trolltech.com/qt/source/
DISTFILES    = qt-x11-opensource-src-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWqt4,prototype-sparc prototype-i386)
DISTFILES   += $(call admfiles,CSWqt4-devel,prototype-sparc prototype-i386)
DISTFILES   += $(call admfiles,CSWqt4-docs,prototype)

WORKDIR = $(WORKROOTDIR)/$(DESTIMG).d/$(PLATFORM)
COOKIEROOTDIR = cookies.$(PLATFORM)

WORKSRC = $(WORKDIR)/qt-x11-opensource-src-$(GARVERSION)

ifdef DO64
	bindir = $(exec_prefix)/bin/sparcv9
	libdir = $(exec_prefix)/lib/sparcv9
	docdir = $(prefix)/ignore/doc
	includedir = $(prefix)/ignore/include
	datadir = $(prefix)/ignore/data
	sharedstatedir = $(prefix)/ignore/share
	etcdir = $(prefix)/ignore/etc
endif

CONFIGURE_ARGS = -prefix $(prefix) \
			-bindir $(bindir) \
			-libdir $(libdir) \
			-docdir $(docdir)/qt/doc \
			-headerdir $(includedir) \
			-plugindir $(libdir)/qt4/plugins \
			-datadir $(sharedstatedir)/qt4 \
			-translationdir $(sharedstatedir)/qt4/translations \
			-sysconfdir $(etcdir)/qt4/settings \
			-examplesdir $(sharedstatedir)/qt4/examples \
			-demosdir $(sharedstatedir)/qt4/demos \
			-platform $(PLATFORM) \
			-confirm-license 

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

SRC_CLEAN_TARGET = confclean

CLEAN_TARGETS += custom

include ../category.mk

OPTARCH = $(OPTARCH_$(ISA))

ifdef DO64
	# Don't use any flags as this is already correctly set
	#CFLAGS =
	#CXXFLAGS =
	#LDFLAGS =
else
	# Do NOT include -xO3 as -xO2 is already set in the Makefile
	SUN_CC_OPT = -xarch=$(OPTARCH) -xspace -xildoff
	SUN_CXX_OPT = -xarch=$(OPTARCH) -xspace -xildoff
endif

build64:
	@echo " ==> Building 64 bit version"
	gmake DO64=1 build

install64: build64
	@echo " ==> Installing 64 bit version"
	gmake DO64=1 install

pre-package: install64

pre-install:
	@echo " ==> Install environment:"
	@echo " bindir: $(bindir)"
	@echo " libdir: $(libdir)"
	@/usr/bin/env

clean64:
	gmake DO64=1 clean-all

clean-custom: clean64 clean-all
