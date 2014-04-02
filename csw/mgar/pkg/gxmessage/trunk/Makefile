# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gxmessage
VERSION = 2.12.4
CATEGORIES = gnome
GARTYPE = v2
DESCRIPTION = Clone of xmessage for GTK based desktops

VENDOR_URL = http://homepages.ihug.co.nz/~trmusson/programs.html
MASTER_SITES  = http://homepages.ihug.co.nz/~trmusson/stuff/
MASTER_SITES += http://ftp.gnu.org/pub/gnu/gxmessage/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

EXTRA_INC = $(prefix)/include/gtk-2.0
CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibpango1-0-0
PATCHFILES += 0001-removing-a-usr-local-reference.patch
include gar/category.mk

post-install-modulated:
	ln -sf gxmessage $(DESTDIR)$(bindir)/gmessage
	install -d -m 755 $(DESTDIR)$(prefix)/gnu
	ln -sf ../bin/gxmessage $(DESTDIR)$(prefix)/gnu/xmessage
	@$(MAKECOOKIE)

# Otherwise it keeps finding /usr/bin/xgettext and failing.
PATH := /opt/csw/gnu:$(PATH)
