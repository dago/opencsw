# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = hwloc
VERSION = 1.2.1
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = Hwloc provides an abstraction of the hierarchical topology of modern architectures
define BLURB
  The Portable Hardware Locality (hwloc) software package provides a portable abstraction (across OS, versions, architectures, ...) of the hierarchical topology of modern architectures, including NUMA memory nodes, sockets, shared caches, cores and simultaneous multithreading. It also gathers various system attributes such as cache and memory information. It primarily aims at helping applications with gathering information about modern computing hardware so as to exploit it accordingly and efficiently.
endef

MASTER_SITES =  http://www.open-mpi.org/software/hwloc/v1.2/downloads/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 


# Checkpkg suggests adding the following lines to the GAR recipe:
# # This is a summary; see above for details.
# # (If CSWhwloc-dev doesn't exist yet)
PACKAGES += CSWhwloc-dev
CATALOGNAME_CSWhwloc-dev = hwloc_dev
SPKG_DESC_CSWhwloc += $(DESCRIPTION), development files
PKGFILES_CSWhwloc-dev += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWhwloc += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWhwloc += CSWlibxml2-2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-visibility

BUILD64 = 1

include gar/category.mk

