# $Id$
#
NAME = hwloc
VERSION = 1.4.2
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = Hwloc provides abstraction of the hierarchical topology of modern architectures
define BLURB
  The Portable Hardware Locality (hwloc) software package provides a portable abstraction (across OS, versions, architectures, ...) of the hierarchical topology of modern architectures, including NUMA memory nodes, sockets, shared caches, cores and simultaneous multithreading. It also gathers various system attributes such as cache and memory information. It primarily aims at helping applications with gathering information about modern computing hardware so as to exploit it accordingly and efficiently.
endef

MASTER_SITES =  http://www.open-mpi.org/software/hwloc/v1.4/downloads/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc
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

RUNTIME_DEP_PKGS_CSWhwloc      = CSWlibcairo2
RUNTIME_DEP_PKGS_CSWhwloc     += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWhwloc     += CSWlibhwloc5
RUNTIME_DEP_PKGS_CSWlibhwloc5 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWhwloc-dev  = CSWhwloc
RUNTIME_DEP_PKGS_CSWhwloc-dev += CSWlibhwloc5

#BUILDDEPS = CSWautoconf

CONFIGURE_ARGS  = $(DIRPATHS)
#CONFIGURE_ARGS += --disable-visibility

include gar/category.mk

