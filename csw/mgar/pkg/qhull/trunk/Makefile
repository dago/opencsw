NAME = qhull
VERSION = 2003.1
CATEGORIES = lib

DESCRIPTION = Qhull computes the convex hull and other hulls (with poly.c-qh_gethash.patch)
define BLURB
  Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
  halfspace intersection about a point, furthest-site Delaunay triangulation,
  and furthest-site Voronoi diagram. The source code runs in 2-d, 3-d, 4-d,
  and higher dimensions. Qhull implements the Quickhull algorithm for computing
  the convex hull. It handles roundoff errors from floating point arithmetic.
  It computes volumes, surface areas, and approximations to the convex hull.
  Qhull does not support constrained Delaunay triangulations, triangulation
  of non-convex surfaces, mesh generation of non-convex objects, or
  medium-sized inputs in 9-D and higher.
endef

MASTER_SITES = http://www.qhull.org/download/
DISTFILES  = $(DISTNAME).tar.gz

# From http://www.qhull.org/download/
PATCHDIRLEVEL = 2
PATCHFILES = poly.c-qh_gethash.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYING.txt

PACKAGES = CSWqhull CSWqhullrt

CATALOGNAME_CSWqhull = qhull
CATALOGNAME_CSWqhullrt = qhull_rt

SPKG_DESC_CSWqhull = Qhull computes the convex hull and other hulls
SPKG_DESC_CSWqhullrt = Qhull runtime libraries

PKGFILES_CSWqhullrt = $(PKGFILES_RT)

RUNTIME_DEP_PKGS_CSWqhull = CSWqhullrt

SPKG_SOURCEURL = http://www.qhull.org/

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

# This is for amd64 checked on i386
CHECKPKG_OVERRIDES = soname-not-found|libm.so.2

include gar/category.mk
