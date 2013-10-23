# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = buildbot
VERSION = 0.8.8
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

MASTER_SITES = $(PYPI_MIRROR)
PATCHFILES  = buildbot-tail.patch
#PATCHFILES += buildbot-debug.patch
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWbuildbot
SPKG_DESC_CSWbuildbot = A system to automate the compile/test cycle
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWbuildbot += CSWcoreutils
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-twisted
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-zope-interface
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-sqlalchemy
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-jinja2
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-tempita
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-decorator
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-openssl

CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-twisted
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-sqlalchemy
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-zope-interface
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-jinja2
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-tempita
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-decorator
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-openssl

# This is more like an application than a python module
CHECKPKG_OVERRIDES_CSWbuildbot += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWbuildbot += catalogname-does-not-start-with-py_

ARCHALL_CSWbuildbot = 1

# There seems to be 'trial' missing
SKIPTEST ?= 1

include gar/category.mk
