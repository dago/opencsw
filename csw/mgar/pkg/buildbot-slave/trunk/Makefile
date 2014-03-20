# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = buildbot-slave
VERSION = 0.8.8
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = BuildBot Slave Daemon

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# Buildbot is 2.7 only and the server is Solaris 10 only
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWbuildbot-slave
SPKG_DESC_CSWbuildbot-slave = BuildBot Slave Daemon
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWbuildbot-slave += CSWpy-twisted
CHECKPKG_OVERRIDES_CSWbuildbot-slave += surplus-dependency|CSWpy-twisted

ARCHALL_CSWbuildbot-slave = 1

# This is more like an application than a python module
CHECKPKG_OVERRIDES_CSWbuildbot-slave += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWbuildbot-slave += catalogname-does-not-start-with-py_

# logwatcher uses 'tail -f -n 0' only available on XPG4 tail or GNU tail, let's prefer XPG4
REINPLACEMENTS += tail
REINPLACE_MATCH_tail = /usr/bin/tail
REINPLACE_WITH_tail = /usr/xpg4/bin/tail
REINPLACE_FILES_tail += buildslave/scripts/logwatcher.py

# There seems to be 'trial' missing
SKIPTEST ?= 1

include gar/category.mk
