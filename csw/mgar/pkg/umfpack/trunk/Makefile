NAME = umfpack
VERSION = 5.5.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A set of routines for solving unsymmetric sparse linear systems
define BLURB
  UMFPACK is a set of routines for solving unsymmetric sparse linear systems,
  Ax=b, using the Unsymmetric MultiFrontal method. Written in ANSI/ISO C, with
  a MATLAB (Version 6.0 and later) interface. Appears as a built-in routine
  (for lu, backslash, and forward slash) in MATLAB. Includes a MATLAB interface,
  a C-callable interface, and a Fortran-callable interface. Note that "UMFPACK"
  is pronounced in two syllables, "Umph Pack". It is not "You Em Ef Pack".
endef

MASTER_SITES = http://www.cise.ufl.edu/research/sparse/umfpack/
MASTER_SITES += http://www.cise.ufl.edu/research/sparse/UFconfig/
MASTER_SITES += http://www.cise.ufl.edu/research/sparse/amd/
DISTNAME = UMFPACK
DISTFILES  = UMFPACK-$(VERSION).tar.gz
DISTFILES += UFconfig-3.6.1.tar.gz
DISTFILES += AMD-2.2.2.tar.gz

BUILD64_LIBS_ONLY = 1
# CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =

# From UFconfig/UFconfig.mk
OPT_FLAGS_SOS_32 = -KPIC -dalign -xc99=%none -Xc -xlibmieee -xO5 -xlibmil
OPT_FLAGS_SOS_64 = -fast -KPIC -xc99=%none -xlibmieee -xlibmil -Xc
OPT_FLAGS_SOS = $(OPT_FLAGS_SOS_$(MEMORYMODEL))

FFLAGS = -fast -KPIC -dalign -xlibmil -m64
BLAS = -xlic_lib=sunperf
LAPACK =

BUILD_OVERRIDE_DIRS = CFLAGS FFLAGS BLAS LAPACK

include gar/category.mk
