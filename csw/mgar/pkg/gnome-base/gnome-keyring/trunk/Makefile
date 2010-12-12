# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gnome-keyring
GNOME_VERSION = 2.28
VERSION = $(GNOME_VERSION).2
CATEGORIES = gnome
DESCRIPTION = Stores passwords and encryption keys in an encrypted file
define BLURB
endef
SPKG_SOURCEURL = http://live.gnome.org/GnomeKeyring
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(GNOME_VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME_CSWgnomekeyring = gnomekeyring
PACKAGES = CSWgnomekeyring
CONFIGURE_ARGS = $(DIRPATHS)
TEST_TARGET = check
PATCHFILES += inttypes.patch
PATCHFILES += inttypes-gck-rpc-module.c.patch
STRIP_LIBTOOL = 1
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWfconfig
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWftype2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgconf2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgcrypt
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWglib2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgpgerr
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgtk2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibatk
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibdbus
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibtasn1
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWpango

include gar/category.mk
