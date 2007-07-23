GARNAME = xinelib
GARVERSION = hg
CATEGORIES = APPS

DESCRIPTION = Xine-lib 1.1.8 (HG test build)
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = www.xine.de
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWxinelib,$(GAROSREL).depend)


#Solaris 8 Patches
ifeq ($(GAROSREL),5.8)
	PATCHFILES = bswap-for-solaris-8.diff
endif


GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS) docdir=/opt/csw/share/doc/xine
CONFIGURE_ARGS += --x-includes=/usr/X11/include --x-libraries=/usr/X11/lib
CONFIGURE_ARGS += CC="/opt/csw/gcc4/bin/gcc"
CONFIGURE_ARGS += CXX="/opt/csw/gcc4/bin/g++"

include ../category.mk
LD_OPTIONS :=

pre-package:
	(cp files/CSW$(GARNAME).$(GAROSREL).depend $(WORKSRC)/../CSW$(GARNAME).depend)

