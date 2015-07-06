# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = carbonate
VERSION = 0.2.2
CATEGORIES = python

DESCRIPTION = Tools for managing federated carbon clusters

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# This is a new package, don't bother building for 2.6
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWpy-carbonate
SPKG_DESC_CSWpy-carbon = Tools for managing federated carbon clusters
# PKGFILES is catchall
ARCHALL_CSWpy-carbon = 1
# The binaries like carbon-cache.py need this
RUNTIME_DEP_PKGS_CSWpy-carbon += CSWpython27

# This is intended
CHECKPKG_OVERRIDES_CSWpy-carbonate += python-package-missing-py26-files

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = /opt/graphite/conf/carbonate.conf
REINPLACE_WITH_conf = $(sysconfdir)/graphite/carbonate.conf
REINPLACE_FILES_conf += carbonate/util.py

include gar/category.mk
