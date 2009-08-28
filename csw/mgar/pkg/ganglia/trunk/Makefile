GARNAME = ganglia
GARVERSION = 3.1.2
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

PACKAGES = CSWgangliart CSWgangliaagent

CATALOGNAME_CSWgangliart	= ganglia_rt
CATALOGNAME_CSWgangliaagent	= ganglia_agent

SPKG_DESC_CSWgangliart		= Ganglia runtime libraries
SPKG_DESC_CSWgangliaagent	= Ganglia performance monitoring agent gmond

REQUIRED_PKGS_CSWgangliart = CSWexpat CSWlibconfuse CSWapache2rt
REQUIRED_PKGS_CSWgangliaagent = CSWexpat CSWlibconfuse CSWapache2rt
REQUIRED_PKGS_CSWgangliaagent += CSWgangliart

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=43021
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# This is attachment #45 from Ganglia bug
#   http://bugzilla.ganglia.info/cgi-bin/bugzilla/show_bug.cgi?id=77
#PATCHFILES = $(GARNAME)-$(GARVERSION)-solaris-cc.patch

CONFIGURE_ARGS = $(DIRPATHS)

# Don't build gmetad (not tested yet on Solaris, more deps required to build)
CONFIGURE_ARGS += --without-gmetad

# Reduce dependencies, no gettext:
CONFIGURE_ARGS += --disable-nls

PKGFILES_CSWgangliart = $(libdir)/libganglia.*

include gar/category.mk
