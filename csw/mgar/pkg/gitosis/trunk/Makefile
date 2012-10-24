NAME = gitosis
VERSION = 0.2
# This represents the tip of master as of 20090516.  It is ahead of
# release/0.2
PATCHLEVEL = 73a03
CATEGORIES = python
GARTYPE = v2

VENDOR_URL = http://eagain.net/gitweb/?p=gitosis.git

DESCRIPTION = Software for hosting git repositories
define BLURB
Manage git repositories, provide access to them over SSH, with tight access control and not needing shell accounts.

gitosis aims to make hosting git repos easier and safer. It manages multiple repositories under one user account, using SSH keys to identify users. End users do not need shell accounts on the server, they will talk to one shared account that will not let them run arbitrary commands.
endef

define CSWgitosis_postinstall
#!/bin/sh

# in case the gitosis package was still using /bin/bash.
/usr/bin/getent passwd gitosis | /usr/xpg4/bin/grep -q ':/bin/bash'
if [ $$? -eq 0 ]; then
	echo Updating shell for gitosis account to /opt/csw/bin/bash.
	/usr/sbin/usermod -s /opt/csw/bin/bash gitosis
fi

echo See $(docdir)/$(NAME)/README.csw for first use instructions.
endef

PACKAGES = CSWgitosis
CATALOGNAME_CSWgitosis = $(NAME)
SPKG_DESC_CSWgitosis = $(DESCRIPTION)
ARCHALL_CSWgitosis = 1
BUILD_DEP_PKGS_CSWgitosis = CSWpython CSWpysetuptools
RUNTIME_DEP_PKGS_CSWgitosis = CSWgit CSWpysetuptools CSWbash

# this is not for release.
PACKAGES += CSWgitosis-test
SPKG_DESC_CSWgitosis-test = The test suite for gitosis
PKGFILES_CSWgitosis-test = .*/test/.*
ARCHALL_CSWgitosis-test = 1
CHECKPKG_OVERRIDES_CSWgitosis-test += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWgitosis-test += catalogname-does-not-start-with-py_

GIT_REPOS = git://github.com/tv42/gitosis.git
GIT_USE_PROXY = 1
# We don't use a specific release tag as we want to get some fixes to
# support git 1.6+.  We'll simply package the tip of the public branch
# (as of 2009-05-16: 73a032520493f6b4186185d4826d12edb5614135)
GIT_TREEISH_gitosis.git = $(PATCHLEVEL)

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES UPSTREAM_MASTER_SITES =

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root $(DESTDIR) --single-version-externally-managed

GITOSISHOME = /var/opt/csw/gitosis
CSWUG = gitosis:gitosis:Gitosis Host:$(GITOSISHOME):/opt/csw/bin/bash:::NP
CSWPKGD = $(INSTALLISADIR)/opt/csw/etc/pkg/CSW$(NAME)

USERGROUP = /opt/csw/etc/pkg/CSWgitosis/cswusergroup
INETDCONF = /opt/csw/etc/pkg/CSWgitosis/inetd.conf

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/var\/opt\/csw\/gitosis/ { $$$$2 = "ugfiles"; $$$$5 = "gitosis"; $$$$6 = "gitosis" }; { print }'

CHECKPKG_OVERRIDES_CSWgitosis += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWgitosis += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWgitosis += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWgitosis += surplus-dependency|CSWpysetuptools
CHECKPKG_OVERRIDES_CSWgitosis += surplus-dependency|CSWgit

LICENSE = COPYING

PYCOMPILE = 1

include gar/category.mk

# override the category exclusion
_MERGE_EXCLUDE_CATEGORY =

# Set a slightly altered revstamp to indicate that we're not using a
# pressed release.
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(PATCHLEVEL)

post-install-modulated:
	@( gmkdir -p $(CSWPKGD); \
		echo "$(CSWUG)" > $(CSWPKGD)/cswusergroup; \
	   ginstall -m 0644 $(FILEDIR)/inetd.conf $(CSWPKGD); \
	   gmkdir -p $(INSTALLISADIR)$(GITOSISHOME); \
	   echo 'PATH=/opt/csw/bin:$$PATH' > $(INSTALLISADIR)$(GITOSISHOME)/.bashrc; \
	   echo 'PATH=/opt/csw/bin:$$PATH' > $(INSTALLISADIR)$(GITOSISHOME)/.bash_profile; \
	   gmkdir -p $(INSTALLISADIR)/opt/csw/share/doc/gitosis; \
	   gcp files/README.csw $(INSTALLISADIR)/opt/csw/share/doc/gitosis/; \
	   gcp $(WORKSRC)/*rst $(WORKSRC)/*conf $(WORKSRC)/etc* $(INSTALLISADIR)/opt/csw/share/doc/gitosis/; )
	$(MAKECOOKIE)
