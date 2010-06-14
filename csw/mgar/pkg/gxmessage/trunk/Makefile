# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = gxmessage
GARVERSION = 2.12.4
CATEGORIES = gnome
DESCRIPTION = An xmessage clone for GTK based desktops
define BLURB
endef
SPKG_SOURCEURL = http://homepages.ihug.co.nz/~trmusson/programs.html
MASTER_SITES  = http://homepages.ihug.co.nz/~trmusson/stuff/
MASTER_SITES += http://ftp.gnu.org/pub/gnu/gxmessage/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWgxmessage += CSWfconfig
RUNTIME_DEP_PKGS_CSWgxmessage += CSWftype2
RUNTIME_DEP_PKGS_CSWgxmessage += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgxmessage += CSWglib2
RUNTIME_DEP_PKGS_CSWgxmessage += CSWgtk2
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibatk
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgxmessage += CSWlibxext
RUNTIME_DEP_PKGS_CSWgxmessage += CSWpango
EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so
include gar/category.mk

post-install-modulated:
	ln -s gxmessage $(DESTDIR)$(bindir)/gmessage
	ln -s gxmessage $(DESTDIR)$(bindir)/xmessage
	@$(MAKECOOKIE)

# Otherwise it keeps finding /usr/bin/xgettext and failing.
PATH := /opt/csw/gnu:$(PATH)
