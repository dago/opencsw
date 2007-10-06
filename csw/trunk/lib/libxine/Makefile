GARNAME = libxine
GARVERSION = 1.1.8
CATEGORIES = APPS

DESCRIPTION = Xine-lib 1.1.8
define BLURB
xine-lib is the engine of xine. It contains all basic plugins and is necessary to run anything that relies on xine.
endef

SF_PROJ = xine
MASTER_SITES = http://prdownloads.sourceforge.net/xine/

DISTFILES  = xine-lib-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibxine)

PATCHFILES  = int_fast-defs-sol8.diff
PATCHFILES += bswap-for-sol8-i386.diff

GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS) docdir=/opt/csw/share/doc/xine
CONFIGURE_ARGS += --x-includes=/usr/X11/include --x-libraries=/usr/X11/lib
CONFIGURE_ARGS += CC="/opt/csw/gcc4/bin/gcc"
CONFIGURE_ARGS += CXX="/opt/csw/gcc4/bin/g++"
#Excluding imagemagick and gnomevfs to cut down on dependancies
CONFIGURE_ARGS += --without-imagemagick --disable-gnomevfs

include ../category.mk

#Fixing the directory names, (this code is actually called xine-lib.)
pre-patch:
	@echo "==> Renaming directory to libxine <=="
	if test !  -f $(WORKDIR)/libxine-$(GARVERSION)/*; then cd $(WORKDIR); mv xine-lib-$(GARVERSION)/* libxine-$(GARVERSION); fi
