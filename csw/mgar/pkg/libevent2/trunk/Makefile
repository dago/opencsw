NAME = libevent
VERSION = 2.0.21
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Event notification library
define BLURB
  The libevent API provides a mechanism to execute a callback function when a
  specific event occurs on a file descriptor or after a timeout has been
  reached. Furthermore, libevent also support callbacks due to signals or
  regular timeouts.
endef

MASTER_SITES = http://github.com/downloads/libevent/libevent/
DISTNAME = $(NAME)-$(VERSION)-stable
DISTFILES += $(DVENDOR_URL = http://www.monkey.org/~provos/libevent/
LICENSE = LICENSE

BUILD_DEP_PKGS += CSWlibssl-devS += CSWossldevel

PACKAGES += CSWlibevent2-0-5
SPKG_DESC_CSWlibevent2-0-5 = Event notification library 2.0, libevent-2.0.so.5
PKGFILES_CSWlibevent2-0-5 = $(call pkgfiles_lib,libevent-2.0.so.5)

PACKAGES += CSWlibevent-core2-0-5
SPKG_DESC_CSWlibevent-core2-0-5 = Event notification library 2.0, libevent_core-2.0.so.5
PKGFILES_CSWlibevent-core2-0-5 = $(call pkgfiles_lib,libevent_core-2.0.so.5)

PACKAGES += CSWlibevent-extra2-0-5
SPKG_DESC_CSWlibevent-extra2-0-5 = Event notification library 2.0, libevent_extra-2.0.so.5
PKGFILES_CSWlibevent-extra2-0-5 = $(call pkgfiles_lib,libevent_extra-2.0.so.5)

PACKAGES += CSWlibevent-openssl2-0-5
SPKG_DESC_CSWlibevent-openssl2-0-5 = Event notification library 2.0, libevent_openssl-2.0.so.5
PKGFILES_CSWlibevent-openssl2-0-5 = $(call pkgfiles_lib,libevent_openssl-2.0.so.5)
RUNTIME_DEP_PKGS_CSWlibevent-oplibssl1-0-0-0-5 += CSWosslrt

PACKAGES += CSWlibevent-pthreads2-0-5
SPKG_DESC_CSWlibevent-pthreads2-0-5 = Event notification library 2.0, libevent_pthreads-2.0.so.5
PKGFILES_CSWlibevent-pthreads2-0-5 = $(call pkgfiles_lib,libevent_pthreads-2.0.so.5)

PACKAGES += CSWlibevent-dev
SPKG_DESC_CSWlibevent-dev = Development files for libevent*-2.0.so.5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-core2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-extra2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-openssl2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-pthreads2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWpython
OBSOLETED_BY_CSWlibevent-dev += CSREINPLACEMENTS += bash
REINPLACE_MATCH_bash = \#!/bin/sh
REINPLACE_WITH_bash = \#!/bin/bash
REINPLACE_FILES_bash += test/test.shCSWlibevent-devel

# We don't need it and if defined the test breaks
NOISALIST = 1
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATBUILD64_LIBS_ONLY = 1

TEST_TARGET = verify

include gar/category.mk

