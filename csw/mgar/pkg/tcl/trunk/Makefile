GARNAME = tcl
GARVERSION = 8.5.7
CATEGORIES = lang

DESCRIPTION = Tcl programming language
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(GARNAME)$(GARVERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

# Fix for finding libsunmath on i386 and amd64
PATCHFILES += configure.patch
PATCHFILES += tcl.m4.patch

RUNTIME_DEP_PKGS_CSWtcl += CSWsunmath

PATCHDIR = $(WORKDIR)/$(DISTNAME)

SPKG_SOURCEURL = http://www.tcl.tk/

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)-src.tar.gz

BUILD64 = 1
NOISAEXEC = 1

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

LICENSE = license.terms

INCLUDE_FLAGS =

CONFIGURE_ARGS = $(DIRPATHS)

# tk need the static tclstub library for some reason
EXTRA_MERGE_INCLUDE_FILES  = $(libdir)/libtclstub.*\.a

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; cp -p ../license.terms .; autoconf)
	@$(MAKECOOKIE)
