GARNAME = qt
GARVERSION = 4.0.1
CATEGORIES = lib

DESCRIPTION = TrollTech C++ application framework
define BLURB
  LONG DESCRIPTION HERE
endef

GARCOMPILER = GNU

MASTER_SITES = ftp://ftp.trolltech.com/qt/source/
#DISTFILES    = qt-x11-opensource-src-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWqtgcc,)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
