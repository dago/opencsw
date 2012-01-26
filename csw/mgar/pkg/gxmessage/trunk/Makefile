# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gxmessage
VERSION = 2.12.4
CATEGORIES = gnome
GARTYPE = v2
DESCRIPTION = An xmessage clone for GTK based desktops
define BLURB
endef
SPKG_SOURCEURL = http://homepages.ihug.co.nz/~trmusson/programs.html
MASTER_SITES  = http://homepages.ihug.co.nz/~trmusson/stuff/
MASTER_SITES += http://ftp.gnu.org/pub/gnu/gxmessage/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
EXTRA_INC = $(prefix)/include/gtk-2.0
CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWgxmessage += CSWfconfig
RUNTIME_DEP_PKGS_CSWgxmessage += CSWftype2
RUNTIME_DEP_PKGS_CSWgxmessage += CSWglib2
RUNTIME_DEP_PKGS_CSWgxmessage += CSWgtk2
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibatk
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgxmessage += CSWpango
PATCHFILES += 0001-removing-a-usr-local-reference.patch
include gar/category.mk

post-install-modulated:
	ln -s gxmessage $(DESTDIR)$(bindir)/gmessage
	ln -s gxmessage $(DESTDIR)$(bindir)/xmessage
	@$(MAKECOOKIE)

# Otherwise it keeps finding /usr/bin/xgettext and failing.
PATH := /opt/csw/gnu:$(PATH)
