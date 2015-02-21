# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = buildbot-slave
VERSION = 0.8.10
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = BuildBot Slave Daemon

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswbuildslave.xml

# Buildbot is 2.7 only and the server is Solaris 10 only
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWbuildbot-slave
SPKG_DESC_CSWbuildbot-slave = BuildBot Slave Daemon
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWbuildbot-slave += CSWpy-twisted
CHECKPKG_OVERRIDES_CSWbuildbot-slave += surplus-dependency|CSWpy-twisted

ARCHALL_CSWbuildbot-slave = 1

# That is the URI for the DTD
CHECKPKG_OVERRIDES_CSWbuildbot-slave += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswbuildslave.xml

# This is more like an application than a python module
CHECKPKG_OVERRIDES_CSWbuildbot-slave += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWbuildbot-slave += catalogname-does-not-start-with-py_

# There seems to be 'trial' missing
# SKIPTEST ?= 1

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswbuildslave.xml
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKDIR)/cswbuildslave.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswbuildslave.xml
	@$(MAKECOOKIE)

