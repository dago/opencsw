NAME = pyzmq
VERSION = 2.2.0
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = PyZMQ: Python bindings for 0MQ
define BLURB
  This package contains Python bindings for 0MQ. 0MQ is a lightweight and fast messaging implementation.
endef

MASTER_SITES = https://github.com/zeromq/pyzmq/downloads/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

CHECKPKG_OVERRIDES_CSWpy-pyzmq += pkginfo-opencsw-repository-uncommitted

BUILD_DEP_PKGS += CSWlibzmq1-dev
RUNTIME_DEP_PKGS_CSWpy-pyzmq += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pyzmq += CSWlibzmq1

PATCHFILES += 0001-These-flags-are-for-gnu-gcc-and-fail-on-suns-cc-comp.patch

#GARCOMPILER = GCC4

CONFIGURE_ARGS += $(DIRPATHS)

BUILD_ARGS += --zmq=/opt/csw

TEST_SCRIPTS = 

include gar/category.mk
