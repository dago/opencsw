NAME = tcl8.4
VERSION = 8.4.19
CATEGORIES = lang

DESCRIPTION = Tcl programming language, version 8.4
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

REN_LIBTCL  = libtcl8.4.so
REN_TCLSH   = tclsh8.4

PATCHDIR = $(WORKDIR)/$(DISTNAME)
PATCHFILES += tcl.m4.patch
PATCHFILES += tcl-dtrace.patch

PACKAGES  = CSWtcl
PACKAGES += CSWtcl8.4

ALTERNATIVES_PRIO = 840

# The dependencies on the ISAs differ, here's from tcl-x.y.z/unix/tcl.m4: 
#
#              # On Solaris 5.x i386 with the sunpro compiler we need to link
#              # with sunmath to get floating point rounding control
#
RUNTIME_DEP_PKGS_CSWtcl           = CSWtcl8.4
RUNTIME_DEP_PKGS_CSWtcl8.4-i386   = CSWsunmath
RUNTIME_DEP_PKGS_CSWtcl8.4-i386  += $(RUNTIME_DEP_PKGS_CSWtcl-$(GARCH))

SPKG_DESC_CSWtcl          = $(DESCRIPTION), backwards compatibility package
SPKG_DESC_CSWtcl8.4       = $(DESCRIPTION)

ALTERNATIVES_CSWtcl8.4 += tcl8.4
ALTERNATIVES_tc8.4 += $(bindir)/tclsh
ALTERNATIVES_tc8.4 += $(libdir)/tclConfig.sh

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

post-install-modulated:
	@# Need to manually create symlink to latest version
	@echo Creating tclsh link
	@ln -s $(REN_TCLSH) $(INSTALLISADIR)/$(bindir)/tclsh
	@perl -pi -e "s|/usr/local|$(prefix)|g" $(INSTALLISADIR)/$(libdir)/tclConfig.sh
	@perl -pi -e "s|/usr/local|$(prefix)|g" $(INSTALLISADIR)/$(prefix)/share/man/man1/tclsh.1
	@$(MAKECOOKIE)

