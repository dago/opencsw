# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = libyaml
VERSION = 0.1.4
GARTYPE = v2

DESCRIPTION = A YAML 1.1 parser and emitter written in C

VENDOR_URL  ef
SPKG_SOURCEURL = http://pyyaml.org/wiki/LibYAML?version=20
MASTER_SITES = http://pyyaml.org/downlNAME     = yaml-$(VERSION)
DISTFILES    = $(DISTNAME).tar.gz
TEST_SCRIPTS =

PACKAGES += CSWlibyaml0-2
CATALOGNAME_CSWlibyaml0-2 = libyaml0_2
PKGFILES_CSWlibyaml0-2 += $(call baseisadirs,$(libdir),libyaml-0\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibyaml0-2 += $(DESCRIPTION), libyaml-0.so.2

PACKAGES += CSWlibyaml-dev
CATALOGNAME_CSWlibyaml-dev = libyaml_dev
SPKG_DESC_CSWlibyaml-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibyaml-dev += CSWlibyaml0-2
# PKGFILES is catchall

# CSWlibyaml used to contain the dev bits.
# It is an old packages that was replaced by CSWlibyaml0_1  
CHECKPKG_OVERRIDES_CSWlibyaml-dev += file-collision|/opt/csw/lib/libyaml.so|CSWlibyaml|CSWlibyaml-dev
CHECKPKG_OVERRIDES_CSWlibyaml-dev += file-collision|/opt/csw/include/yaml.h|CSWlibyaml|CSWlibyaml-dev

C
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
BUILD
include gar/category.mk
