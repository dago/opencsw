GARNAME = tk
GARVERSION = 8.5.8
CATEGORIES = lang

DESCRIPTION = GUI toolkit for tcl
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(GARNAME)$(GARVERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz
DISTFILES += libtk8.4.so.i
DISTFILES += libtk8.4.so.s

DEP_PKGS_CSWtk = CSWfconfig CSWftype2 CSWlibx11 CSWlibxft2 CSWlibxrender CSWtcl

SPKG_SOURCEURL = http://www.tcl.tk/
LICENSE = license.terms

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)-src.tar.gz

BUILD64 = 1
NOISAEXEC = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

# INCLUDE_FLAGS =

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET =

include gar/category.mk

#CFLAGS := $(filter-out -I%,$(CFLAGS))
#DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))


pre-configure-modulated:
	@(cd $(WORKSRC) ; cp -p ../license.terms .)
	@$(MAKECOOKIE)

post-install-i386:
	@# Install legacy libs
	@# Building them with version modulations would be hard as that would require a full legacy tcl also
	ginstall $(WORKDIR)/libtk8.4.so.i $(DESTDIR)$(libdir)/libtk8.4.so
	@$(MAKECOOKIE)

post-install-sparc:
	@# Install legacy libs
	@# Building them with version modulations would be hard as that would require a full legacy tcl also
	ginstall $(WORKDIR)/libtk8.4.so.s $(DESTDIR)$(libdir)/libtk8.4.so
	@$(MAKECOOKIE)
