# $Id$
#
NAME = hwloc
VERSION = 1.2.1
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = Hwloc provides abstraction of the hierarchical topology of modern architectures
define BLURB
  The Portable Hardware Locality (hwloc) software package provides a portable abstraction (across OS, versions, architectures, ...) of the hierarchical topology of modern architectures, including NUMA memory nodes, sockets, shared caches, cores and simultaneous multithreading. It also gathers various system attributes such as cache and memory information. It primarily aims at helping applications with gathering information about modern computing hardware so as to exploit it accordingly and efficiently.
endef

MASTER_SITES =  http://www.open-mpi.org/software/hwloc/v1.2/downloads/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWhwloc-dev
PACKAGES += CSWhwlocrt
CATALOGNAME_CSWhwloc-dev = hwloc_dev
CATALOGNAME_CSWhwlocrt   = hwlocrt
SPKG_DESC_CSWhwloc-dev  += $(DESCRIPTION), development files
SPKG_DESC_CSWhwlocrt    += $(DESCRIPTION), runtime

PKGFILES_CSWhwloc        = $(bindir)/.*
PKGFILES_CSWhwloc       += $(mandir)/man1/.*
PKGFILES_CSWhwlocrt      = $(call pkgfiles_lib,libhwloc.so.3)
PKGFILES_CSWhwloc-dev    = $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWhwloc      = CSWlibcairo2
RUNTIME_DEP_PKGS_CSWhwloc     += CSWhwlocrt
RUNTIME_DEP_PKGS_CSWhwlocrt    = CSWlibiconv2
RUNTIME_DEP_PKGS_CSWhwlocrt   += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWhwloc-dev  = CSWhwloc
RUNTIME_DEP_PKGS_CSWhwloc-dev += CSWhwlocrt

#BUILDDEPS = CSWautoconf

CONFIGURE_ARGS  = $(DIRPATHS)
#CONFIGURE_ARGS += --disable-visibility

BUILD64 = 1

GARFLAVOR = DBG

include gar/category.mk

