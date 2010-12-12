NAME = tcl
VERSION = 8.5.8
CATEGORIES = lang

DESCRIPTION = Tcl programming language
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)$(VERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

RUNTIME_DEP_PKGS_CSWtcl += CSWsunmath

# Fix for finding libsunmath on i386 and amd64
PATCHFILES  = configure.patch
PATCHFILES += tcl.m4.patch
PATCHFILES += tclInt.h.patch

PATCHDIR = $(WORKDIR)/$(DISTNAME)

CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/export/medusa|root/opt/csw/lib/libtclstub8.4.a
CHECKPKG_OVERRIDES_CSWtcl += soname-not-found|libm.so.2
CHECKPKG_OVERRIDES_CSWtcl += surplus-dependency|CSWsunmath
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/export/medusa|root/opt/csw/share/checkpkg/overrides/tcl

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)(\d+(?:\.\d+)*)-src.tar.gz

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

BUILD64 = 1
NOISAEXEC = 1

INCLUDE_FLAGS =

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_ARGS = install install-private-headers install-tzdata install-msgs

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

include gar/category.mk

# CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; cp -p ../license.terms .; autoconf)
	@$(MAKECOOKIE)

post-install-isa-sparcv8:
	@# Install legacy libs
	@echo Installing legacy files
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.sparc.tar.xz | tar xf -)
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s tclsh8.5 $(INSTALLISADIR)/$(bindir)/tclsh
	@$(MAKECOOKIE)

post-install-isa-sparcv9:
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s tclsh8.5 $(INSTALLISADIR)/$(bindir)/tclsh
	@$(MAKECOOKIE)

post-install-isa-i386:
	@# Install legacy libs
	@echo Installing legacy files
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.i386.tar.xz | tar xf -)
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s tclsh8.5 $(INSTALLISADIR)/$(bindir)/tclsh
	@$(MAKECOOKIE)

post-install-isa-amd64:
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s tclsh8.5 $(INSTALLISADIR)/$(bindir)/tclsh
	@$(MAKECOOKIE)
