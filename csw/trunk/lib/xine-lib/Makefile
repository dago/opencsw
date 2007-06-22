GARNAME = xine-lib
GARVERSION = hg
CATEGORIES = APPS

DESCRIPTION = Xine-lib 1.1.8 (HG test version)
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = www.xine.de
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWxine-lib,depend)


GARCOMPILER = GNU
CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib"
CONFIGURE_ARGS += CC="/opt/csw/gcc4/bin/gcc"
CONFIGURE_ARGS += CXX="/opt/csw/gcc4/bin/g++"

include ../category.mk

#GNU_CC_HOME = /opt/csw/gcc4
