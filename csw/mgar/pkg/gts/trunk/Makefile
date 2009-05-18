GARNAME = gts
GARVERSION = 0.7.6
CATEGORIES = lib

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
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE) = 3788
UPSTREAM_USE_SF = 1

REQUIRED_PKGS = CSWggettextrt CSWglib2

CONFIGURE_ARGS = $(DIRPATHS) --disable-glibtest

PATCHFILES = gts-fabsf.diff

include gar/category.mk
