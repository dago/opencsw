GARNAME = qt4
GARVERSION = 4.3.3
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
DISTFILES   += $(call admfiles,CSWqt4,depend prototype-sparc prototype-i386)
DISTFILES   += $(call admfiles,CSWqt4-devel,depend prototype-sparc prototype-i386)
DISTFILES   += $(call admfiles,CSWqt4-docs,prototype)

WORKDIR = $(WORKROOTDIR)/$(DESTIMG).d/$(PLATFORM)
COOKIEROOTDIR = cookies.$(PLATFORM)

WORKSRC = $(WORKDIR)/qt-x11-opensource-src-$(GARVERSION)

PREREQUISITE_PKGS = CSWpkgconfig CSWfconfig CSWlibdbusdev

# Usually the pathes from already installed stuff at $DESTDIR is
# used before regular installed stuff. This leads to include errors
# if we already have a qt4 installed at $DESTDIR.
IGNORE_DESTDIR = 1

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
			-docdir $(docdir)/qt \
			-headerdir $(includedir) \
			-plugindir $(libdir)/qt4/plugins \
			-datadir $(sharedstatedir)/qt4 \
			-translationdir $(sharedstatedir)/qt4/translations \
			-sysconfdir $(etcdir)/qt4/settings \
			-examplesdir $(sharedstatedir)/qt4/examples \
			-demosdir $(sharedstatedir)/qt4/demos \
			-I$(includedir) \
			-L$(libdir) \
			-platform $(PLATFORM) \
			-confirm-license \
			-verbose

SKIPTEST = 1

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

SRC_CLEAN_TARGET = confclean

ifndef DO64
CLEAN_SCRIPTS = all custom
endif

include ../category.mk

OPTARCH_sparc   = v8
OPTARCH_sparcv9 = v9
OPTARCH_i386    = 386
OPTARCH_amd64   = amd64
OPTARCH = $(OPTARCH_$(ISA))

ifdef DO64
	# Do not use -xO3 as -xO2 is already set in the Makefile
	SUN_CC_OPT = -xarch=$(OPTARCH) -xspace -xildoff
	SUN_CXX_OPT = -xarch=$(OPTARCH) -xspace -xildoff

	# Do not include -I/-L here. These flags must be defined after
	# local QT4 includes and need to be defined during configure.
	CFLAGS = $($(GARCOMPILER)_CC_$(GARFLAVOR))
	CPPFLAGS = $($(GARCOMPILER)_CPP_FLAGS)
	# -D_POSIX_PTHREAD_SEMANTICS needed, because getpwuid_r is used in the 4-arg-version
	# (see getpwuid_r(3c) for details)
	CXXFLAGS = $($(GARCOMPILER)_CXX_$(GARFLAVOR)) -D_POSIX_PTHREAD_SEMANTICS
	LDFLAGS = $($(GARCOMPILER)_LD_FLAGS) $($(GARCOMPILER)_LD_$(GARFLAVOR))
else
	# Do not use -xO3 as -xO2 is already set in the Makefile
	SUN_CC_OPT = -xarch=$(OPTARCH) -xspace -xildoff
	SUN_CXX_OPT = -xarch=$(OPTARCH) -xspace -xildoff

	# Do not include -I/-L here. These flags must be defined after
	# local QT4 includes and need to be defined during configure.
	CFLAGS = $($(GARCOMPILER)_CC_$(GARFLAVOR))
	CPPFLAGS = $($(GARCOMPILER)_CPP_FLAGS)
	CXXFLAGS = $($(GARCOMPILER)_CXX_$(GARFLAVOR))
	LDFLAGS = $($(GARCOMPILER)_LD_FLAGS) $($(GARCOMPILER)_LD_$(GARFLAVOR))
endif

pre-build:
	@echo "ISA: $(ISA)"
	@echo "XC: $(GARCOMPILER)_CC_$(GARFLAVOR)"
	@echo "XC: $($(GARCOMPILER)_CC_$(GARFLAVOR))"
	@echo "CFLAGS: $(CFLAGS)"

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
	gmake DO64=1 clean

clean-custom: clean64

env:
	@echo "      GARCH = $(GARCH)"
	@echo " GARVERSION = $(GARVERSION)"
	@echo "        ISA = $(ISA)"
	@echo "     CFLAGS = $(CFLAGS)"
	@echo "    OPTARCH = $(OPTARCH)"
	@echo " OPTARCH_ISA = $(OPTARCH_$(ISA))"
	@echo "CLEAN TARGETS = $(CLEAN_TARGETS)"
