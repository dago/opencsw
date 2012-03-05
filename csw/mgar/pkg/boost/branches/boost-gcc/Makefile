# $Id$

NAME = boost
VERSION = 1.49.0
CATEGORIES = lib
GARTYPE = v2
# GARTYPE = v2-build64only

define BLURB
  Boost was begun by members of the C++ standards committee Library Working
  Group to provide free peer-reviewed portable libraries to the C++ community.
  An additional objective is to establish "existing practice" and provide
  reference implementations so that the Boost libraries are suitable for
  eventual standardization. Indeed, the explicit intent is to propose many of
  these libraries for inclusion in the C++ Standard Library. The Boost Graph
  Library, formerly known as the Generic Graph Component Library (GGCL), is a
  collection of graph algorithms and data structures created in the generic
  programming style of the Standard Template Library (STL).
endef

DESCRIPTION = Free peer-reviewed portable C++ source libraries

MASTER_SITES = $(SF_MIRROR)/$(NAME)/
DISTVERSION = $(subst .,_,$(VERSION))
DISTNAME = $(NAME)_$(DISTVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
# ISA_DEFAULT_sparc-5.10 = sparcv8plus

PATCHFILES += 0001-Don-t-try-to-use-fchmodat.patch

prefix = /opt/csw/gxx

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=7586
UPSTREAM_USE_SF = 1

GARCOMPILER = GNU
TOOLSET = gcc
COMPILER_SUFFIX_PKG = -gcc
COMPILER_SUFFIX_CAT = _gcc

PACKAGES += CSWboost$(COMPILER_SUFFIX_PKG)
CATALOGNAME_CSWboost$(COMPILER_SUFFIX_PKG) += boost$(COMPILER_SUFFIX_CAT)
SPKG_DESC_CSWboost$(COMPILER_SUFFIX_PKG) = $(DESCRIPTION)
# The boost build system is hard to harness.
CHECKPKG_OVERRIDES_CSWboost$(COMPILER_SUFFIX_PKG) += bad-rpath-entry

PACKAGES += CSWboost$(COMPILER_SUFFIX_PKG)-dev
SPKG_DESC_CSWboost$(COMPILER_SUFFIX_PKG)-dev = $(DESCRIPTION), development files
PKGFILES_CSWboost$(COMPILER_SUFFIX_PKG)-dev = $(PKGFILES_DEVEL)

LICENSE = LICENSE_1_0.txt

BUILD_DEP_PKGS += CSWstar

CONFIGURE_SCRIPTS = boost
BUILD_SCRIPTS = boost
INSTALL_SCRIPTS = bjam

EXTRA_FLAGS = -std=c99
EXTRA_LINKER_FLAGS = -R/opt/csw/lib/\\\$$ISALIST
BUILD64_ONLY = 1

BUILD_ARGS += toolset=$(TOOLSET)
BUILD_ARGS += --prefix=$(DESTDIR)$(prefix)
BUILD_ARGS += --libdir=$(DESTDIR)$(libdir)
BUILD_ARGS += link=shared
BUILD_ARGS += cflags='$(CFLAGS)'
BUILD_ARGS += cxxflags='$(CXXFLAGS)'
BUILD_ARGS += linkflags='$(LDFLAGS) $(LD_OPTIONS)'
# Stop on the first error
BUILD_ARGS += -q
# Display commands as you run them, I want to know what you are doing there
BUILD_ARGS += -d+2
BUILD_ARGS += include='/opt/csw/gcc/include'
BUILD_ARGS += --debug-building
BUILD_ARGS += address-model=64
# We don't have 64-bit Python
BUILD_ARGS += --without-python

TEST_SCRIPTS =

JAMDIR_sparc = solarissparc
JAMDIR_i386 = solarisx86
JAMDIR = $(JAMDIR_$(GARCH))

# BUILD64 = 1

# These can't be just passed from Make's PARALLELMFLAGS because of the -l flag.
BJAM_PARALLELMFLAGS_current9s = -j 32
BJAM_PARALLELMFLAGS_current9x = -j 5
BJAM_PARALLELMFLAGS = $(BJAM_PARALLELMFLAGS_$(call modulation2host))


PACKAGES += CSWlibboost-chrono1-49-0-gxx
PKGFILES_CSWlibboost-chrono1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_chrono\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-chrono1-49-0-gxx += $(DESCRIPTION), libboost_chrono.so.1.49.0

PACKAGES += CSWlibboost-date-time1-49-0-gxx
PKGFILES_CSWlibboost-date-time1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_date_time\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-date-time1-49-0-gxx += $(DESCRIPTION), libboost_date_time.so.1.49.0

PACKAGES += CSWlibboost-filesystem1-49-0-gxx
PKGFILES_CSWlibboost-filesystem1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_filesystem\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-filesystem1-49-0-gxx += $(DESCRIPTION), libboost_filesystem.so.1.49.0

PACKAGES += CSWlibboost-graph1-49-0-gxx
PKGFILES_CSWlibboost-graph1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_graph\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-graph1-49-0-gxx += $(DESCRIPTION), libboost_graph.so.1.49.0

PACKAGES += CSWlibboost-iostreams1-49-0-gxx
PKGFILES_CSWlibboost-iostreams1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_iostreams\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-iostreams1-49-0-gxx += $(DESCRIPTION), libboost_iostreams.so.1.49.0

PACKAGES += CSWlibboost-math-c99-1-49-0-gxx
PKGFILES_CSWlibboost-math-c99-1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_math_c99\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-math-c99-1-49-0-gxx += $(DESCRIPTION), libboost_math_c99.so.1.49.0

PACKAGES += CSWlibboost-math-c99f1-49-0-gxx
PKGFILES_CSWlibboost-math-c99f1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_math_c99f\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-math-c99f1-49-0-gxx += $(DESCRIPTION), libboost_math_c99f.so.1.49.0

PACKAGES += CSWlibboost-math-c99l1-49-0-gxx
PKGFILES_CSWlibboost-math-c99l1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_math_c99l\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-math-c99l1-49-0-gxx += $(DESCRIPTION), libboost_math_c99l.so.1.49.0

PACKAGES += CSWlibboost-math-tr1-1-49-0-gxx
PKGFILES_CSWlibboost-math-tr1-1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_math_tr1\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-math-tr1-1-49-0-gxx += $(DESCRIPTION), libboost_math_tr1.so.1.49.0

PACKAGES += CSWlibboost-math-tr1f1-49-0-gxx
PKGFILES_CSWlibboost-math-tr1f1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_math_tr1f\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-math-tr1f1-49-0-gxx += $(DESCRIPTION), libboost_math_tr1f.so.1.49.0

PACKAGES += CSWlibboost-math-tr1l1-49-0-gxx
PKGFILES_CSWlibboost-math-tr1l1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_math_tr1l\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-math-tr1l1-49-0-gxx += $(DESCRIPTION), libboost_math_tr1l.so.1.49.0

PACKAGES += CSWlibboost-prexmon1-49-0-gxx
PKGFILES_CSWlibboost-prexmon1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_prg_exec_monitor\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-prexmon1-49-0-gxx += $(DESCRIPTION), libboost_prg_exec_monitor.so.1.49.0

PACKAGES += CSWlibboost-prog-opts1-49-0-gxx
PKGFILES_CSWlibboost-prog-opts1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_program_options\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-prog-opts1-49-0-gxx += $(DESCRIPTION), libboost_program_options.so.1.49.0

PACKAGES += CSWlibboost-random1-49-0-gxx
PKGFILES_CSWlibboost-random1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_random\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-random1-49-0-gxx += $(DESCRIPTION), libboost_random.so.1.49.0

PACKAGES += CSWlibboost-regex1-49-0-gxx
PKGFILES_CSWlibboost-regex1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_regex\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-regex1-49-0-gxx += $(DESCRIPTION), libboost_regex.so.1.49.0

PACKAGES += CSWlibboost-s13n1-49-0-gxx
PKGFILES_CSWlibboost-s13n1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_serialization\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-s13n1-49-0-gxx += $(DESCRIPTION), libboost_serialization.so.1.49.0

PACKAGES += CSWlibboost-signals1-49-0-gxx
PKGFILES_CSWlibboost-signals1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_signals\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-signals1-49-0-gxx += $(DESCRIPTION), libboost_signals.so.1.49.0

PACKAGES += CSWlibboost-system1-49-0-gxx
PKGFILES_CSWlibboost-system1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_system\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-system1-49-0-gxx += $(DESCRIPTION), libboost_system.so.1.49.0

PACKAGES += CSWlibboost-thread1-49-0-gxx
PKGFILES_CSWlibboost-thread1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_thread\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-thread1-49-0-gxx += $(DESCRIPTION), libboost_thread.so.1.49.0

PACKAGES += CSWlibboost-timer1-49-0-gxx
PKGFILES_CSWlibboost-timer1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_timer\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-timer1-49-0-gxx += $(DESCRIPTION), libboost_timer.so.1.49.0

PACKAGES += CSWlibboost-ut-fwk1-49-0-gxx
PKGFILES_CSWlibboost-ut-fwk1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_unit_test_framework\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-ut-fwk1-49-0-gxx += $(DESCRIPTION), libboost_unit_test_framework.so.1.49.0

PACKAGES += CSWlibboost-wave1-49-0-gxx
PKGFILES_CSWlibboost-wave1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_wave\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-wave1-49-0-gxx += $(DESCRIPTION), libboost_wave.so.1.49.0

PACKAGES += CSWlibboost-ws13n1-49-0-gxx
PKGFILES_CSWlibboost-ws13n1-49-0-gxx += $(call baseisadirs,$(libdir),libboost_wserialization\.so\.1\.49\.0(\.\d+)*)
SPKG_DESC_CSWlibboost-ws13n1-49-0-gxx += $(DESCRIPTION), libboost_wserialization.so.1.49.0

RUNTIME_DEP_PKGS_CSWlibboost-chrono1-49-0-gxx += CSWlibboost-system1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-chrono1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-chrono1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-signals1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-signals1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-date-time1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-date-time1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-system1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-system1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-math-tr1-1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-math-tr1-1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-filesystem1-49-0-gxx += CSWlibboost-system1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-filesystem1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-filesystem1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-graph1-49-0-gxx += CSWlibboost-regex1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-graph1-49-0-gxx += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibboost-graph1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-graph1-49-0-gxx += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibboost-graph1-49-0-gxx += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSWlibboost-graph1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-wave1-49-0-gxx += CSWlibboost-thread1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-wave1-49-0-gxx += CSWlibboost-system1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-wave1-49-0-gxx += CSWlibboost-date-time1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-wave1-49-0-gxx += CSWlibboost-filesystem1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-wave1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-wave1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-math-tr1f1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-math-tr1f1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-math-tr1l1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-math-tr1l1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-ut-fwk1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-ut-fwk1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-regex1-49-0-gxx += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibboost-regex1-49-0-gxx += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSWlibboost-regex1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-regex1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-regex1-49-0-gxx += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibboost-ws13n1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-ws13n1-49-0-gxx += CSWlibboost-s13n1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-ws13n1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-s13n1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-s13n1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-math-c99-1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-math-c99-1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-math-c99f1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-math-c99f1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-prexmon1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-filesystem1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-math-tr1-1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-math-c99l1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-thread1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-math-c99f1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-iostreams1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-signals1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-wave1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-system1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-ut-fwk1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-date-time1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-math-c99-1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-s13n1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-regex1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-ws13n1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-prog-opts1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-math-tr1l1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-math-tr1f1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-random1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-timer1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-chrono1-49-0-gxx
RUNTIME_DEP_PKGS_CSWboost-gcc-dev += CSWlibboost-graph1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-prog-opts1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-prog-opts1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-prexmon1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-prexmon1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-iostreams1-49-0-gxx += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibboost-iostreams1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-iostreams1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-iostreams1-49-0-gxx += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibboost-timer1-49-0-gxx += CSWlibboost-system1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-timer1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-timer1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-timer1-49-0-gxx += CSWlibboost-chrono1-49-0-gxx
RUNTIME_DEP_PKGS_CSWlibboost-thread1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-thread1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-random1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-random1-49-0-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibboost-math-c99l1-49-0-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibboost-math-c99l1-49-0-gxx += CSWlibstdc++6

# Overridees for bad-rpath-entry are needed because the Boost build system
# apparently interpolates $ISALIST, leaving us with "/opt/csw/lib/"
# with the slash at the end.
CHECKPKG_OVERRIDES_CSWlibboost-chrono1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-date-time1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-filesystem1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-graph1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-iostreams1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-math-c99-1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-math-c99f1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-math-c99l1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-math-tr1-1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-math-tr1f1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-math-tr1l1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-prexmon1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-prog-opts1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-random1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-regex1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-s13n1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-signals1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-system1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-thread1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-timer1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-ut-fwk1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-wave1-49-0-gxx += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWlibboost-ws13n1-49-0-gxx += bad-rpath-entry

# The shared-lib-pkgname-mismatch overrides are here, because some pkgnames
# based on file names are too long and pkgmk can't handle them.
CHECKPKG_OVERRIDES_CSWlibboost-s13n1-49-0-gxx += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWlibboost-ut-fwk1-49-0-gxx += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWlibboost-prog-opts1-49-0-gxx += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWlibboost-prexmon1-49-0-gxx += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWlibboost-ws13n1-49-0-gxx += shared-lib-pkgname-mismatch

include gar/category.mk

PYTHON_ROOT = $(prefix)
PYTHON_VERSION = 2.6
export PYTHON_ROOT PYTHON_VERSION

# Boost is not extractable with SUNW tar nor GNU tar :-(
tar-bz-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	/opt/csw/bin/star -bz -x -C $(EXTRACTDIR) -f $(DOWNLOADDIR)/$*
	@$(MAKECOOKIE)

configure-boost:
	( cd $(WORKSRC) && \
	  ./bootstrap.sh $(TOOLSET))
	# && \
	#  mkdir -p $(DESTDIR)$(bindir) && \
	#  cp bin.$(JAMDIR)/bjam $(DESTDIR)$(bindir) )
	@$(MAKECOOKIE)

build-boost:
	cd $(WORKSRC) && \
		./b2 \
		  -d+2 \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS)
	@$(MAKECOOKIE)

install-bjam:
	cd $(WORKSRC) && \
		./b2 \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS) \
			install
	@$(MAKECOOKIE)
