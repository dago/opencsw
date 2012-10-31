# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = logilab-astng
VERSION = 0.20.3
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Python Abstract Syntax Tree New Generation
PACKAGES = CSWpy-logilab-astng
CATALOGNAME_CSWpy-logilab-astng = py_logilab_astng
define BLURB
endef
SPKG_SOURCEURL = http://www.logilab.org/project/logilab-astng
MASTER_SITES = http://ftp.logilab.org/pub/astng/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyc
ARCHALL_CSWpy-logilab-astng = 1
RUNTIME_DEP_PKGS_CSWpy-logilab-astng = CSWpy-logilab-common
CHECKPKG_OVERRIDES_CSWpy-logilab-astng += surplus-dependency|CSWpy-logilab-common
include gar/category.mk
post-install-modulated:
	rm $(DESTDIR)$(SITE_PACKAGES)/logilab/__init__.py
	@$(MAKECOOKIE)
