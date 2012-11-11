NAME = bashdb
VERSION = 4.0-0.4
# PATCHLEVEL = 75eadce
GARTYPE = v2

DESCRIPTION = Bash Debugger
define BLURB
  This is a port and cleanup of my bash debugger bashdb
endef

# MASTER_SITES = http://cloud.github.com/downloads/rocky/bashdb/
# GIT_REPOS = git://bashdb.git.sourceforge.net/gitroot/bashdb/bashdb/
# GIT_USE_PROXY = 1
# GIT_TREEISH_zshdb.git = $(PATCHLEVEL)

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.bz2
# PATCHFILES = $(notdir $(wildcard $(FILEDIR)/*.patch))
# PATCHFILES  = 0001-sf-Piwik-analytics.patch
PATCHFILES += 0002-Tolerance-for-Solaris-and-older-sed-sh-and-whatnot.patch
PATCHFILES += 0003-Tolerance-for-Solaris-and-older-sed-sh-and-whatnot.patch
PATCHFILES += 0004-Looks-like-sig-line-fixes-back-ported-to-bash-4.0.-N.patch
# PATCHFILES += 0005-Administrivia.patch
PATCHFILES += 0006-sig-SunOS.right-is-same-as-sig-41.right.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWbash

CONFIGURE_ARGS = $(DIRPATHS)

ARCHALL = 1

include gar/category.mk

#post-extract-isa-sparcv8:
#	cd $(WORKSRC) && ./autogen.sh --with-bash=/opt/csw/bin/bash
#	@$(MAKECOOKIE)
