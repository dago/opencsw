NAME = pyzmq
VERSION = 2.2.0.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = PyZMQ: Python bindings for 0MQ
define BLURB
  This package contains Python bindings for 0MQ. 0MQ is a lightweight and fast messaging implementation.
endef

MASTER_SITES = https://github.com/downloads/zeromq/pyzmq/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-These-flags-are-for-gnu-gcc-and-fail-on-suns-cc-comp.patch
PATCHFILES += 0002-Include-inttypes-so-builds-on-solaris-9.patch

BUILD_DEP_PKGS += CSWlibzmq1-dev
RUNTIME_DEP_PKGS_CSWpy-pyzmq += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pyzmq += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-pyzmq += CSWlibzmq1
RUNTIME_DEP_PKGS_CSWpy-pyzmq += CSWlibgcc-s1

BUILD_ARGS += --zmq=$(prefix)

TEST_SCRIPTS = 

include gar/category.mk
