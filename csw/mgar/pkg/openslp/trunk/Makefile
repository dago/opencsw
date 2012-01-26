# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = openslp
VERSION = 1.2.1
# http://prdownloads.sourceforge.net/openslp/openslp-1.2.1.tar.gz?download
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = Service Location Protocol
define BLURB
endef
SPKG_SOURCEURL = http://www.openslp.org/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES += CSWlibslp1
CATALOGNAME_CSWlibslp1 = libslp1
PKGFILES_CSWlibslp1 += $(call baseisadirs,$(libdir),libslp\.so\.1\.0\.1)
PKGFILES_CSWlibslp1 += $(call baseisadirs,$(libdir),libslp\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibslp1 += Service Location Protocol, libslp.so.1
RUNTIME_DEP_PKGS_CSWlibslp1 += CSWosslrt

PACKAGES += CSWopenslp-devel
CATALOGNAME_CSWopenslp-devel = openslp_devel
SPKG_DESC_CSWopenslp-devel = $(DESCRIPTION), development files
PKGFILES_CSWopenslp-devel += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWopenslp += CSWosslrt

include gar/category.mk
