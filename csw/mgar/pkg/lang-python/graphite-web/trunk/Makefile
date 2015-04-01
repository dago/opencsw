# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = graphite-web
VERSION = 0.9.13
CATEGORIES = python

DESCRIPTION = Enterprise scalable realtime graphing

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWgraphite-web
SPKG_DESC_CSWgraphite-web = Enterprise scalable realtime graphing
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-django
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-django-tagging
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-carbon
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-whisper
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWap2modwsgi
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-cairo
RUNTIME_DEP_PKGS_CSWgraphite-web += CSWpy-simplejson
# python-hashlib is included in Python 2.5+

CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-django
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-django-tagging
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-carbon
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-whisper
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWap2modwsgi
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-cairo
CHECKPKG_OVERRIDES_CSWgraphite-web += surplus-dependency|CSWpy-simplejson

# This is /usr/share/lib/zoneinfo
CHECKPKG_OVERRIDES_CSWgraphite-web += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/graphite/thirdparty/pytz/__init__.py
CHECKPKG_OVERRIDES_CSWgraphite-web += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/graphite/thirdparty/pytz/__init__.py

# Use upstream naming for main package
CHECKPKG_OVERRIDES_CSWgraphite-web += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWgraphite-web += catalogname-does-not-start-with-py_

# requires = Django => 1.1.4
#            django-tagging
#            carbon
#            whisper
#            mod_wsgi
#            pycairo
#            pycairo-devel
#            python-simplejson
#            python-sqlite2
#            python-hashlib

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

post-extract:
	-cd $(WORKSRC) && mv setup.cfg setup.cfg.orig
	@$(MAKECOOKIE)

