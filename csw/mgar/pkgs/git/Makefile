GARNAME = git
GARVERSION = 1.5.5.1
CATEGORIES = devel

DESCRIPTION = Fast Version Control System
define BLURB
  Git is a popular version control system designed to handle
  very large projects with speed and efficiency; it is used
  mainly for various open source projects, most notably the Linux kernel.
endef

MASTER_SITES = http://kernel.org/pub/software/scm/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgit,)

PREREQUISITE_PKGS = CSWasciidoc CSWossldevel

CONFIGURE_ARGS = $(DIRPATHS)

BUILD_ARGS = MSGFMT=gmsgfmt all doc

INSTALL_ARGS = install-doc

include ../category.mk

CFLAGS += -L$(libdir)
