NAME = gts
VERSION = 0.7.6
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU Triangulated Surface Library
define BLURB
  This is the GTS library. GTS stands for the GNU Triangulated
  Surface Library. It includes a number of useful functions to deal with
  triangulated surfaces including, but not limited to, multi-resolution
  models, Delaunay and Constrained Delaunay triangulations, set operations on
  surfaces (intersection, union etc ...), bounding-boxes trees for efficient
  collision and intersection detection, triangle strips generation for fast
  rendering.
endef

MASTER_SITES = $(SF_MIRRORS) 
DISTFILES    = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://gts.sGARCOMPILER = GCC4?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# 1343 is the group_id for the gts project on sourceforge
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=1343
UPSTREAM_USE_SF = 1

RUNTIME_DEP_PKGS = CSWggettextrt CSWglib2

CONFIGURE_ARGS = $(DIRPATHS) --disable-glibtest

PATCHFILES = gts-fa = 1
ISAEXEC = 1

PACKAGES += CSWlibgts0-7-5
CATALOGNAME_CSWlibgts0-7-5 = libgts0_7_5
PKGFILES_CSWlibgts0-7-5 += $(call baseisadirs,$(libdir),libgts-0\.7\.so\.5\.0\.1)
PKGFILES_CSWlibgts0-7-5 += $(call baseisadirs,$(libdir),libgts-0\.7\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibgts0-7-5 += $(DESCRIPTION), libgts-0.7.so.5
RUNTIME_DEP_PKGS_CSWlibgts0-7-5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgts0-7-5 += CSWlibglib2-0-0

PACKAGES += CSWgts-dev
CATALOGNAME_CSWgts-dev = gts_dev
SPKG_DESC_CSWgts-dev += $(DESCRIPTION), development files
PKGFILES_CSWgts-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWgts-dev += CSWlibgts0-7-5

PACKAGES += CSWgts
CATALOGNAME_CSWgts = gts
SPKG_DESC_CSWgts  += $(DESCRIPTION), utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgts += CSWlibgts0-7-5
RUNTIME_DEP_PKGS_CSWgts += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgts += CSWlibnetpbm10

# Some scripts are not +x
SKIPTEST = 1

include gar/category.mk
