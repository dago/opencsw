GARNAME = tcl
GARVERSION = 8.5.8
CATEGORIES = lang

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 8.4.19 8.5.8
# The legacy library was not available in 64 bit, so don't bother compiling it
SKIP_MODULATIONS = isa-sparcv9-garversion-8.4.19 isa-amd64-garversion-8.4.19

DESCRIPTION = Tcl programming language
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION), $(GARNAME)$(VERSION)-src.tar.gz)
DISTFILES  = $(SOURCEFILES)
NOEXTRACT = $(filter-out $(GARNAME)$(GARVERSION)-src.tar.gz,$(SOURCEFILES))

# Fix for finding libsunmath on i386 and amd64
PATCHFILES-8.5.8  = configure.patch
PATCHFILES-8.5.8 += tcl.m4.patch
PATCHFILES-8.5.8 += tclInt.h.patch

PATCHFILES = $(PATCHFILES-$(GARVERSION))
ALLFILES_PATCHFILES = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(PATCHFILES-$(VERSION)))

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)-src.tar.gz

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

DISTNAME = $(GARNAME)$(GARVERSION)
PATCHDIR = $(WORKDIR)/$(DISTNAME)
WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

BUILD64-8.5.8 = 1
BUILD64 = $(BUILD64-$(GARVERSION))
NOISAEXEC = 1

INCLUDE_FLAGS =

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_ARGS-8.4.19 = install
INSTALL_ARGS-8.5.8 = install install-private-headers install-tzdata install-msgs
INSTALL_ARGS = $(INSTALL_ARGS-$(GARVERSION))

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

MERGE_SCRIPTS_isa-default-garversion-8.4.19 = copy-lib-only

MERGE_SCRIPTS_isa-default-garversion-8.5.8 = copy-all
MERGE_SCRIPTS_isa-extra-garversion-8.5.8 = copy-relocated-only
MERGE_DIRS_isa-extra-garversion-8.5.8 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

include gar/category.mk

# CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; cp -p ../license.terms .; autoconf)
	@$(MAKECOOKIE)

merge-copy-lib-only:
	ginstall -d $(PKGROOT)$(libdir)
	ginstall $(INSTALLISADIR)$(libdir)/*.so $(PKGROOT)$(libdir)
	@$(MAKECOOKIE)
