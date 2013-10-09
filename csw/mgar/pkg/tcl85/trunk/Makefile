NAME = tcl
VERSION = 8.5.15
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Tcl programming language v8.5
define BLECTURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRNAME)$(VERSION)
DISTFILES  = $(DISTNAMEILES  = $(DISTNAME)-src.tar.gz

# Separate build for Solaris 10 with DTrace support
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

VENDOR_URL = http://www.tcl.tk/
LICENSEPATCHFILES += 0001-libsunmath-needs-fix-on-S9.patchSE = license.terms

REN_#olaris-9-.patch

# The dependencies on the ISAs differ, here's from tcl-x.y.z/unix/tcl.m4: 
#
#              # On Solaris 5.x i386 with the sunpro compiler we need to link
#              # with sunmath to get floating point#
# I think it's not really needed on recent Solaris 10, but it also appears
# to be a pain to remove, so I'll just let it be.t rounding control

PACKAGES  = CSWtcl
SPKG_DESC_CSWtcl = Tcl programming language 8.5
RUNTIME_DEP_PKGS_CSWtc_CSWtcl-$(GARCH))

# There are legacy packages depending on CSWtcl which require libtcl 8.4
FOREIGN_PACKAGES += CSWlibtcl8-4
RUNTIME_DEP_PKGS_CSWtcl += CSWlibtcl8-4
CHECKPKG_OVERRIDES_CSWtcl += surplus-dependency|CSWlibtcl8-4
CHECKPKG_OVERRIDES_CSWtcl += unidentified-dependeman/mann/clock.n

PACKAGES += CSWlibtcl8-5
SPKG_DESC_CSWlibtcl8-5 = $(DESCRIPTION), libraries
PKGFILES_CSWlibtcl8-5 += $(call pkgfiles_lib,libtcl8.5.so)
PKGFILES_CSWlibtcl8-5 += $(libdir)/tcl8.5/.*
# This dependency can not be tracked by checkpkg
RUNTIME_DEP_PKGS_CSWlibtcl8-5 += CRUNTIME_DEP_PKGS_CSWlibtcl8-5-i386 += CSWsunmath
RUNTIME_DEP_PKGS_CSWlibtcl8-5 += $(RUNTIME_DEP_PKGS_CSWlibtcl8-5-$(GARCH))CCHECKPKG_OVERRIDES_CSWlibtcl8-5 += surplus-dependency|CSWtcl8-tclmodules
itcl8-5-$(GARCH))

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
RUNTIME_DEP_PKGS_CSWtcl-dev# Enable 64 bits, but not for Solaris 9 x86
BUILD64_5.9_sparc  = 1
BUILD64_5.10_sparc = 1
BUILD64_5.9_i386   =
BUILD64_5.10_i386  = 1
BUILD64 = $(BUILD64_$(GAROSREL)_$(GARCH))cl8-5

BUILD64 = 1
ISAEXEC = 1

INCLUDE_FLAGS =

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGUREshared
CONFIGURE_ARGS += --enable-threads
# This is supposed to be needed for completeness, but what it does in configure
# is really questionable. Should not break stuff, though.
CONFIGURE_ARGS-64 += --enable-64bit
CONFIGURE_ARGS += CONFIGURE_ARGS-$(MEMORYMODEL)= --enable-threads

# DTrace support is currently broken, disable for now
#  Text relocation remains                         referenced
#      against symbol                  offset      in file
#  st                                  0x634       tclDTrace.o
#  ld: fatal: relocations remain against allocatable but non-writable sections
# CONFIGURE_ARGS-5.10 +#  --enable-dtrace

CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL))

INSTALL_ARGS = install install-libraries install-private-headers install-tzdata install-msgs

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET = test

include gar/category.mk

post-install-modulated:
	@echo Creating tclsh link
	ln -s $(REN_TCLSH) $(DESTDIR# Remove wrong path
	perl -pi -e "s|/usr/local|$(prefix)|g" \
		$(DESTDIR)$(libdir)/tclConfig.sh
	perl -pi -e "s|/usr/local|$(prefix)|g" \
		$(DESTDIR)$(mandir)/man1/tclsh.1
	# Remove compiler-specific arch references
	# Those compatible between GCC4 and Studio 12 are left in.
	gsed -i \
		-e '/^[^#]/s/-xO[0-5][^ ]* *//g' \
		-e '/^[^#]/s/-xarch=[^ ]* *//g' \
		-e '/^[^#]/s/-xchip=[^ ]* *//g' \
		-e '/^[^#]/s/-norunpath[^ ]* *//g' \
		-e '/^[^#]/s/-lCrun[^ ]* *//g' \
		-e '/^[^#]/s/-lCstd[^ ]* *//g' \
		-e '/^[^#]/s/-mtune=[^ ]* *//g' \
		-e '/^[^#]/s/-march=[^ ]* *//g' \
		-e '/^[^#]/s/-Wall *//g' \
		-e '/^[^#]/s/-pipe *//g' \
		-e '/^[^#]/s/-KPIC/-fPIC/g' \
		$(DESTDIR)$(libdir)/tclConfig.sh
	@$(MAKECOOKIE)

