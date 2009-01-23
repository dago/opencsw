GARNAME = tk
GARVERSION = 8.4.19
CATEGORIES = lang

DESCRIPTION = Tcl programming language
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(GARNAME)$(GARVERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz
DISTFILES += $(call admfiles,CSWtk,)

SPKG_SOURCEURL = http://www.tcl.tk/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)-src.tar.gz

BUILD64 = 1
NO_ISAEXEC = 1

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

INCLUDE_FLAGS =

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))
