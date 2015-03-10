#####################################################################
# OpenCSW build recipe for jq
#
# Copyright 2013 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = jq
VERSION = 1.4
GARTYPE = v2

DESCRIPTION = A lightweight and flexible command-line JSON processor.
define BLURB
	jq is like sed for JSON data, you can use it to slice and filter and map
	and transform structured data with the same ease that sed, awk, grep and
	friends let you play with text.
endef

MASTER_SITES = http://stedolan.github.io/jq/download/source/
DISTFILES += $(DISTNAME).tar.gz
VENDOR_URL = http://stedolan.github.io/jq/

PACKAGES += CSWjq
SPKG_DESC_CSWjq = A lightweight and flexible command-line JSON processor.
# PKGFILES is catchall

PACKAGES += CSWlibjq1
SPKG_DESC_CSWlibjq1 = A C API interface to jq JSON representation and for running jq programs from C applications
PKGFILES_CSWlibjq1 += $(call pkgfiles_lib,libjq.so.1)
RUNTIME_DEP_PKGS_CSWlibjq1 += CSWlibgcc-s1

PACKAGES += CSWlibjq-dev
SPKG_DESC_CSWlibjq-dev = Development support files for C API interface to jq
PKGFILES_CSWlibjq-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibjq-dev += CSWlibjq1

GARCOMPILER = GNU

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

# WARNING: valgrind is required to test jq
SKIPTEST ?= 1

include gar/category.mk

