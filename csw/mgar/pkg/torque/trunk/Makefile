# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = torque
VERSION = 3.0.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Batch job scheduling system

MASTER_SITES += http://www.adaptivecomputing.com/resources/downloads/torque/
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0001-daemonize-function-prototype.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-server-home

GARCOMPILER = GNU

# CSWtk 8.5 is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://www.clusterresources.com/products/torque-resource-manager.php

LICENSE = PBS_License_2.5.txt

PACKAGES = CSWtorque
SPKG_DESC_CSWtorque = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWtorque-dev += CSWlibtorque2

PACKAGES += CSWlibtorque2
CATALOGNAME_CSWlibtorque2 = libtorque2
PKGFILES_CSWlibtorque2 += $(call baseisadirs,$(libdir),libtorque\.so\.2\.0\.0)
PKGFILES_CSWlibtorque2 += $(call baseisadirs,$(libdir),libtorque\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibtorque2 += $(DESCRIPTION), libtorque.so.2
RUNTIME_DEP_PKGS_CSWtorque += CSWlibtorque2
RUNTIME_DEP_PKGS_CSWlibtorque2 += CSWlibgcc-s1

PACKAGES += CSWtorque-dev
CATALOGNAME_CSWtorque-dev = torque_dev
SPKG_DESC_CSWtorque-dev += $(DESCRIPTION), development files
PKGFILES_CSWtorque-dev += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWtorque += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWtorque += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWtorque += CSWlibreadline6

CHECKPKG_OVERRIDES_CSWtorque += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/qsub.1
CHECKPKG_OVERRIDES_CSWtorque += file-with-bad-content|/usr/local|root/opt/csw/bin/qsub

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
