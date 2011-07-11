# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pinentry
VERSION = 0.8.1
CATEGORIES = utils

DESCRIPTION = Allows entering passwords into gpg-agent
define BLURB
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/pinentry/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.gnupg.org/related_software/pinentry/

BUILD_DEP_PKGS += CSWlibgnugetopt-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWgtk2devel
BUILD_DEP_PKGS += CSWlibatkdevel
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibcairo-dev

PACKAGES += CSWpinentry
SPKG_DESC_CSWpinentry = Allows entering passwords into gpg-agent (ncurses version)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpinentry += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWpinentry += CSWiconv
RUNTIME_DEP_PKGS_CSWpinentry += CSWlibncurses5

PACKAGES += CSWpinentry-gtk2
SPKG_DESC_CSWpinentry-gtk2 = Allows entering passwords into gpg-agent (gtk2 version)
PKGFILES_CSWpinentry-gtk2 += $(bindir)/pinentry-gtk-2
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWiconv
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWftype2
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWgtk2
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWlibatk
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWpango
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWglib2
RUNTIME_DEP_PKGS_CSWpinentry-gtk2 += CSWlibcairo2

# This is passed to curses/, but not pinentry/
EXTRA_CPPFLAGS += -I$(includedir)/ncurses

EXTRA_LINKER_FLAGS += -lgnugetopt

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-pinentry-curses
CONFIGURE_ARGS += --disable-pinentry-gtk
CONFIGURE_ARGS += --enable-pinentry-gtk2

# This is a symlink, we replace that by alternatives
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/pinentry

ALTERNATIVES_CSWpinentry = ncurses
ALTERNATIVES_CSWpinentry-gtk2 = gtk2
ALTERNATIVE_ncurses = $(bindir)/pinentry pinentry $(bindir)/pinentry-curses 100
ALTERNATIVE_gtk2 = $(bindir)/pinentry pinentry $(bindir)/pinentry-gtk-2 200

include gar/category.mk
