# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = libyaml
VERSION = 0.1.6
GARTYPE = v2

DESCRIPTION = A YAML 1.1 parser and emitter written in C

VENDOR_URL  ef
SPKG_SOURCEURL = http://pyyaml.org/wiki/LibYAML?version=20
MASTER_SITES = http://pyyaml.org/downlNAME     = yaml-$(VERSION)
DISTFILES    = $(DISTNAME).tar.gz
TEST_SCRIPTS =

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc
PACKAGING_PLATFORMS += solaris10-i386 solaris10-sparc

PATCHFILES += 0001-Solaris-headers-are-different.patch

PACKAGES += CSWlibyaml0-2
CATALOGNAME_CSWlibyaml0-2 = libyaml0_2
PKGFILES_CSWlibyaml0-2 += $(call baseisadirs,$(libdir),libyaml-0\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibyaml0-2 += $(DESCRIPTION), libyaml-0.so.2

PACKAGES += CSWlibyaml-dev
CATALOGNAME_CSWlibyaml-dev = libyaml_dev
SPKG_DESC_CSWlibyaml-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibyaml-dev += CSWlibyaml0-2
# PKGFILES is catchall

OBSOLETED_BY_CSWlibyaml-dev = CSWlibyaml
OBSOLETED_BY_CSWlibyaml0-1 = CSWlibyaml
FOREIGN_PACKAGES = CSWlibyaml0-1

CONFIGURE_ARGS = $(DIRPATHS)
BUILD64_LIBS_ONLY = 1

include gar/category.mk
