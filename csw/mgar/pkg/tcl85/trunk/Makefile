GARNAME = tcl
GARVERSION = 8.5.6
CATEGORIES = lang

DESCRIPTION = Tcl programming language
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(GARNAME)$(GARVERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz
DISTFILES += $(call admfiles,CSWtcl85,)

# From https://sourceforge.net/tracker/?func=detail&atid=110894&aid=1839067&group_id=10894
# for Solaris x86:
#PATCHFILES = sunmath-updated.diff
#PATCHFILES = sunmath.diff
# Both patches seem to be for HEAD instead of 8.5.6, to postpone for now

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
