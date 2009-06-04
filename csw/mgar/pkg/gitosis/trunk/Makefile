GARNAME = gitosis
GARVERSION = 0.2
# This represents the tip of master as of 20090516.  It is ahead of
# release/0.2
PATCHLEVEL = 73a03
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

REQUIRED_PKGS_CSWgitosis = CSWgit CSWpython CSWcswclassutils

GIT_REPOS = git://eagain.net/gitosis.git
GIT_USE_PROXY = 1
# We don't use a specific release tag as we want to get some fixes to
# support git 1.6+.  We'll simply package the tip of the public branch
# (as of 2009-05-16: 73a032520493f6b4186185d4826d12edb5614135)
GIT_TREEISH_gitosis.git = $(PATCHLEVEL)

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
INSTALL_ARGS = --root $(DESTDIR) --single-version-externally-managed

CSWUG = gitosis:gitosis:Gitosis Host:/var/opt/csw/gitosis:/bin/bash:m:
CSWUGD = $(INSTALLISADIR)/opt/csw/etc/pkg/CSW$(GARNAME)

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/CSWgitosis\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } { print }'

SPKG_CLASSES = none cswusergroup

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# Set a slightly altered revstamp to indicate that we're not using a
# pressed release.
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(PATCHLEVEL)

post-install-modulated:
	@( gmkdir -p $(CSWUGD); \
		echo "$(CSWUG)" > $(CSWUGD)/cswusergroup )
	$(MAKECOOKIE)