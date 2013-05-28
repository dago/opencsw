# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = jasper
VERSION = 1.900.1
GARTYPE = v2

DESCRIPTION = JasPer reference implementation of the codec specified by JPEG-2000

MASTER_SITES = http://www.ece.uvic.ca/~frodo/jasper/software/
DISTFILES += $(DISTNAME).zip

VENDOR_URL = http://www.ece.uvic.ca/~frodo/jasper/

BUILD_DEP_PKGS += CSWmesa
BUILD_DEP_PKGS += CSWfreeglut
BUILD_DEP_PKGS += CSWlibjpeg-dev

PACKAGES += CSWjasper
SPKG_DESC_CSWjasper = JasPer reference implementation of the codec specified by JPEG-2000
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWjasper += CSWlibjasper1
RUNTIME_DEP_PKGS_CSWjasper += CSWmesa
RUNTIME_DEP_PKGS_CSWjasper += CSWfreeglut

PACKAGES += CSWlibjasper1
SPKG_DESC_CSWlibjasper1 = Library for JPEG-2000 access, libjasper.so.1
PKGFILES_CSWlibjasper1 += $(call pkgfiles_lib,libjasper.so.1)
RUNTIME_DEP_PKGS_CSWlibjasper1 += CSWlibjpeg7

PACKAGES += CSWlibjasper-dev
SPKG_DESC_CSWlibjasper-dev = Development files for libjasper.so.1
PKGFILES_CSWlibjasper-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibjasper-dev += CSWlibjasper1

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-shared

include gar/category.mk

