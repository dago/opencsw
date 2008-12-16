GARNAME = git
GARVERSION = 1.6.0.5
CATEGORIES = devel

PREREQUISITE_PKGS = CSWasciidoc CSWossldevel CSWxmlto CSWbash CSWcurl

DESCRIPTION = Fast Version Control System
define BLURB
  Git is a popular version control system designed to handle
  very large projects with speed and efficiency; it is used
  mainly for various open source projects, most notably the Linux kernel.
endef

MASTER_SITES = http://kernel.org/pub/software/scm/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgit,)

PATCHFILES = doc-makefile.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS) --with-shell=/opt/csw/bin/bash

BUILD_ARGS = MSGFMT=gmsgfmt SHELL_PATH=/opt/csw/bin/bash all doc

INSTALL_ARGS = install-doc

include gar/category.mk

CFLAGS += -L$(libdir)

# for tail -n
PATH := /usr/xpg4/bin:$(PATH)