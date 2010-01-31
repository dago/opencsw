GARNAME = tk
GARVERSION = 8.5.7
CATEGORIES = lang

DESCRIPTION = GUI toolkit for tcl
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(GARNAME)$(GARVERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

REQUIRED_PKGS_CSWtk += CSWfconfig
REQUIRED_PKGS_CSWtk += CSWftype2
REQUIRED_PKGS_CSWtk += CSWlibx11
REQUIRED_PKGS_CSWtk += CSWlibxft2
REQUIRED_PKGS_CSWtk += CSWlibxrender
REQUIRED_PKGS_CSWtk += CSWtcl

SPKG_SOURCEURL = http://www.tcl.tk/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)-src.tar.gz

BUILD64 = 1
NO_ISAEXEC = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

# INCLUDE_FLAGS =

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

EXTRA_MERGE_INCLUDE_FILES  = $(libdir)/libtkstub.*\.a

TEST_TARGET =

include gar/category.mk

#CFLAGS := $(filter-out -I%,$(CFLAGS))
#DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))
