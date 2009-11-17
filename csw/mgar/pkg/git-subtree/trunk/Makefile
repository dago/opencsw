GARNAME = git-subtree
GARVERSION = 0.2
PATCHLEVEL = d20ac
CATEGORIES = devel

DESCRIPTION = Subtree support for git
define BLURB
An experimental alternative to the git-submodule command.
endef

PACKAGES = CSWgitsubtree
CATALOGNAME_CSWgitsubtree = git_subtree

ARCHALL_CSWgitsubtree = 1

PREREQUISITE_PKGS = CSWasciidoc CSWxmlto

REQUIRED_PKGS_CSWgitsubtree = CSWbash CSWgit

GIT_REPOS = git://github.com/apenwarr/git-subtree.git
GIT_TREEISH_git-subtree.git = $(PATCHLEVEL)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

SPKG_VERSION = $(GARVERSION)_$(PATCHLEVEL)

include gar/category.mk

install-custom:
	@(cd $(WORKSRC); \
		gsed 's#/bin/bash#/opt/csw/bin/bash#' git-subtree.sh > git-subtree.sh.new; \
		mv git-subtree.sh.new git-subtree.sh; \
		gmake DESTDIR=$(DESTDIR) INSTALL=/opt/csw/bin/ginstall prefix=/opt/csw install )
