# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = numpy
VERSION = 1.9.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Standard numerical array library for python
define BLURB
  numpy is the standard numerical array library for python, the successor
  to Numeric and numarray. numpy provides fast operations for homogeneous
  data sets and common mathematical operations like correlations, standard
  deviation, fourier transforms, and convolutions.
endef

SPKG_SOURCEURL = http://numpy.scipy.org/
DISTFILES = $(DISTNAME).tar.gz

# PATCHFILES += 0001-mvec-is-a-SPARC-only-library.patch

# This is a special library, Solaris 10 only, sorry
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

RUNTIME_DEP_PKGS_CSWpy-numpy += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-numpy += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-numpy += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-numpy += CSWsunmath

RUNTIME_DEP_PKGS_CSWpy-numpy-sparc += CSWss12f95rt
RUNTIME_DEP_PKGS_CSWpy-numpy += $(RUNTIME_DEP_PKGS_CSWpy-numpy-$(GARCH))

# the so version (and package names) for libsunperf differ depending
# on platform
SUNPERF_SO_sparc = 8
SUNPERF_SO_i386 = 4
SUNPERF_SO = $(SUNPERF_SO_$(GARCH))
RUNTIME_DEP_PKGS_CSWpy-numpy += CSWlibsunperf$(SUNPERF_SO)

LICENSE = LICENSE.txt

EXTRA_CFLAGS_2_6 = -xnorunpath
EXTRA_CFLAGS += $(EXTRA_CFLAGS_$(PYTHON_VERSION))

EXTRA_BUILD_ENV += ATLAS=None
EXTRA_BUILD_ENV += BLAS=$(CC_HOME)/lib/libsunperf.so
EXTRA_BUILD_ENV += LAPACK=$(libdir)/libsunmath.so

TEST_SCRIPTS =
INSTALL_ARGS += --root=$(DESTDIR)

REINPLACE_USRLOCAL += $(SITE_PACKAGES)/numpy/site.cfg.example
REINPLACE_USRLOCAL += $(SITE_PACKAGES)/numpy/distutils/system_info.py
REINPLACE_WHEN_USRLOCAL = postinstall

# because we need to force the use of libsunperf from (initially) the
# studio install dir, the RPATH gets munged, regardless of
# -xnorunpath.  Our library path takes precedence though so we do not relay on things from studio at runtime.
CHECKPKG_OVERRIDES_CSWpy-numpy += bad-rpath-entry

# The static libs are needed for other modules depending on this one
#   https://www.opencsw.org/mantis/view.php?id=5207
MERGE_EXCLUDE_STATICLIBS =
CHECKPKG_OVERRIDES_CSWpy-numpy += discouraged-path-in-pkgmap|/opt/csw/lib/python2.6/site-packages/numpy/core/lib/libnpymath.a
CHECKPKG_OVERRIDES_CSWpy-numpy += discouraged-path-in-pkgmap|/opt/csw/lib/python2.7/site-packages/numpy/core/lib/libnpymath.a

include gar/category.mk

post-extract:
	@# The tarball contains multiple git repos - yuck!
	cd $(WORKSRC) && rm -rf .git doc/sphinxext/.git doc/scipy-sphinx-theme/.git
	@$(MAKECOOKIE)
