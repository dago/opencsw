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
BUILD_DEP_PKGS += CSWglib
BUILD_DEP_PKGS += CSWgtk2devel

RUNTIME_DEP_PKGS_CSWpinentry += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWpinentry += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpinentry += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWpinentry += CSWglib
RUNTIME_DEP_PKGS_CSWpinentry += CSWgtk
RUNTIME_DEP_PKGS_CSWpinentry += CSWiconv
RUNTIME_DEP_PKGS_CSWpinentry += CSWglib2
RUNTIME_DEP_PKGS_CSWpinentry += CSWftype2
RUNTIME_DEP_PKGS_CSWpinentry += CSWgtk2
RUNTIME_DEP_PKGS_CSWpinentry += CSWlibatk
RUNTIME_DEP_PKGS_CSWpinentry += CSWfconfig
RUNTIME_DEP_PKGS_CSWpinentry += CSWpango
RUNTIME_DEP_PKGS_CSWpinentry += CSWlibcairo2

# This is passed to curses/, but not pinentry/
EXTRA_CPPFLAGS += -I$(includedir)/ncurses

EXTRA_LINKER_FLAGS += -lgnugetopt

include gar/category.mk
