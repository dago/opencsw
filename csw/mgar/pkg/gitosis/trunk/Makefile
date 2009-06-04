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

define CSWgitosis_postinstall
#!/bin/sh

/usr/bin/passwd -N gitosis
endef

PACKAGES = CSWgitosis
CATALOGNAME_CSWgitosis = $(GARNAME)
ARCHALL_CSWgitosis = 1

PREREQUISITE_PKGS_CSWgitosis = CSWpython

REQUIRED_PKGS_CSWgitosis = CSWgit CSWpython CSWcswclassutils CSWpysetuptools

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

GITOSISHOME = /var/opt/csw/gitosis
CSWUG = gitosis:gitosis:Gitosis Host:$(GITOSISHOME):/bin/bash::
CSWUGD = $(INSTALLISADIR)/opt/csw/etc/pkg/CSW$(GARNAME)

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/CSWgitosis\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" }; $$$$3 ~ /\/var\/opt\/csw\/gitosis/ { $$$$2 = "ugfiles"; $$$$5 = "gitosis"; $$$$6 = "gitosis" } { print }'

SPKG_CLASSES = none cswusergroup ugfiles

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# Set a slightly altered revstamp to indicate that we're not using a
# pressed release.
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(PATCHLEVEL)

post-install-modulated:
	@( gmkdir -p $(CSWUGD); \
		echo "$(CSWUG)" > $(CSWUGD)/cswusergroup; \
	   gmkdir -p $(INSTALLISADIR)$(GITOSISHOME); \
	   echo 'PATH=/opt/csw/bin:$$PATH' > $(INSTALLISADIR)$(GITOSISHOME)/.bashrc; \
	   echo 'PATH=/opt/csw/bin:$$PATH' > $(INSTALLISADIR)$(GITOSISHOME)/.bash_profile; )
	$(MAKECOOKIE)
