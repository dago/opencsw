# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = geeqie
VERSION = 1.0
CATEGORIES = gnome
GARTYPE = v2
DESCRIPTION = A lightweight image viewer, forked from GQview
VENDOR_URL = http://geeqie.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LDFLAGS = -lsocket

RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgeeqie += CSWliblcms1

# For some mysterious reason, this library is only used on intel.
RUNTIME_DEP_PKGS_CSWgeeqie_sparc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgeeqie_sparc += $(RUNTIME_DEP_PKGS_CSWgeeqie_$(GARCH))

CHECKPKG_OVERRIDES_CSWgeeqie += file-with-bad-content|/usr/share|root/opt/csw/bin/geeqie

CHECKPKG_OVERRIDES_CSWgeeqie += bad-rpath-entry|/lib|opt/csw/bin/geeqie
CHECKPKG_OVERRIDES_CSWgeeqie += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/bin/geeqie
CHECKPKG_OVERRIDES_CSWgeeqie += bad-rpath-entry|/opt/SUNWspro/lib/rw7|opt/csw/bin/geeqie
CHECKPKG_OVERRIDES_CSWgeeqie += bad-rpath-entry|/opt/SUNWspro/lib/sparc|opt/csw/bin/geeqie

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
