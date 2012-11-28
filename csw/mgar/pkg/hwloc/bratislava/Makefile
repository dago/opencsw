# $Id$
#
NAME = hwloc
VERSION = 1.5.1
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = Hwloc provides abstraction of the hierarchical topology of modern architectures
define BLURB
  The Portable Hardware Locality (hwloc) software package provides a portable abstraction (across OS, versions, architectures, ...) of the hierarchical topology of modern architectures, including NUMA memory nodes, sockets, shared caches, cores and simultaneous multithreading. It also gathers various system attributes such as cache and memory information. It primarily aims at helping applications with gathering information about modern computing hardware so as to exploit it accordingly and efficiently.
endef

MASTER_SITES =  http://www.open-mpi.org/software/hwloc/v1.5/downloads/
DISTFILES  = $BUILD64 = 1
ISAEXECc
BUILD64_LIBS_ONLY = 1

PACKAGES  = CSWhwloc
PACKAGES += CSWhwloc-dev
PACKAGES += CSWhwloc-doc
PACKAGES += CSWlibhwloc5

ARCHALL_CSWhwloc-doc = 1

SPKG_DESC_CSWhwloc        += $(DESCRIPTION)
SPKG_DESC_CSWhwloc-dev    += $(DESCRIPTION), development files
SPKG_DESC_CSWhwloc-doc    += $(DESCRIPTION), documentation
SPKG_DESC_CSWlibhwloc5    += $(DESCRIPTION), runtime

PKGFILES_CSWlibhwloc5      = $(call pkgfiles_lib,libhwloc.so.5)
PKGFILES_CSWhwloc-dev      = $(PKGFILES_DEVEL)
PKGFILES_CSWhwloc-doc      = $(PKGFILES_DOC)

RUNTIME_DEP_PKGS_CSWhwloc     += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWhwloc     += CSWlibhwloc5
RUNTIME_DEP_PKGS_CSWlibhwloc5 += CSWlibxml2-2
Rlibhwloc5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWhwloc-dev  = CSWhwloc
RUNTIME_DEP_PKGS_CSWhwloc-dev += CSWlibhwloc5

CHECKPKG_OVERRIDES_CSWhwloc-dev += disallowed-path
CHECKPKG_OVERRIDES_CSWhwloc-dev += bad-location-of-file
CHECKPKG_OVERRIDES_CSWlibhwloc5 += disallowed-path
CHECKPKG_OVERRIDES_CSWlibhwloc5 += disallowed-path
CHECKPKG_OVERRIDES_CSWlibhwloc5 += bad-location-of-file
CHECKPKG_OVERRIDES_CSWhwloc += disallowed-path
CHECKPKG_OVERRIDES_CSWhwloc += bad-location-of-file
CHECKPKG_OVERRIDES_CSWhwloc-doc += disallowed-path
CHECKPKG_OVERRIDES_CSWhwloc-doc += bad-location-of-file

deGARCOMPILER = GNU
COMMON_PKG_DEPENDS =
INCLUDE_COMMONDIRS = 1DDEPS = CSWautoconf

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-cairo
#CONFIGURE_ARGS += --disable-visibility

includ