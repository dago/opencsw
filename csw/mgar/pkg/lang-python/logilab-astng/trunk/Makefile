# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = logilab-astng
VERSION = 0.24.3
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Python Abstract Syntax Tree New Generation
PACKAGES = CSWpy-logilab-astng
VENDOR_URL = http://www.logilab.org/project/logilab-astng
MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz
ARCHALL_CSWpy-logilab-astng = 1
RUNTIME_DEP_PKGS_CSWpy-logilab-astng = CSWpy-logilab-common
CHECKPKG_OVERRIDES_CSWpy-logilab-astng += surplus-dependency|CSWpy-logilab-common

include gar/category.mk

post-install-modulated:
	rm $(DESTDIR)$(libdir)/python/site-packages/logilab/__init__.py
	@$(MAKECOOKIE)
