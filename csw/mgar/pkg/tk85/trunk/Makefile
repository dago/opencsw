NAME = tk
VERSION = 8.5.15
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = GUI toolkit for tcl
define BLECTURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(NAME)$(VERSION)
DISTFILES  = $(DIST#PATCHFILES = Makefile.in.diff
#PATCHDIR = $(WORKDIR)/$(DISTNAME)

# libsunmath support on Solaris 9 i386 is broken
PACKAGING_PLATFORMS  = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

PATCHFILES += 0001-disable-libsunmath.patchSE = license.terms

PACKAGES += CSWtk
SPKG_DESC_CSWtk = GUI toolkit for tcl
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWtk += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWtk += CSWlibtk8-5

RUNTIME_DEP_PKGS_CSWtk-i386 += CSWsunmath
RUNTIME_DEP_PKGS_CSWtk += $(RUNTIME_DEP_PKGS/man/man1/wish.1

PACKAGES += CSWlibtk8-5
SPKG_DESC_CSWlibtk8-5 = GUI toolkit library for tcl, libtk8.5.so
PKGFILES_CSWlibtk8-5 += $(call pkgfiles_lib,libtk8.5.so)
PKGFILES_CSWlibtk8-5 += $(call baseisadirs,$(RUNTIME_DEP_PKGS_CSWlibtk8-5 += CSWlibxft2
RUNTIME_DEP_PKGS_CSWlibtk8-5 += CSWlibfontconfig1libtk8-5-$(GARCH))

# This is correct, the soname with *.so is really the one to use
CHECKPKG_OVERRIDES_CSWlibtk8-5 += soname-equals-filename
# This is just a demo
CHECKPKG_OVERRIDES_CSWlibtk8-5 += file-with-bad-content|/usr/local|root/opt/csw/lib/tk8.5/demos/tcolor

PACKAGES += CSWtk-dev
SPKG_DESC_CSWtk-dev = Development files for libtk8.5.so
# Indeed, the *.so is the real library and belongs to CSWlibtcl8-5
PKGFILES_DEVEL_SHAREDLIBLINK =
PKGFILES_CSWtk-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWtk-dev += $(call baseisadirs,$(libdir),tkConfig.sh)
RUNTIME_DEP_PKGS_CSWtcl-dev Enable 64 bits, but not for Solaris 9 x86
BUILD64_5.9_sparc  = 1
BUILD64_5.10_sparc = 1
BUILD64_5.9_i386   =
BUILD64_5.10_i386  = 1
BUILD64 = $(BUILD64_$(GAROSREL)_$(GARCH))ar.gz

BUILD64 = 1
ISAEXEC = 1

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

CONFIGURE_ARGS = $(DIRPATHS)

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET =

include gar/category.mk

#CFLAGS := $(filter-out -I%,$(CFLAGS))
#DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))


pre-configure-modulated:
	(cd $(WORKSRC) ; cp -p ../license.terms .)
	@$(MAKECOOKIE)

post-install-modulated:
	@echo Creating link to wish8.5
	ln -s wish8.5 $(DESTDIR)$(bindir)/wis