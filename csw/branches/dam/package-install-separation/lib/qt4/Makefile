GARNAME = qt4
GARVERSION = 4.3.1
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  Qt is a comprehensive cross-platform C++ application framework. Qt 4.3
  introduces new features and many improvements over the 3.x series. See
  http://doc.trolltech.com/4.3/qt4-intro.html for details.
endef

ifndef PLATFORM
PLATFORM = solaris-cc
endif

MASTER_SITES = ftp://ftp.trolltech.com/qt/source/
DISTFILES    = qt-x11-opensource-src-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWqt4,)
DISTFILES   += $(call admfiles,CSWqt4-rt,)
DISTFILES   += $(call admfiles,CSWqt4-devel,)
DISTFILES   += $(call admfiles,CSWqt4-demos,)
DISTFILES   += $(call admfiles,CSWqt4-docs,)
DISTFILES   += $(call admfiles,CSWqt4-gcc,)

WORKDIR = $(WORKROOTDIR)/$(DESTIMG).d/$(PLATFORM)
COOKIEROOTDIR = cookies.$(PLATFORM)

WORKSRC = $(WORKDIR)/qt-x11-opensource-src-$(GARVERSION)

CONFIGURE_ARGS = -prefix $(prefix) \
			-docdir $(docdir)/qt/doc \
			-examplesdir $(sharedstatedir)/qt/examples \
			-demosdir $(sharedstatedir)/qt/demos \
			-platform $(PLATFORM) \
			-confirm-license 

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

include ../category.mk

# Do NOT include -xO3 as -xO2 is already set in the Makefile
SUN_CC_OPT = -xarch=$(OPTARCH) -xspace -xildoff
SUN_CXX_OPT = -xarch=$(OPTARCH) -xspace -xildoff

# Do NOT include the CSW include pathes here
CFLAGS = $($(GARCOMPILER)_CC_$(GARFLAVOR))
CXXFLAGS = $($(GARCOMPILER)_CXX_$(GARFLAVOR))

pre-package:
	@echo " ==> Building 64 bit version with Sun Studio CC"
	gmake PLATFORM=solaris-cc-64 \
		bindir=$(bindir)/sparcv9 \
		libdir=$(libdir)/sparcv9 \
		install
	$(MAKECOOKIE)

clean-custom: clean-all
	gmake PLATFORM=solaris-cc-64 clean-all
