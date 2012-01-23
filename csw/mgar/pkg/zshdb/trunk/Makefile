NAME = zshdb
VERSION = 0_gitcurrent
# PATCHLEVEL = 75eadce
CATEGORIES = utils

DESCRIPTION = ZSH Debugger
define BLURB
  This is a port and cleanup of my bash debugger bashdb
endef

# MASTER_SITES = http://cloud.github.com/downloads/rocky/zshdb/
GIT_REPOS = git://github.com/rocky/zshdb.git
GIT_USE_PROXY = 1
# GIT_TREEISH_zshdb.git = $(PATCHLEVEL)

# DISTFILES = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWzsh

CONFIGURE_ARGS = $(DIRPATHS)

ARCHALL = 1

include gar/category.mk

post-extract-isa-sparcv8:
	cd $(WORKSRC) && ./autogen.sh --with-zsh=/opt/csw/bin/zsh
	@$(MAKECOOKIE)
