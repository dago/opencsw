NAME = tcl
VERSION = 8.5.10
CATEGORIES = lang

DESCRIPTION = Tcl programming language
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)$(VERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz
DISTFILES += soname.diff
DISTFILES += tcl.m4.patch

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)(\d+(?:\.\d+)*)-src.tar.gz

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms


## Fix for finding libsunmath on i386 and amd64
#PATCHFILES  = configure.patch
#PATCHFILES += tclInt.h.patch

REN_LIBTCL  = libtcl8.5.so

PATCHDIR = $(WORKDIR)/$(DISTNAME)
PATCHFILES  = soname.diff
PATCHFILES += tcl.m4.patch

PACKAGES  = CSWtcl
PACKAGES += CSWlibtcl8-5
PACKAGES += CSWtcl-dev
PACKAGES += CSWtcl-doc
CATALOGNAME_CSWtcl       = tcl
CATALOGNAME_CSWlibtcl8-5 = libtcl8_5
CATALOGNAME_CSWtcl-dev   = tcl_dev
CATALOGNAME_CSWtcl-doc   = tcl_doc

RUNTIME_DEP_PKGS_CSWtcl       += CSWsunmath
RUNTIME_DEP_PKGS_CSWlibtcl8-5 += CSWsunmath

SPKG_DESC_CSWtcl        = $(DESCRIPTION)
SPKG_DESC_CSWlibtcl8-5  = $(DESCRIPTION), libraries
SPKG_DESC_CSWtcl-dev    = $(DESCRIPTION), development files
SPKG_DESC_CSWtcl-doc    = $(DESCRIPTION), documentation

PKGFILES_CSWlibtcl8-5   = $(call pkgfiles_lib,libtcl8.5.so.0)
PKGFILES_CSWtcl-dev     = $(PKGFILES_DEVEL)
PKGFILES_CSWtcl-doc     = $(PKGFILES_DOC)

BUILD64 = 1

INCLUDE_FLAGS =

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads
#CONFIGURE_ARGS += --enable-dtrace

INSTALL_ARGS = install install-private-headers install-tzdata install-msgs

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET = test

# this is only temporaryly
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk


# CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; cp -p ../license.terms .; $(prefix)/bin/autoreconf -if )
	@$(MAKECOOKIE)

pre-test-modulated:
	@# Need to manually create symlink to latest version
	@echo Creating symlinks for libtcl8.5.so
	@(cd $(WORKSRC) ; \
		mv $(REN_LIBTCL) $(REN_LIBTCL).0 ; \
		ln -sf $(REN_LIBTCL).0 $(REN_LIBTCL) )
	@$(MAKECOOKIE)

post-install-isa-sparcv8:
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
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s tclsh8.5 $(INSTALLISADIR)/$(bindir)/tclsh
	@$(MAKECOOKIE)

post-install-isa-amd64:
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s tclsh8.5 $(INSTALLISADIR)/$(bindir)/tclsh
	@$(MAKECOOKIE)
