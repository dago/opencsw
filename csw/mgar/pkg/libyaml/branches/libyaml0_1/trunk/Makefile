# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = libyaml
VERSION = 0.1.2
GARTYPE = v2

DESCRIPTION = A YAML 1.1 parser and emitter written in C
define BLURB
endef

VENDOR_URL   = http://pyyaml.org/wiki/LibYAML?version=20
MASTER_SITES = http://pyyaml.org/download/libyaml/
DISTFILES    = yaml-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
TEST_SCRIPTS =

PACKAGES += CSWlibyaml0-1
CATALOGNAME_CSWlibyaml0-1 = libyaml0_1
PKGFILES_CSWlibyaml0-1 += $(call baseisadirs,$(libdir),libyaml-0\.so\.1\.1\.0)
PKGFILES_CSWlibyaml0-1 += $(call baseisadirs,$(libdir),libyaml-0\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibyaml0-1 += $(DESCRIPTION), libyaml-0.so.1
OBSOLETED_BY_CSWlibyaml0-1  = CSWlibyaml

CATALOGNAME_CSWlibyaml = libyaml_stub

CONFIGURE_ARGS = $(DIRPATHS)
BUILD64_LIBS_ONLY = 1
WORKSRC = $(WORKDIR)/yaml-$(VERSION)

include gar/category.mk
