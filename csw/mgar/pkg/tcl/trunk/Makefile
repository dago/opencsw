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

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

## Fix for finding libsunmath on i386 and amd64
#PATCHFILES  = configure.patch
#PATCHFILES += tclInt.h.patch

REN_LIBTCL  = libtcl8.5.so
REN_TCLSH   = tclsh8.5

PATCHDIR = $(WORKDIR)/$(DISTNAME)
PATCHFILES  = soname.diff
PATCHFILES += tcl.m4.patch
PATCHFILES += tcl-dtrace.patch

PACKAGES  = CSWtcl
PACKAGES += CSWlibtcl8-5-0
PACKAGES += CSWtcl-dev
PACKAGES += CSWtcl-doc

# The dependencies on the ISAs differ, here's from tcl-x.y.z/unix/tcl.m4: 
#
#              # On Solaris 5.x i386 with the sunpro compiler we need to link
#              # with sunmath to get floating point rounding control
#
RUNTIME_DEP_PKGS_CSWtcl-i386          = CSWsunmath
RUNTIME_DEP_PKGS_CSWtcl              += CSWlibtcl8-5-0
RUNTIME_DEP_PKGS_CSWtcl              += $(RUNTIME_DEP_PKGS_CSWtcl-$(GARCH))
RUNTIME_DEP_PKGS_CSWlibtcl8-5-0-i386 += CSWsunmath
RUNTIME_DEP_PKGS_CSWlibtcl8-5-0      += $(RUNTIME_DEP_PKGS_CSWlibtcl8-5-0-$(GARCH))
RUNTIME_DEP_PKGS_CSWtcl-dev          += CSWlibtcl8-5-0

SPKG_DESC_CSWtcl          = $(DESCRIPTION)
SPKG_DESC_CSWlibtcl8-5-0  = $(DESCRIPTION), libraries
SPKG_DESC_CSWtcl-dev      = $(DESCRIPTION), development files
SPKG_DESC_CSWtcl-doc      = $(DESCRIPTION), documentation

PKGFILES_CSWlibtcl8-5-0   = $(call pkgfiles_lib,libtcl8.5.so.0)
PKGFILES_CSWtcl-dev       = $(PKGFILES_DEVEL)
PKGFILES_CSWtcl-doc       = $(PKGFILES_DOC)

ARCHALL_CSWtcl-doc = 1 

CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/local|root/opt/csw/share/man/mann/clock.n
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/share|root/opt/csw/share/man/mann/clock.n
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/local|root/opt/csw/lib/tcl8.5/clock.tcl
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/share|root/opt/csw/lib/tcl8.5/clock.tcl


BUILD64 = 1

INCLUDE_FLAGS =

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-dtrace

INSTALL_ARGS = install install-private-headers install-tzdata install-msgs

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET = test

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

post-install-modulated:
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s $(REN_TCLSH) $(INSTALLISADIR)/$(bindir)/tclsh
	@perl -pi -e "s|/usr/local|$(prefix)|g" $(INSTALLISADIR)/$(libdir)/tclConfig.sh
	@perl -pi -e "s|/usr/local|$(prefix)|g" $(INSTALLISADIR)/$(prefix)/share/man/man1/tclsh.1
	@$(MAKECOOKIE)

