GARNAME = qt
GARVERSION = 4.3.1
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  Qt is a comprehensive cross-platform C++ application framework. Qt 4.3
  introduces new features and many improvements over the 3.x series. See
  http://doc.trolltech.com/4.3/qt4-intro.html for details.
endef

MASTER_SITES = ftp://ftp.trolltech.com/qt/source/
DISTFILES    = qt-x11-opensource-src-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWqt,)
DISTFILES   += $(call admfiles,CSWqtdocs,)
DISTFILES   += $(call admfiles,CSWqtgcc,)

CONFIGURE_ARGS = $(DIRPATHS)

WORKSRC = $(WORKDIR)/qt-x11-opensource-src-$(GARVERSION)

CONFIGURE_ARGS = -prefix $(prefix) \
			-docdir $(docdir)/qt/doc \
			-examplesdir $(sharedstatedir)/qt/examples \
			-demosdir $(sharedstatedir)/qt/demos \
			-confirm-license 

# Alternaitv: -platform solaris-cc-64

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

include ../category.mk

# Do NOT include -xO3 as -xO2 is already set in the Makefile
SUN_CC_OPT = -xarch=$(OPTARCH) -xspace -xildoff
SUN_CXX_OPT = -xarch=$(OPTARCH) -xspace -xildoff

# Do NOT include the CSW include pathes here
CFLAGS = $($(GARCOMPILER)_CC_$(GARFLAVOR))
CXXFLAGS = $($(GARCOMPILER)_CXX_$(GARFLAVOR))
