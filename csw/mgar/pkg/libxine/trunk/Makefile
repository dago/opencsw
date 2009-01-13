GARNAME = libxine
GARVERSION = 1.1.8
CATEGORIES = apps

DESCRIPTION = Xine-lib 1.1.8
define BLURB
xine-lib is the engine of xine. It contains all basic plugins and is necessary to run anything that relies on xine.
endef

SF_PROJ = xine
MASTER_SITES = http://prdownloads.sourceforge.net/xine/

DISTFILES  = xine-lib-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibxine,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=9655
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES  = int_fast-defs-sol8.diff
PATCHFILES += bswap-for-sol8-i386.diff
PATCHFILES += configure-v8only.diff

GARCOMPILER = GNU
GARFLAVOR =

CONFIGURE_ARGS  = $(DIRPATHS) docdir=/opt/csw/share/doc/xine
CONFIGURE_ARGS += --x-includes=/usr/X11/include --x-libraries=/usr/X11/lib
CONFIGURE_ARGS += CC="/opt/csw/gcc4/bin/gcc"
CONFIGURE_ARGS += CXX="/opt/csw/gcc4/bin/g++"
#Excluding gnomevfs to cut down on dependancies
CONFIGURE_ARGS += --disable-gnomevfs

include gar/category.mk

#Fixing the directory names, (this code is actually called xine-lib.)
post-extract:
	( if test -d $(WORKDIR)/xine-lib-$(GARVERSION); then mv $(WORKDIR)/xine-lib-$(GARVERSION) $(WORKDIR)/$(DISTNAME); fi )
	@$(MAKECOOKIE)
