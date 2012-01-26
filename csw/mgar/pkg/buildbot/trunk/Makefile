# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = buildbot
VERSION = 0.7.12
PATCHLEVEL =
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A system to automate the compile/test cycle
define BLURB
  The BuildBot is a system to automate the compile/test cycle required by most
  software projects to validate code changes. By automatically rebuilding and
  testing the tree each time something has changed, build problems are
  pinpointed quickly, before other developers are inconvenienced by the
  failure. The guilty developer can be identified and harassed without human
  intervention. By running the builds on a variety of platforms, developers who
  do not have the facilities to test their changes everywhere before checkin
  will at least know shortly afterwards whether they have broken the build or
  not. Warning counts, lint checks, image size, compile time, and other build
  parameters can be tracked over time, are more visible, and are therefore
  easier to improve. 
endef

MASTER_SITES = $(SF_MIRROR)
PATCHFILES  = buildbot-tail.patch
PATCHFILES += buildbot-debug.patch
DISTFILES  = $(NAME)-$(VERSION)$(PATCHLEVEL).tar.gz $(PATCHFILES)

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PYCOMPILE = 1

RUNTIME_DEP_PKGS += CSWcoreutils
RUNTIME_DEP_PKGS += CSWtwisted
RUNTIME_DEP_PKGS += CSWzope

ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = buildbot
TEST_SCRIPTS =
INSTALL_SCRIPTS = buildbot

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)$(PATCHLEVEL)

CHECKPKG_OVERRIDES_CSWbuildbot += unidentified-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWtwisted
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWzope
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWcoreutils

build-buildbot:
	(cd $(WORKSRC); python setup.py build)
	@$(MAKECOOKIE)

install-buildbot:
	(cd $(WORKSRC); python setup.py install --root=$(DESTDIR))
	@$(MAKECOOKIE)

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)

include gar/category.mk
