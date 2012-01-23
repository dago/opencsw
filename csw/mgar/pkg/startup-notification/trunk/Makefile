# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = startup-notification
VERSION = 0.9
CATEGORIES = lib
DESCRIPTION = Reference implementation of the startup notification protocol
define BLURB
endef
SPKG_SOURCEURL = http://www.freedesktop.org/wiki/Software/startup-notification
MASTER_SITES = http://www.freedesktop.org/software/startup-notification/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = startup_notif
PACKAGES = CSWstartupnotif
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64_LIBS_ONLY = 1
EXTRA_PKG_CONFIG_DIRS = /opt/csw/lib
include gar/category.mk

# post-merge:
# 	ginstall -m 755 -d $(PKGROOT)/opt/csw/lib
# 	ln -s          ../X11/lib/libstartup-notification-1.so.0 \
# 	   $(PKGROOT)/opt/csw/lib/libstartup-notification-1.so.0
# 	@$(MAKECOOKIE)
