NAME = tk
VERSION = 8.5.12
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = GUI toolkit for tcl
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(NAME)$(VERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

PATCHFILES = Makefile.in.diff
PATCHDIR = $(WORKDIR)/$(DISTNAME)

#DEP_PKGS_CSWtk = CSWfconfig CSWftype2 CSWlibx11 CSWlibxft2 CSWlibxrender CSWtcl
#DEP_PKGS_CSWtk += CSWlibxext
#DEP_PKGS_CSWtk += CSWlibxscrnsaver
#DEP_PKGS_CSWtk += CSWsunmath

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

PACKAGES += CSWtk
SPKG_DESC_CSWtk = GUI toolkit for tcl
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWtk += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWtk += CSWlibtk8-5

# Leave the manpage for now
CHECKPKG_OVERRIDES_CSWtk += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/wish.1

PACKAGES += CSWlibtk8-5
SPKG_DESC_CSWlibtk8-5 = GUI toolkit library for tcl, libtk8.5.so
PKGFILES_CSWlibtk8-5 += $(call pkgfiles_lib,libtk8.5.so)
PKGFILES_CSWlibtk8-5 += $(call baseisadirs,$(libdir),tk8.5/.*)

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
RUNTIME_DEP_PKGS_CSWtcl-dev += CSWlibtk8-5

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)(\d+(?:\.\d+)*)-src.tar.gz

BUILD64 = 1

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

CONFIGURE_ARGS = $(DIRPATHS)

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET =

include gar/category.mk

#CFLAGS := $(filter-out -I%,$(CFLAGS))
#DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))


pre-configure-modulated:
	@(cd $(WORKSRC) ; cp -p ../license.terms .)
	@$(MAKECOOKIE)

post-install-isa-i386:
	@# Install legacy libs
	@# Building them with version modulations would be hard as that would require a full legacy tcl also
	#@echo Installing legacy files
	#@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.i386.tar.xz | tar xf -)
	@# Need to manually create symlink to latest version
	@echo Creating link to wish8.5
	@ln -s wish8.5 $(INSTALLISADIR)/$(bindir)/wish
	@$(MAKECOOKIE)

post-install-isa-amd64:
	@# Need to manually create symlink to latest version
	@echo Creating link to wish8.5
	@ln -s wish8.5 $(INSTALLISADIR)/$(bindir)/wish
	@$(MAKECOOKIE)

post-install-isa-sparcv8:
	@# Install legacy libs
	@# Building them with version modulations would be hard as that would require a full legacy tcl also
	#@echo Installing legacy files
	#@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.sparc.tar.xz | tar xf -)
	@# Need to manually create symlink to latest version
	@echo Creating link to wish8.5
	@ln -s wish8.5 $(INSTALLISADIR)/$(bindir)/wish
	@$(MAKECOOKIE)

post-install-isa-sparcv9:
	@# Need to manually create symlink to latest version
	@echo Creating link to wish8.5
	@ln -s wish8.5 $(INSTALLISADIR)/$(bindir)/wish
	@$(MAKECOOKIE)
