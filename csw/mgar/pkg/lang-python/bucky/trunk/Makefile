# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = bucky
VERSION = 2.3.0
CATEGORIES = python

DESCRIPTION = StatsD and CollectD adapter for Graphite

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWpy-bucky
SPKG_DESC_CSWpy-bucky = StatsD and CollectD adapter for Graphite
# PKGFILES is catchall
ARCHALL_CSWpy-bucky = 1
RUNTIME_DEP_PKGS_CSWpy-bucky += CSWpy-setproctitle
# Checkpkg can't track this
CHECKPKG_OVERRIDES_CSWpy-bucky += surplus-dependency|CSWpy-setproctitle

# This is a new package, don't bother building for 2.6
MODULATIONS_PYTHON_VERSION = 2_7
CHECKPKG_OVERRIDES_CSWpy-bucky += python-package-missing-py26-files

# For types.db from CollectD
REINPLACE_USRLOCAL += bucky/collectd.py

# This is also for types.db
CHECKPKG_OVERRIDES_CSWpy-bucky += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/bucky/collectd.py

include gar/category.mk
