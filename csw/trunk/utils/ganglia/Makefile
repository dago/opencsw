GARNAME = ganglia
GARVERSION = 3.0.4
CATEGORIES = utils

DESCRIPTION = A scalable distributed monitoring system
define BLURB
  Ganglia is a scalable distributed monitoring system for high-performance computing
  systems such as clusters and Grids. It is based on a hierarchical design targeted
  at federations of clusters.
endef

SF_PROJ = ganglia
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpackage,)

# This is attachment #45 from Ganglia bug
#   http://bugzilla.ganglia.info/cgi-bin/bugzilla/show_bug.cgi?id=77
PATCHFILES = $(GARNAME)-$(GARVERSION)-solaris-cc.patch

CONFIGURE_ARGS = $(DIRPATHS) --with-gmetad

include ../category.mk
