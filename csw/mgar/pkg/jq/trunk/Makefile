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
VERSION = 1.3
GARTYPE = v2

DESCRIPTION = A lightweight and flexible command-line JSON processor.
define BLURB
	jq is like sed for JSON data, you can use it to slice and filter and map
	and transform structured data with the same ease that sed, awk, grep and
	friends let you play with text.
endef

###### Upstream and opencsw files information #######

MASTER_SITES = http://stedolan.github.io/jq/download/source/
DISTFILES  = $(DISTNAME).tar.gz

# The jq test suite uses valgrind to check for memory leaks
# but we don't have it on Solaris
PATCHFILES += 0001-remove-valgrind-usage-in-tests.patch

##### Build and installation information #####

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 

include gar/category.mk

