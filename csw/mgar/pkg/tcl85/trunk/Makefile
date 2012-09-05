NAME = tcl8.5
VERSION = 8.5.12
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Tcl programming language v8.5
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(SF_PROJ)$(VERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

# Separate build for Solaris 10 with DTrace support
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

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
# PATCHFILES += tcl-dtrace.patch

# The dependencies on the ISAs differ, here's from tcl-x.y.z/unix/tcl.m4: 
#
#              # On Solaris 5.x i386 with the sunpro compiler we need to link
#              # with sunmath to get floating point rounding control

PACKAGES  = CSWtcl
SPKG_DESC_CSWtcl = Tcl programming language 8.5
RUNTIME_DEP_PKGS_CSWtcl += CSWlibtcl8-5-0
RUNTIME_DEP_PKGS_CSWtcl-i386 = CSWsunmath
RUNTIME_DEP_PKGS_CSWtcl += $(RUNTIME_DEP_PKGS_CSWtcl-$(GARCH))

# This is to find zoneinfo
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/local|root/opt/csw/share/man/mann/clock.n
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/share|root/opt/csw/share/man/mann/clock.n

PACKAGES += CSWlibtcl8-5-0
SPKG_DESC_CSWlibtcl8-5-0 = $(DESCRIPTION), libraries
PKGFILES_CSWlibtcl8-5-0 += $(call pkgfiles_lib,libtcl8.5.so.0)
PKGFILES_CSWlibtcl8-5-0 += $(libdir)/tcl8/.*
PKGFILES_CSWlibtcl8-5-0 += $(libdir)/tcl8.5/.*
RUNTIME_DEP_PKGS_CSWlibtcl8-5-0-i386 += CSWsunmath
RUNTIME_DEP_PKGS_CSWlibtcl8-5-0 += $(RUNTIME_DEP_PKGS_CSWlibtcl8-5-0-$(GARCH))

# This is to find zoneinfo
CHECKPKG_OVERRIDES_CSWlibtcl8-5-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/tcl8.5/clock.tcl
CHECKPKG_OVERRIDES_CSWlibtcl8-5-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/tcl8.5/clock.tcl

PACKAGES += CSWtcl-dev
SPKG_DESC_CSWtcl-dev = $(DESCRIPTION), development files
PKGFILES_CSWtcl-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWtcl-dev += $(call baseisadirs,$(libdir),tclConfig.sh)
RUNTIME_DEP_PKGS_CSWtcl-dev += CSWlibtcl8-5-0

BUILD64 = 1

INCLUDE_FLAGS =

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads

# DTrace support is currently broken, disable for now
#  Text relocation remains                         referenced
#      against symbol                  offset      in file
#  st                                  0x634       tclDTrace.o
#  ld: fatal: relocations remain against allocatable but non-writable sections
CONFIGURE_ARGS-5.10 += --enable-dtrace

CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL))

INSTALL_ARGS = install install-libraries install-private-headers install-tzdata install-msgs

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET = test

include gar/category.mk

DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	#(cd $(WORKSRC) ; cp -p ../license.terms .; $(prefix)/bin/autoreconf -if )
	@$(MAKECOOKIE)

pre-test-modulated:
	@# Need to manually create symlink to latest version
	@echo Creating symlinks for libtcl8.5.so
	(cd $(WORKSRC) ; \
		mv $(REN_LIBTCL) $(REN_LIBTCL).0 ; \
		ln -sf $(REN_LIBTCL).0 $(REN_LIBTCL) )
	@$(MAKECOOKIE)

post-install-modulated:
	@# Need to manually create symlink to latest version - it will be handled by alternatives
	@echo Creating tclsh link
	ln -s $(REN_TCLSH) $(DESTDIR)$(bindir)/tclsh
	cd $(DESTDIR)$(libdir) && mv $(REN_LIBTCL) $(REN_LIBTCL).0 && ln -sf $(REN_LIBTCL).0 $(REN_LIBTCL)
	perl -pi -e "s|/usr/local|$(prefix)|g" $(DESTDIR)$(libdir)/tclConfig.sh
	perl -pi -e "s|/usr/local|$(prefix)|g" $(DESTDIR)$(mandir)/man1/tclsh.1
	@$(MAKECOOKIE)

