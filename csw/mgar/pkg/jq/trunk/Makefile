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

PACKAGES = CSWjq CSWlibjq1 CSWlibjq-dev

SPKG_DESC_CSWjq = A lightweight and flexible command-line JSON processor.
SPKG_DESC_CSWlibjq1 = A C API interface to jq JSON representation and for running jq programs from C applications
SPKG_DESC_CSWlibjq-dev = Development support files for C API interface to jq

RUNTIME_DEP_PKGS_CSWlibjq1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibjq-dev += CSWlibjq1

###### Upstream and opencsw files information #######

MASTER_SITES = http://stedolan.github.io/jq/download/source/
DISTFILES  = $(DISTNAME).tar.gz

PKGFILES_CSWjq = $(bindir)/.*
PKGFILES_CSWjq += $(mandir)/man1/.* $(mandir)/man5/.* $(mandir)/man7/.*
PKGFILES_CSWjq += $(docdir)/jq/.*

PKGFILES_CSWliblibjq1 = $(PKGFILES_RT)
PKGFILES_CSWliblibjq1 += $(docdir)/libjq1/.*

PKGFILES_CSWlibjq-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibjq-dev += $(docdir)/libjq-dev/.*

##### Build and installation information #####

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 

include gar/category.mk

