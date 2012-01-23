NAME = tk
VERSION = 8.5.8
CATEGORIES = lang

DESCRIPTION = GUI toolkit for tcl
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)

DISTNAME = $(NAME)$(VERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

PATCHFILES = Makefile.in.diff
PATCHDIR = $(WORKDIR)/$(DISTNAME)

DEP_PKGS_CSWtk = CSWfconfig CSWftype2 CSWlibx11 CSWlibxft2 CSWlibxrender CSWtcl
DEP_PKGS_CSWtk += CSWlibxext
DEP_PKGS_CSWtk += CSWlibxscrnsaver
DEP_PKGS_CSWtk += CSWsunmath

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

CHECKPKG_OVERRIDES_CSWtk += file-with-bad-content|/export/medusa|root/opt/csw/lib/libtk8.4.so
CHECKPKG_OVERRIDES_CSWtk += file-with-bad-content|/export/medusa|root/opt/csw/lib/libtkstub8.4.a
CHECKPKG_OVERRIDES_CSWtk += file-with-bad-content|/export/medusa|root/opt/csw/share/checkpkg/overrides/tk
CHECKPKG_OVERRIDES_CSWtk += linked-against-discouraged-library|libtk8.4.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWtk += surplus-dependency|CSWsunmath
CHECKPKG_OVERRIDES_CSWtk += soname-not-found|libm.so.2

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)(\d+(?:\.\d+)*)-src.tar.gz

BUILD64 = 1

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

post-install-isa-i386:
	@# Install legacy libs
	@# Building them with version modulations would be hard as that would require a full legacy tcl also
	@echo Installing legacy files
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.i386.tar.xz | tar xf -)
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
	@echo Installing legacy files
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.sparc.tar.xz | tar xf -)
	@# Need to manually create symlink to latest version
	@echo Creating link to wish8.5
	@ln -s wish8.5 $(INSTALLISADIR)/$(bindir)/wish
	@$(MAKECOOKIE)

post-install-isa-sparcv9:
	@# Need to manually create symlink to latest version
	@echo Creating link to wish8.5
	@ln -s wish8.5 $(INSTALLISADIR)/$(bindir)/wish
	@$(MAKECOOKIE)
