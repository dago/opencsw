# $Id$
# Only builds on Solaris 10

NAME = R
VERSION = 3.1.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A language and environment for statistical compuefine BLURB
endef

MASTER_SITES = http://stat.ethz.c$(shell echo $(VERSION) | awk -F. '{print $$1}')/CRAN/src/base/R-2/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

PACKAGES       = CSWr-base
VENDOR_URL     = http://www.r-project.org/

RUNTIME_DEP_PKGS_CSWr-base += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWr-bas52
RUNTIME_DEP_PKGS_CSWr-base += CSWlibicuuc52e += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWr-base += CSWlibintl8
RUNTIME_DEP_PKGS_CSWr-base += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWr-base += CSWliblzma5
RUNTIME_DEP_PKGS_CSWr-5-15
RUNTIME_DEP_PKGS_CSWr-base += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWr-base += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWr-base += CSWlibz1
RUNTIME_DEP_PKGS_CSWr-base += CSWsunmath
RUNTIME_DEP_PKGS_CSWr-base += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWr-base += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWr-base += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWr-base += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWr-base += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWr-base += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWr-base += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWr-base += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWr-base += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWr-base += CSWlibgfortran3

# These are because of linker anomaly
CHECKPKG_OVERRIDES_CSWr-base += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWr-base += surplus-dependency|CSWlibglib2-0-0CSWr-base += CSWtk

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
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/bin/exec/R
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/library/Matrix/libs/Matrix.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/library/stats/libs/stats.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/sparcv9/R/library/Matrix/libs/Matrix.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/sparcv9/R/library/mgcv/libs/mgcv.so
CHECKPKG_OVERRIDES_CSWr-base += sonlapacknot-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/library/stats/libs/stats.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/R/library/stats/libs/stats.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/modules/lapack.so
CHECKPKG_OVERRIDES_CSWr-base += sonlapacknot-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/modules/lapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/lib/libRlapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/library/mgcv/libs/mgcv.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/sparcv9/R/library/KernSmooth/libs/KernSmooth.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/amd64/R/bin/exec/R
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/amd64/R/library/Matrix/libs/Matrix.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/amd64/R/library/stats/libs/stats.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/amd64/R/library/Matrix/libs/Matrix.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/amd64/R/library/mgcv/libs/mgcv.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/amd64/R/modules/lapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needed|by|opt/csw/lib/amd64/R/modules/lapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/amd64/R/lib/libRlapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/amd64/R/library/mgcv/libs/mgcv.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRblas.so|is|needed|by|opt/csw/lib/amd64/R/library/KernSmooth/lmodules/lapack.so
CHECKPKG_OVERRIDES_CSWr-base += soname-not-found|libRlapack.so|is|needamd64/R/library/stats/libs/stats.so

GARCOMPILER = GNU

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check-recommended

include gar/category.mk
