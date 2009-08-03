# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = libatomic-ops
GARVERSION = 1.2
CATEGORIES = lib
DESCRIPTION = Portable library for atomic operations
define BLURB
endef
SPKG_SOURCEURL = http://www.hpl.hp.com/research/linux/atomic_ops/
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/liba/libatomic-ops/
PATCHFILES = solaris-$(GARVERSION).patch
DISTFILES  = $(GARNAME)_$(GARVERSION).orig.tar.gz $(PATCHFILES)
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = libatomic_ops
TEST_SCRIPTS =
WORKSRC = $(WORKDIR)/$(CATALOGNAME)-$(GARVERSION)
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
