GARNAME = tcl
GARVERSION = 8.5.8
CATEGORIES = lang

DESCRIPTION = Tcl programming language
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(GARNAME)$(GARVERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

RUNTIME_DEP_PKGS_CSWtcl += CSWsunmath

# Fix for finding libsunmath on i386 and amd64
PATCHFILES  = configure.patch
PATCHFILES += tcl.m4.patch
PATCHFILES += tclInt.h.patch

PATCHDIR = $(WORKDIR)/$(DISTNAME)

CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/export/medusa|root/opt/csw/lib/libtclstub8.4.a
CHECKPKG_OVERRIDES_CSWtcl += soname-not-found|libm.so.2|needed|by|opt/csw/lib/amd64/libtcl8.5.so
CHECKPKG_OVERRIDES_CSWtcl += soname-not-found|libm.so.2|needed|by|opt/csw/bin/amd64/tclsh8.5
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/export/medusa|root/opt/csw/share/checkpkg/overrides/tcl

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)-src.tar.gz

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
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.sparc.tar.xz | tar xf -)
	@$(MAKECOOKIE)

post-install-isa-i386:
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/8.4.i386.tar.xz | tar xf -)
	@$(MAKECOOKIE)
