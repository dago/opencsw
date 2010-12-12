NAME = djvulibre
VERSION = 3.5.22
CATEGORIES = apps

DESCRIPTION = DjVu standalone viewer, browser plug-in, command line tools
define BLURB
endef

SF_PROJ = djvu
MASTER_SITES = $(SF_MIRRORS)/DjVuLibre/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWdjvulibre CSWdjvulibrert CSWdjvulibredevel
CATALOGNAME_CSWdjvulibre = djvulibre
CATALOGNAME_CSWdjvulibrert = djvulibre_rt
CATALOGNAME_CSWdjvulibredevel = djvulibre_devel

SPKG_DESC_CSWdjvulibre += DjVu standalone viewer, browser plug-in, command linetools
SPKG_DESC_CSWdjvulibrert += DjVu standalone viewer, browser plug-in, command line tools - runtime package
SPKG_DESC_CSWdjvulibredevel += DjVu standalone viewer, browser plug-in, commandline tools - developer package

RUNTIME_DEP_PKGS_CSWdjvulibre += CSWdjvulibrert CSWjpeg
RUNTIME_DEP_PKGS_CSWdjvulibre += CSWtiff
RUNTIME_DEP_PKGS_CSWdjvulibrert += CSWjpeg
RUNTIME_DEP_PKGS_CSWdjvulibrert += CSWiconv
RUNTIME_DEP_PKGS_CSWdjvulibredevel += CSWdjvulibrert

PKGFILES_CSWdjvulibrert = $(PKGFILES_RT)
PKGFILES_CSWdjvulibredevel = $(PKGFILES_DEVEL)


CHECKPKG_OVERRIDES_CSWdjvulibredevel += missing-dependency|CSWdjvulibre

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
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

BUILD64 = 1

TEST_TARGET =

include gar/category.mk

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libdjvulibre.so.15.s $(INSTALLISADIR)$(libdir)/libdjvulibre.so.15
	$(MAKECOOKIE)

post-install-isa-i386:
	@cp $(FILEDIR)/libdjvulibre.so.15.i $(INSTALLISADIR)$(libdir)/libdjvulibre.so.15
	$(MAKECOOKIE)
