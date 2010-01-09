GARNAME = djvulibre
GARVERSION = 3.5.22
CATEGORIES = apps

DESCRIPTION = DjVu standalone viewer, browser plug-in, command line tools
define BLURB
endef

SF_PROJ = djvu
MASTER_SITES = $(SF_MIRRORS)/DjVuLibre/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWdjvulibre CSWdjvulibrert CSWdjvulibredevel
CATALOGNAME_CSWdjvulibre = djvulibre
CATALOGNAME_CSWdjvulibrert = djvulibre_rt
CATALOGNAME_CSWdjvulibredevel = djvulibre_devel

SPKG_DESC_CSWdjvulibre += DjVu standalone viewer, browser plug-in, command linetools
SPKG_DESC_CSWdjvulibrert += DjVu standalone viewer, browser plug-in, command line tools - runtime package
SPKG_DESC_CSWdjvulibredevel += DjVu standalone viewer, browser plug-in, commandline tools - developer package

REQUIRED_PKGS_CSWdjvulibre += CSWdjvulibrert CSWjpeg CSWtiff CSWzlib
REQUIRED_PKGS_CSWdjvulibrert += CSWjpeg
REQUIRED_PKGS_CSWdjvulibredevel += CSWdjvulibre

PKGFILES_CSWdjvulibrert = $(PKGFILES_RT)
PKGFILES_CSWdjvulibredevel = $(PKGFILES_DEVEL)

SPKG_SOURCEURL = http://djvu.sourceforge.net/

LICENSE = COPYING

PATCHFILES += ddjvu.cpp.patch

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=32953
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

OPTS='-DNDEBUG'
EXTRA_COMMON_EXPORTS += OPTS

PTHREAD_LIBS = -lpthread
PTHREAD_CFLAGS = -D_REENTRANT
EXTRA_COMMON_EXPORTS += PTHREAD_LIBS
EXTRA_COMMON_EXPORTS += PTHREAD_CFLAGS


EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

X_CFLAGS = -I$(prefix)/X11/include
X_LIBS = -L$(prefix)/X11/lib -R$(prefix)/X11/lib
EXTRA_COMMON_EXPORTS += X_CFLAGS 
EXTRA_COMMON_EXPORTS += X_LIBS 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-extra-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --with-extra-libraries=$(prefix)/X11/lib

BUILD64 = 1

TEST_TARGET =

include gar/category.mk
