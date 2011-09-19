# Only builds on Solaris 10

NAME = R
VERSION = 2.13.1
CATEGORIES = apps

DESCRIPTION = A language and environment for statistical computing and graphics
define BLURB
endef

MASTER_SITES = http://stat.ethz.ch/CRAN/src/base/R-2/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

PACKAGES       = CSWr-base
VENDOR_URL     = http://www.r-project.org/

RUNTIME_DEP_PKGS_CSWr-base += CSWsunmath 
RUNTIME_DEP_PKGS_CSWr-base += CSWjpeg
RUNTIME_DEP_PKGS_CSWr-base += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWr-base += CSWtcl
RUNTIME_DEP_PKGS_CSWr-base += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWr-base += CSWlibz1
RUNTIME_DEP_PKGS_CSWr-base += CSWlibintl8
RUNTIME_DEP_PKGS_CSWr-base += CSWtiff
RUNTIME_DEP_PKGS_CSWr-base += CSWliblzma5
RUNTIME_DEP_PKGS_CSWr-base += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWr-base += CSWlibicu46
RUNTIME_DEP_PKGS_CSWr-base += CSWtk
RUNTIME_DEP_PKGS_CSWr-base += CSWpango
RUNTIME_DEP_PKGS_CSWr-base += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWr-base += CSWss12f95rt
RUNTIME_DEP_PKGS_CSWr-base += CSWglib2

# Temporary overrides
CHECKPKG_OVERRIDES_CSWr-base += file-with-bad-content
CHECKPKG_OVERRIDES_CSWr-base += bad-rpath-entry

# There is a special wrapper that takes care of finding the sonames.
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/R/bin/exec/R
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/R/lib/libRlapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/R/library/KernSmooth/libs/KernSmooth.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/R/library/Matrix/libs/Matrix.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/R/library/mgcv/libs/mgcv.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/R/library/stats/libs/stats.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/R/modules/lapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/R/library/Matrix/libs/Matrix.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/R/library/mgcv/libs/mgcv.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/R/modules/lapack.so

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check-recommended

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk
