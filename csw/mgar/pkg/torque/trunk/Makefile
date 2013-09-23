# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# ! still fails:
# checking for on_exit... no
# configure: error: Must have atexit() or on_exit()

NAME = torque
VERSION = 4.2.5
GARTYPE = v2

DESCRIPTION = Batch job scheduling system

# Their download process is broken. Our scheme won't work. This is the URL for the 4.2.5 version:
# http://www.adaptivecomputing.com/index.php?wpfb_dl=1677
# But the file downloaded has a different name, and only downloads after a HTTP redirect.

# MASTER_SITES += http://adaptive.wpengine.com/resources/downloads/torque/
DISTFILES += $(DISTNAME).tar.gz

# PATCHFILES += 0001-daemonize-function-prototype.patch
PATCHFILES += 0001-Disable-the-broken-lxml2-detection.patch
PATCHFILES += 0002-Replace-an-obsolete-macro.patch
PATCHFILES += 0003-Hardcode-the-name-of-libxml2-library-function-prototype.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-server-home

GARCOMPILER = GNU

# CSWtk 8.5 is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOadaptivecomputing.com/products/open-source/torque/

LICENSE = PBS_License_2.5.txt

# Their libxml2 detection is broken. There is a custom sed expression that is
# supposed to filter the output from libxml2-config, but it doesn't work.
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibssl-dev
# BUILD_DEP_PKGS += CSWautoconf
# BUILD_DEP_PKGS += CSWautomake
# BUILD_DEP_PKGS += CSWlibtool
# BUILD_DEP_PKGS += CSWpkgconfigPBS_License_2.5.txt

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

PATH := /o
# pre-configure:
# 	cd $(WORKSRC); autoreconf -fi
# 	$(MAKECOOKIE)
