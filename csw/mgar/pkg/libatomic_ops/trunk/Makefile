# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libatomic-ops
VERSION = 1.2
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = Portable library for atomic operations
define BLURB
endef
SPKG_SOURCEURL = http://www.hpl.hp.com/research/linux/atomic_ops/
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/liba/libatomic-ops/
PATCHFILES = solaris-$(VERSION).patch
DISTFILES  = $(NAME)_$(VERSION).orig.tar.gz $(PATCHFILES)
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = libatomic_ops
TEST_SCRIPTS =
WORKSRC = $(WORKDIR)/$(CATALOGNAME)-$(VERSION)
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
