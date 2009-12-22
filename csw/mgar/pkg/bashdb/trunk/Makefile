GARNAME = bashdb
GARVERSION = 0_gitcurrent
# PATCHLEVEL = 75eadce
CATEGORIES = utils

DESCRIPTION = Bash Debugger
define BLURB
  This is a port and cleanup of my bash debugger bashdb
endef

# MASTER_SITES = http://cloud.github.com/downloads/rocky/bashdb/
GIT_REPOS = git://bashdb.git.sourceforge.net/gitroot/bashdb/bashdb
GIT_USE_PROXY = 1
# GIT_TREEISH_zshdb.git = $(PATCHLEVEL)

# DISTFILES = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWbash

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

ARCHALL = 1

include gar/category.mk

post-extract-isa-sparcv8:
	cd $(WORKSRC) && ./autogen.sh --with-bash=/opt/csw/bin/bash
	@$(MAKECOOKIE)
