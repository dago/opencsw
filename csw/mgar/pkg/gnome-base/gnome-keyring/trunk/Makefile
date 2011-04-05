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
CATALOGNAME_CSWgnomekeyring = gnomekeyring
PACKAGES = CSWgnomekeyring
CONFIGURE_ARGS = $(DIRPATHS)
TEST_TARGET = check
PATCHFILES += inttypes.patch
PATCHFILES += inttypes-gck-rpc-module.c.patch
STRIP_LIBTOOL = 1

SPKG_DESC_CSWgnomekeyring = $(DESCRIPTION)

PACKAGES += CSWlibgcr0
CATALOGNAME_CSWlibgcr0 = libgcr0
PKGFILES_CSWlibgcr0 += $(call baseisadirs,$(libdir),libgcr\.so\.0\.0\.0)
PKGFILES_CSWlibgcr0 += $(call baseisadirs,$(libdir),libgcr\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgcr0 += Stores passwords and encryption keys in an encrypted file, libgcr.so.0
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibgcr0

PACKAGES += CSWlibgnome-keyring0
CATALOGNAME_CSWlibgnome-keyring0 = libgnome_keyring0
PKGFILES_CSWlibgnome-keyring0 += $(call baseisadirs,$(libdir),libgnome-keyring\.so\.0\.1\.1)
PKGFILES_CSWlibgnome-keyring0 += $(call baseisadirs,$(libdir),libgnome-keyring\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgnome-keyring0 += Stores passwords and encryption keys in an encrypted file, libgnome-keyring.so.0
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibgnome-keyring0
# Only needed for backward-compatibility reasons.
CHECKPKG_OVERRIDES_CSWgnomekeyring += surplus-dependency|CSWlibgnome-keyring0

PACKAGES += CSWlibgp11-0
CATALOGNAME_CSWlibgp11-0 = libgp11_0
PKGFILES_CSWlibgp11-0 += $(call baseisadirs,$(libdir),libgp11\.so\.0\.0\.0)
PKGFILES_CSWlibgp11-0 += $(call baseisadirs,$(libdir),libgp11\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgp11-0 += Stores passwords and encryption keys in an encrypted file, libgp11.so.0
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibgp11-0

PACKAGES += CSWgnomekeyring-dev
PKGFILES_CSWgnomekeyring-dev += $(libdir)/libgcr.so
PKGFILES_CSWgnomekeyring-dev += $(libdir)/libgnome-keyring.so
PKGFILES_CSWgnomekeyring-dev += $(libdir)/libgp11.so
PKGFILES_CSWgnomekeyring-dev += $(PKGFILES_DEVEL)
CATALOGNAME_CSWgnomekeyring-dev = gnomekeyring_dev
SPKG_DESC_CSWgnomekeyring-dev = Development files for gnome keyring


RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgpgerr
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgtk2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWftype2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibatk
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWpango
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgcrypt
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibdbus
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWgconf2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWfconfig
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWglib2


RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWlibgp11-0
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWgpgerr
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWlibtasn1-3
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWlibatk
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWgcrypt
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibgcr0 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibgnome-keyring0 += CSWlibdbus
RUNTIME_DEP_PKGS_CSWlibgnome-keyring0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnome-keyring0 += CSWglib2
RUNTIME_DEP_PKGS_CSWgnomekeyring-dev += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWgnomekeyring-dev += CSWlibgp11-0
RUNTIME_DEP_PKGS_CSWgnomekeyring-dev += CSWlibgcr0
RUNTIME_DEP_PKGS_CSWlibgp11-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgp11-0 += CSWglib2
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnomekeyring += CSWlibtasn1-3

include gar/category.mk
