GARNAME = clusterit
GARVERSION = 2.5
CATEGORIES = net

DESCRIPTION = Suite of tools for managing large clusters of machines
define BLURB
   This is a collection of clustering tools, to turn your ordinary everyday pile of UNIX workstations into a speedy parallel beast. Initially this work was based on the work of IBM's PSSP, and copied heavily from the ideas there. Its also lightly based on the work pioneered in GLUnix.
endef

MASTER_SITES = $(SF_MIRROR)/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWclusterit,)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
