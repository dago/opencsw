GARNAME = gitosis
GARVERSION = 0.2
CATEGORIES = utils

DESCRIPTION = Software for hosting git repositories
define BLURB
Manage git repositories, provide access to them over SSH, with tight access control and not needing shell accounts.

gitosis aims to make hosting git repos easier and safer. It manages multiple repositories under one user account, using SSH keys to identify users. End users do not need shell accounts on the server, they will talk to one shared account that will not let them run arbitrary commands.
endef

PACKAGES = CSWgitosis
CATALOGNAME_CSWgitosis = $(GARNAME)
ARCHALL_CSWgitosis = 1

PREREQUISITE_PKGS_CSWgitosis = CSWpython

REQUIRED_PKGS_CSWgitosis = CSWgit CSWpython

GIT_REPOS = git://eagain.net/gitosis.git
GIT_USE_PROXY = 1
GIT_TREEISH_gitosis.git = release/$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES UPSTREAM_MASTER_SITES =

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

INSTALL_SCRIPTS = $(WORKSRC)/setup.py
#INSTALL_ARGS = --root $(DESTDIR) --single-version-externally-managed
INSTALL_ARGS = --root $(DESTDIR)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)