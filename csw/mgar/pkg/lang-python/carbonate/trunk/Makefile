# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = carbonate
VERSION = 0.2.2
CATEGORIES = python

DESCRIPTION = Tools for managing federated carbon clusters

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += carbonate.conf

# This is a new package, don't bother building for 2.6
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWcarbonate
SPKG_DESC_CSWcarbonate = Tools for managing federated carbon clusters
# PKGFILES is catchall
ARCHALL_CSWcarbonate = 1
# The binaries like carbon-cache.py need this
RUNTIME_DEP_PKGS_CSWcarbonate += CSWpython27
# Checkpkg can't detect this
CHECKPKG_OVERRIDES_CSWcarbonate += surplus-dependency|CSWpython27

# This is intended
CHECKPKG_OVERRIDES_CSWcarbonate += python-package-missing-py26-files

# This is more of a tool than python-related
CHECKPKG_OVERRIDES_CSWcarbonate += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWcarbonate += catalogname-does-not-start-with-py_

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = /opt/graphite/conf/carbonate.conf
REINPLACE_WITH_conf = $(sysconfdir)/graphite/carbonate.conf
REINPLACE_FILES_conf += carbonate/util.py

PRESERVECONF = $(sysconfdir)/graphite/carbonate.conf

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKDIR)/carbonate.conf $(DESTDIR)$(sysconfdir)/graphite/carbonate.conf
	@$(MAKECOOKIE)
