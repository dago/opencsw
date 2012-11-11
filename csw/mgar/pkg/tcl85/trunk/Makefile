NAME = tcl8.5
VERSION = 8.5.12
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Tcl programming language v8.5
define BLECTURB
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

REN_TCLSH = tclsh8.5

PATCHDIR = $(WORKDIR)/$(DISTNAME)
#PATCHFILES += 0001-Enable-SONAME-in-library.patch
#PATCHFILES += 0002-Fix-linking-issues-and-enable-building-on-Solaris-9-.patch

# The dependencies on the ISAs differ, here's from tcl-x.y.z/unix/tcl.m4: 
#
#              # On Solaris 5.x i386 with the sunpro compiler we need to link
#              # with sunmath to get floating point rounding control

PACKAGES  = CSWtcl
SPKG_DESC_CSWtcl = Tcl programming language 8.5
RUNTIME_DEP_PKGS_CSWtcl += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWtcl-i386 = CSWsunmath
RUNTIME_DEP_PKGS_CSWtcl += $(RUNTIME_DEP_PKGS_CSWtcl-$(GARCH))

# There are legacy packages depending on CSWtcl which require libtcl 8.4
FOREIGN_PACKAGES += CSWlibtcl8-4
RUNTIME_DEP_PKGS_CSWtcl += CSWlibtcl8-4
CHECKPKG_OVERRIDES_CSWtcl += surplus-dependency|CSWlibtcl8-4
CHECKPKG_OVERRIDES_CSWtcl += unidentified-dependency|CSWlibtcl8-4

# This is to find zoneinfo
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/local|root/opt/csw/share/man/mann/clock.n
CHECKPKG_OVERRIDES_CSWtcl += file-with-bad-content|/usr/share|root/opt/csw/share/man/mann/clock.n

PACKAGES += CSWlibtcl8-5
SPKG_DESC_CSWlibtcl8-5 = $(DESCRIPTION), libraries
PKGFILES_CSWlibtcl8-5 += $(call pkgfiles_lib,libtcl8.5.so)
PKGFILES_CSWlibtcl8-5 += $(libdir)/tcl8.5/.*
# This dependency can not be tracked by checkpkg
RUNTIME_DEP_PKGS_CSWlibtcl8-5 += CSWtcl8-tclmodules
CHECKPKG_OVERRIDES_CSWlibtcl8-5 += surplus-dependency|CSWtcl8-tclmodules
RUNTIME_DEP_PKGS_CSWlibtcl8-5-i386 += CSWsunmath
RUNTIME_DEP_PKGS_CSWlibtcl8-5 += $(RUNTIME_DEP_PKGS_CSWlibtcl8-5-$(GARCH))

# This is correct, the soname with *.so is really the one to use
CHECKPKG_OVERRIDES_CSWlibtcl8-5 += soname-equals-filename

# This is to find zoneinfo
CHECKPKG_OVERRIDES_CSWlibtcl8-5 += file-with-bad-content|/usr/local|root/opt/csw/lib/tcl8.5/clock.tcl
CHECKPKG_OVERRIDES_CSWlibtcl8-5 += file-with-bad-content|/usr/share|root/opt/csw/lib/tcl8.5/clock.tcl

PACKAGES += CSWtcl8-tclmodules
SPKG_DESC_CSWtcl8-tclmodules = Modules common to TCL 8.x
PKGFILES_CSWtcl8-tclmodules += $(libdir)/tcl8/.*

PACKAGES += CSWtcl-dev
SPKG_DESC_CSWtcl-dev = $(DESCRIPTION), development files
# Indeed, the *.so is the real library and belongs to CSWlibtcl8-5
PKGFILES_DEVEL_SHAREDLIBLINK =
PKGFILES_CSWtcl-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWtcl-dev += $(call baseisadirs,$(libdir),tclConfig.sh)
RUNTIME_DEP_PKGS_CSWtcl-dev += CSWlibtcl8-5

BUILD64 = 1
ISAEXEC = 1

INCLUDE_FLAGS =

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads

# DTrace support is currently broken, disable for now
#  Text relocation remains                         referenced
#      against symbol                  offset      in file
#  st                                  0x634       tclDTrace.o
#  ld: fatal: relocations remain against allocatable but non-writable sections
# CONFIGURE_ARGS-5.10 += --enable-dtrace

CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL))

INSTALL_ARGS = install install-libraries install-private-headers install-tzdata install-msgs

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET = test

include gar/category.mk

post-install-modulated:
	@echo Creating tclsh link
	ln -s $(REN_TCLSH) $(DESTDIR)$(bindir)/tclsh
	perl -pi -e "s|/usr/local|$(prefix)|g" $(DESTDIR)$(libdir)/tclConfig.sh
	perl -pi -e "s|/usr/local|$(prefix)|g" $(DESTDIR)$(mandir)/man1/tclsh.1