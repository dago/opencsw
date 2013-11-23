# $Id$

NAME = octave
VERSION = 3.6.4
GARTYPE = v2

DESCRIPTION = The GNU Octave language for numerical computations
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-make-script-work-with-Solaris-sh.patch 0002-workaround-conflict-with-gets.patch

# using the sunperf library for blas and lapack and therefore also the
# sunf90 Fortran compiler but the C++ will only build with g++. 
GARCOMPILER = GNU
CONFIGURE_ARGS = $(DIRPATHS) F77=sunf90 --with-lapack=sunperf --with-blas=sunperf --without-opengl LD_LIBRARY_PATH="/opt/csw/lib" LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib" FFLAGS="-xO2"

include gar/category.mk

