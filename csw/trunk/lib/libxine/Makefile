GARNAME = libxine
GARVERSION = 1.1.8
CATEGORIES = APPS

DESCRIPTION = Xine-lib 1.1.8
define BLURB
This is a work in progress. Currently this build only works under solaris 10. Solaris 8 is yet to come.
endef

SF_PROJ = xine
MASTER_SITES = http://prdownloads.sourceforge.net/xine/

DISTFILES  = xine-lib-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibxine)#,$(GAROSREL).depend)


#Solaris 8 Patches
ifeq ($(GAROSREL),5.8)
	PATCHFILES = bswap-for-solaris-8.diff
	PATCHFILES = int_fast-defs-sol8.diff
endif


GARCOMPILER = GNU

#CONFIGURE_SCRIPTS = custom

#Excluding imagemagick and gnomevfs to cut down on dependancies
CONFIGURE_ARGS  = $(DIRPATHS) docdir=/opt/csw/share/doc/xine
CONFIGURE_ARGS += --x-includes=/usr/X11/include --x-libraries=/usr/X11/lib
CONFIGURE_ARGS += --without-imagemagick --disable-gnomevfs
CONFIGURE_ARGS += CC="/opt/csw/gcc4/bin/gcc"
CONFIGURE_ARGS += CXX="/opt/csw/gcc4/bin/g++"

include ../category.mk
LD_OPTIONS :=

pre-package:
	(cp files/CSW$(GARNAME).$(GAROSREL).depend $(WORKSRC)/../CSW$(GARNAME).depend)

#Fixing the directory names, this code is actually called xine-lib.
pre-configure:
	@echo "==> Renaming directory to libxine <=="
	if test !  -f $(WORKDIR)/libxine-$(GARVERSION)/*; then cd $(WORKDIR); mv xine-lib-$(GARVERSION)/* libxine-$(GARVERSION); fi
